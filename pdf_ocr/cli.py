"""
Command-line interface for PDF OCR CLI.
"""

import os
import sys
import click
from pathlib import Path
from typing import Optional
import logging

from .ocr import convert_pdf_to_text

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@click.command()
@click.argument('pdf_path', type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option('-o', '--output', 'output_path', type=click.Path(dir_okay=False, writable=True),
              help='Path to save the extracted text to. If not provided, the text will be saved to the same location as the PDF with a .txt extension.')
@click.option('-e', '--engine', type=click.Choice(['tesseract', 'easyocr'], case_sensitive=False),
              default='tesseract', help='OCR engine to use.')
@click.option('-l', '--lang', default='tha', help='Language code(s) for OCR (e.g., "tha" for Thai, "tha+eng" for Thai and English).')
@click.option('-d', '--dpi', type=int, default=300, help='DPI setting for PDF to image conversion.')
@click.option('-t', '--tesseract-cmd', help='Path to Tesseract executable (if not in PATH).')
@click.option('--tessdata-dir', help='Path to directory containing Tesseract language data files.')
@click.option('-g', '--gpu/--no-gpu', default=True, help='Use GPU for OCR (only for EasyOCR).')
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose output.')
def main(
    pdf_path: str,
    output_path: Optional[str] = None,
    engine: str = 'tesseract',
    lang: str = 'tha',
    dpi: int = 300,
    tesseract_cmd: Optional[str] = None,
    tessdata_dir: Optional[str] = None,
    gpu: bool = True,
    verbose: bool = False
):
    """
    Extract text from a PDF file using OCR.
    
    PDF_PATH is the path to the PDF file to extract text from.
    """
    # Set logging level
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)
    
    # Determine output path if not provided
    if not output_path:
        output_path = str(Path(pdf_path).with_suffix('.txt'))
    
    # Additional arguments for OCR engine
    kwargs = {}
    if engine == 'tesseract':
        if tesseract_cmd:
            kwargs['tesseract_cmd'] = tesseract_cmd
        if tessdata_dir:
            kwargs['tessdata_dir'] = tessdata_dir
    elif engine == 'easyocr':
        kwargs['use_gpu'] = gpu
    
    try:
        # Convert PDF to text
        click.echo(f"Converting {pdf_path} to text using {engine}...")
        convert_pdf_to_text(
            pdf_path=pdf_path,
            output_path=output_path,
            engine=engine,
            lang=lang,
            dpi=dpi,
            **kwargs
        )
        click.echo(f"Text extracted and saved to: {output_path}")
    except Exception as e:
        logger.error(f"Error: {e}")
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
