#!/usr/bin/env python3
"""
Script to generate a single PDF containing all documentation files
in the order specified by docs.json schema.
"""

import json
import os
from pathlib import Path
import re
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor

def read_docs_schema(schema_path="docs.json"):
    """Read and parse the docs.json file to get the structure."""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_pages_from_schema(schema):
    """Extract the ordered list of pages from the schema."""
    pages = []
    
    # Navigate through the schema structure to extract pages
    if 'navigation' in schema and 'tabs' in schema['navigation']:
        for tab in schema['navigation']['tabs']:
            if 'groups' in tab:
                for group in tab['groups']:
                    if 'pages' in group:
                        # Add group info for section headers
                        pages.append({
                            'type': 'group_header',
                            'title': group['group']
                        })
                        # Add individual pages
                        for page in group['pages']:
                            pages.append({
                                'type': 'page',
                                'path': page,
                                'group': group['group']
                            })
    
    return pages

def read_mdx_file(file_path):
    """Read and parse an MDX file, extracting title and content."""
    if not os.path.exists(file_path):
        print(f"Warning: File {file_path} not found")
        return None, None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file is empty or only whitespace
        if not content.strip():
            print(f"Info: File {file_path} is empty or contains only whitespace")
            # Still return the filename as title for empty files
            title = os.path.basename(file_path).replace('.mdx', '').replace('-', ' ').title()
            return title, "[This section is currently empty]"
        
        # Extract title from the first line if it's a markdown header
        lines = content.split('\n')
        title = None
        content_start = 0
        
        # Look for title in frontmatter or first heading
        if lines and lines[0].startswith('---'):
            # Handle frontmatter
            end_frontmatter = -1
            for i, line in enumerate(lines[1:], 1):
                if line.strip() == '---':
                    end_frontmatter = i
                    break
                if line.startswith('title:'):
                    title = line.replace('title:', '').strip().strip('"\'')
            
            if end_frontmatter > 0:
                content_start = end_frontmatter + 1
        
        # If no title found in frontmatter, look for first heading
        if not title:
            for i, line in enumerate(lines[content_start:], content_start):
                if line.startswith('#'):
                    title = line.lstrip('#').strip()
                    content_start = i + 1
                    break
        
        # If still no title, use filename
        if not title:
            title = os.path.basename(file_path).replace('.mdx', '').replace('-', ' ').title()
        
        # Get the actual content
        actual_content = '\n'.join(lines[content_start:]).strip()
        
        return title, actual_content
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None

def convert_mdx_to_text(content):
    """Convert MDX content to plain text suitable for PDF."""
    if not content:
        return ""
    
    # Remove JSX components and HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Convert markdown formatting to simple text indicators
    content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)  # Bold
    content = re.sub(r'\*(.*?)\*', r'\1', content)      # Italic
    content = re.sub(r'`(.*?)`', r'"\1"', content)      # Inline code
    
    # Handle code blocks
    content = re.sub(r'```[\s\S]*?```', '[Code Block]', content)
    
    # Clean up extra whitespace
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content.strip()

def create_pdf_styles():
    """Create custom styles for the PDF."""
    styles = getSampleStyleSheet()
    
    # Custom title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        textColor=HexColor('#000000'),
        alignment=0  # Left alignment
    )
    
    # Custom group header style
    group_style = ParagraphStyle(
        'GroupHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=20,
        spaceAfter=10,
        textColor=HexColor('#333333'),
        alignment=0
    )
    
    # Custom body text style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        alignment=0
    )
    
    return {
        'title': title_style,
        'group': group_style,
        'body': body_style,
        'normal': styles['Normal']
    }

def generate_pdf(output_filename="documentation.pdf"):
    """Main function to generate the PDF documentation."""
    print("Starting PDF generation...")
    
    # Read the schema
    schema = read_docs_schema()
    pages = extract_pages_from_schema(schema)
    
    print(f"Found {len([p for p in pages if p['type'] == 'page'])} pages to process")
    
    # Create PDF document
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        rightMargin=inch,
        leftMargin=inch,
        topMargin=inch,
        bottomMargin=inch
    )
    
    # Get styles
    styles = create_pdf_styles()
    
    # Build the story (content for PDF)
    story = []
    
    # Add main title
    main_title = schema.get('name', 'Documentation')
    story.append(Paragraph(main_title, styles['title']))
    story.append(Spacer(1, 20))
    
    processed_pages = 0
    skipped_pages = 0
    
    # Process each page
    for page_info in pages:
        if page_info['type'] == 'group_header':
            # Add group header
            story.append(Paragraph(page_info['title'], styles['group']))
            story.append(Spacer(1, 10))
            
        elif page_info['type'] == 'page':
            # Read the MDX file
            file_path = f"{page_info['path']}.mdx"
            title, content = read_mdx_file(file_path)
            
            if title and content:
                # Add page title
                story.append(Paragraph(title, styles['title']))
                story.append(Spacer(1, 10))
                
                # Convert and add content
                text_content = convert_mdx_to_text(content)
                if text_content:
                    # Split content into paragraphs
                    paragraphs = text_content.split('\n\n')
                    for para in paragraphs:
                        if para.strip():
                            story.append(Paragraph(para.strip(), styles['body']))
                            story.append(Spacer(1, 6))
                
                # Add some space after each document
                story.append(Spacer(1, 20))
                processed_pages += 1
            else:
                print(f"Skipping {file_path} - could not read content")
                skipped_pages += 1
    
    # Build the PDF
    print(f"Building PDF: {output_filename}")
    print(f"Processed: {processed_pages} pages, Skipped: {skipped_pages} pages")
    doc.build(story)
    print(f"PDF generated successfully: {output_filename}")

if __name__ == "__main__":
    # Check if required packages are available
    try:
        import reportlab
    except ImportError:
        print("Error: reportlab package is required.")
        print("Install it with: pip install reportlab")
        exit(1)
    
    generate_pdf() 