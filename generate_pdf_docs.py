#!/usr/bin/env python3
"""
Script to generate a single markdown file containing all documentation files
in the order specified by docs.json schema.
"""

import json
import os
from pathlib import Path
import re

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

def convert_mdx_to_markdown(content):
    """Convert MDX content to clean markdown, removing JSX components but preserving markdown formatting."""
    if not content:
        return ""
    
    # Remove JSX components and HTML tags while preserving content
    # Handle image tags - convert to markdown image syntax
    content = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*/?>', r'![\\2](\\1)', content)
    content = re.sub(r'<img[^>]*alt=["\']([^"\']*)["\'][^>]*src=["\']([^"\']*)["\'][^>]*/?>', r'![\\1](\\2)', content)
    
    # Remove other HTML/JSX tags but keep their content
    content = re.sub(r'<div[^>]*>', '', content)
    content = re.sub(r'</div>', '', content)
    content = re.sub(r'<[^>]+>', '', content)
    
    # Clean up extra whitespace but preserve paragraph breaks
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    content = re.sub(r'^\s+', '', content, flags=re.MULTILINE)
    
    return content.strip()

def generate_markdown(output_filename="documentation.md"):
    """Main function to generate the markdown documentation."""
    print("Starting markdown generation...")
    
    # Read the schema
    schema = read_docs_schema()
    pages = extract_pages_from_schema(schema)
    
    print(f"Found {len([p for p in pages if p['type'] == 'page'])} pages to process")
    
    # Build the markdown content
    markdown_content = []
    
    # Add main title
    main_title = schema.get('name', 'Documentation')
    markdown_content.append(f"# {main_title}")
    markdown_content.append("")  # Empty line
    
    processed_pages = 0
    skipped_pages = 0
    current_group = None
    
    # Process each page
    for page_info in pages:
        if page_info['type'] == 'group_header':
            # Add group header as H2
            current_group = page_info['title']
            markdown_content.append(f"## {page_info['title']}")
            markdown_content.append("")  # Empty line
            
        elif page_info['type'] == 'page':
            # Read the MDX file
            file_path = f"{page_info['path']}.mdx"
            title, content = read_mdx_file(file_path)
            
            if title and content:
                # Add page title as H3
                markdown_content.append(f"### {title}")
                markdown_content.append("")  # Empty line
                
                # Convert and add content
                markdown_text = convert_mdx_to_markdown(content)
                if markdown_text:
                    markdown_content.append(markdown_text)
                    markdown_content.append("")  # Empty line after content
                    markdown_content.append("---")  # Separator between sections
                    markdown_content.append("")  # Empty line after separator
                
                processed_pages += 1
            else:
                print(f"Skipping {file_path} - could not read content")
                skipped_pages += 1
    
    # Write the markdown file
    final_content = '\n'.join(markdown_content)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Markdown file generated successfully: {output_filename}")
    print(f"Processed: {processed_pages} pages, Skipped: {skipped_pages} pages")

if __name__ == "__main__":
    generate_markdown() 