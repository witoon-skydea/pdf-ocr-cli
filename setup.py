"""
Setup script for PDF OCR CLI.
"""

from setuptools import setup, find_packages
import os
import re

# Read the version from __init__.py
with open(os.path.join('pdf_ocr', '__init__.py'), 'r', encoding='utf-8') as f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Could not find version string")

# Read long description from README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pdf-ocr-cli',
    version=version,
    description='A command-line tool for extracting text from PDF files using OCR',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Witoon Pongsilathong',
    author_email='example@example.com',
    url='https://github.com/your-username/pdf-ocr-cli',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pdf-ocr=pdf_ocr.cli:main',
        ],
    },
    install_requires=[
        'PyMuPDF>=1.19.0',
        'Pillow>=9.0.0',
        'click>=8.0.0',
        'numpy>=1.20.0',
        'tqdm>=4.62.0',
    ],
    extras_require={
        'tesseract': ['pytesseract>=0.3.8'],
        'easyocr': ['easyocr>=1.5.0', 'torch>=1.10.0'],
        'all': ['pytesseract>=0.3.8', 'easyocr>=1.5.0', 'torch>=1.10.0']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
    keywords='pdf, ocr, text extraction, thai, cli',
)
