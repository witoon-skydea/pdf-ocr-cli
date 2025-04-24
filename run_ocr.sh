#!/bin/bash

# Script for running the PDF OCR CLI tool with proper environment configuration

# Set environment variables for Tesseract
export TESSDATA_PREFIX="/opt/homebrew/share/tessdata"

# Display available languages
echo "Available OCR languages:"
tesseract --list-langs

# Display help message
if [ "$1" == "--help" ] || [ "$1" == "-h" ] || [ -z "$1" ]; then
    echo ""
    echo "PDF OCR CLI Tool"
    echo "---------------"
    echo "Usage: ./run_ocr.sh [options] your_file.pdf"
    echo ""
    echo "Default: Will use Tesseract OCR with Thai and English language support"
    echo ""
    echo "Common options:"
    echo "  -o, --output PATH        Output file path"
    echo "  -e, --engine ENGINE      OCR engine to use (tesseract or easyocr)"
    echo "  -l, --lang LANG          Language codes (e.g., tha, eng, tha+eng)"
    echo "  -d, --dpi DPI            DPI setting for image conversion"
    echo "  -v, --verbose            Enable verbose output"
    echo ""
    echo "For complete options: python -m pdf_ocr --help"
    echo ""
    
    # Exit if no arguments provided
    [ -z "$1" ] && exit 0
fi

# Run the PDF OCR CLI tool
python -m pdf_ocr "$@"
