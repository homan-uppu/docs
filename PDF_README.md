# PDF Documentation Generator

This script generates a single PDF file containing all your documentation files in the order specified by your `docs.json` schema.

## Files Created

- `generate_pdf_docs.py` - Main Python script that generates the PDF
- `requirements.txt` - Required Python packages
- `run_pdf_generator.sh` - Convenience script that handles environment setup
- `documentation.pdf` - Generated PDF output (created when you run the script)

## How to Use

### Option 1: Using the convenience script (recommended)

```bash
./run_pdf_generator.sh
```

This script will automatically:

- Create a virtual environment if needed
- Install required dependencies
- Generate the PDF
- Show you the results

### Option 2: Manual setup

```bash
# Create virtual environment
python3 -m venv pdf_env
source pdf_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Generate PDF
python generate_pdf_docs.py
```

## What the Script Does

1. **Reads `docs.json`** - Parses your documentation schema to understand the structure and order
2. **Processes files in order** - Goes through each page listed in the schema in the exact order specified
3. **Handles different sections** - Creates section headers for each group (Getting Started, Fundraise, Invest, Other)
4. **Converts MDX to PDF** - Converts your MDX files to PDF format, handling:
   - Frontmatter (title extraction)
   - Markdown headers
   - Basic formatting
   - Empty files (shows "[This section is currently empty]")
5. **Generates single PDF** - Creates `documentation.pdf` with all content

## Features

- ✅ Maintains the exact order from `docs.json`
- ✅ Handles empty or incomplete files gracefully
- ✅ Extracts titles from frontmatter or headers
- ✅ Creates section dividers for different groups
- ✅ Clean, readable PDF formatting
- ✅ Progress reporting during generation

## Output

The generated PDF will have:

- Main title: "PersonalTokenNet" (from your docs.json name)
- Section headers for each group
- Individual page titles and content
- Proper spacing and formatting

## Customization

You can modify `generate_pdf_docs.py` to:

- Change PDF styling (fonts, colors, spacing)
- Modify how MDX content is processed
- Add table of contents
- Change page layout or margins
- Add custom headers/footers
