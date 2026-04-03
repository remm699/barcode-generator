# Barcode Generator

A Python GUI application for generating EAN-13 barcodes from 12-digit input.

## Features
- Simple Tkinter interface
- Real-time barcode preview
- Save barcode images (PNG, JPEG, etc.)
- Input validation (exactly 12 digits required)
- Automatic checksum calculation

## Installation
```bash
# Clone or download this repository
git clone <repository-url>
cd barcode-generator

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
python barcode_generator.py
```

1. Enter exactly 12 digits in the input field
2. Press Enter or click "Générer le code barre"
3. Preview the generated barcode
4. Click "Enregistrer l'image" to save
5. Use "Effacer" to reset the form

## How It Works
- Uses the `python-barcode` library to generate standard EAN-13 barcodes
- The 12 input digits are used to calculate the 13th checksum digit automatically
- Barcode images are generated in memory and displayed using Tkinter Canvas
- Original PIL Image is preserved for saving to disk

## Requirements
- Python 3.x
- python-barcode>=0.16.1
- Pillow>=12.2.0

## Testing the Application
Run the application and test with sample data:
- Enter: 123456789012
- Should generate a valid EAN-13 barcode

## Customization Options
### Change Barcode Type
Modify the barcode type in `barcode_generator.py`:
```python
# Other options: 'ean8', 'upca', 'code128', etc.
ean = barcode.get('ean13', code12, writer=ImageWriter())
```

### Adjust Display Size
Change the display_width variable in `generate_barcode()`:
```python
display_width = 400  # Increase for larger preview
```

## Notes
1. The application generates EAN-13 barcodes which require 12 data digits + 1 checksum digit
2. Input validation prevents invalid barcodes from being generated
3. Images are generated in memory first, then displayed and saved
4. The application is cross-platform (Windows, macOS, Linux)
5. No external services or API keys required