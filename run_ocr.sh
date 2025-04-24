#!/bin/bash

# Script for running the PDF OCR CLI tool with proper environment configuration

# Set environment variables for Tesseract
export TESSDATA_PREFIX="/opt/homebrew/share/tessdata"

# Run the PDF OCR CLI tool
python -m pdf_ocr "$@"
