#!/bin/bash

# Script to generate PDF documentation
# This script will set up a virtual environment if needed and run the PDF generator

echo "📚 PDF Documentation Generator"
echo "==============================="

# Check if virtual environment exists
if [ ! -d "pdf_env" ]; then
    echo "🔧 Setting up virtual environment..."
    python3 -m venv pdf_env
    source pdf_env/bin/activate
    pip install -r requirements.txt
else
    echo "✅ Virtual environment found, activating..."
    source pdf_env/bin/activate
fi

# Check if reportlab is installed
python -c "import reportlab" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing required packages..."
    pip install -r requirements.txt
fi

# Run the PDF generator
echo "🚀 Generating PDF documentation..."
python generate_pdf_docs.py

# Check if PDF was generated successfully
if [ -f "documentation.pdf" ]; then
    echo "✅ PDF generated successfully: documentation.pdf"
    echo "📄 File size: $(ls -lh documentation.pdf | awk '{print $5}')"
else
    echo "❌ PDF generation failed"
    exit 1
fi 