"""
Tests for PDF OCR CLI.
"""

import unittest
from pathlib import Path
import tempfile
import os
import shutil

from pdf_ocr.ocr import get_ocr_engine, TesseractOCR, EasyOCR


class TestOCREngines(unittest.TestCase):
    """Tests for OCR engines."""
    
    def test_get_ocr_engine_tesseract(self):
        """Test get_ocr_engine with tesseract."""
        try:
            engine = get_ocr_engine('tesseract')
            self.assertIsInstance(engine, TesseractOCR)
        except (ImportError, RuntimeError):
            self.skipTest("Tesseract not installed or configured correctly")
    
    def test_get_ocr_engine_easyocr(self):
        """Test get_ocr_engine with easyocr."""
        try:
            engine = get_ocr_engine('easyocr')
            self.assertIsInstance(engine, EasyOCR)
        except ImportError:
            self.skipTest("EasyOCR not installed")
    
    def test_invalid_engine(self):
        """Test get_ocr_engine with invalid engine."""
        with self.assertRaises(ValueError):
            get_ocr_engine('invalid_engine')


# Only run this test if you have sample PDF files available
class TestPDFConversion(unittest.TestCase):
    """Tests for PDF conversion."""
    
    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.output_path = os.path.join(self.temp_dir, 'output.txt')
        
        # Path to a sample PDF file (replace with an actual path if you have one)
        self.sample_pdf_path = None
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.temp_dir)
    
    def test_convert_pdf_to_text(self):
        """Test convert_pdf_to_text."""
        if self.sample_pdf_path is None or not os.path.exists(self.sample_pdf_path):
            self.skipTest("Sample PDF file not available")
        
        from pdf_ocr.ocr import convert_pdf_to_text
        
        try:
            # Test with Tesseract
            convert_pdf_to_text(
                pdf_path=self.sample_pdf_path,
                output_path=self.output_path,
                engine='tesseract',
                lang='tha',
                dpi=150  # Lower DPI for faster testing
            )
            
            # Check if output file exists
            self.assertTrue(os.path.exists(self.output_path))
            
            # Check if output file has content
            with open(self.output_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertGreater(len(content), 0)
        
        except (ImportError, RuntimeError):
            self.skipTest("Tesseract not installed or configured correctly")


if __name__ == '__main__':
    unittest.main()
