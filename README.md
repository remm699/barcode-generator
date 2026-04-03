# Barcode Generator & Reader

A Python GUI application for generating EAN-13 barcodes from 12-digit input and reading barcodes from images.

## Features
- **Generate**: Create EAN-13 barcodes from 12-digit input with automatic checksum calculation
- **Read**: Detect and decode barcodes from image files (PNG, JPEG, BMP, TIFF)
- **Preview**: Real-time display of generated or loaded barcode images
- **Save**: Save barcode images in PNG, JPEG, or other formats
- **Input validation**: Ensures exactly 12 digits are entered for generation
- **Multi-format support**: Reads various barcode formats (optimized for EAN-13)

## Installation
```bash
# Clone or download this repository
git clone https://github.com/remm699/barcode-generator
cd barcode-generator

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
python barcode_generator.py
```

### Génération de code-barres
1. Entrez exactement 12 chiffres dans le champ de saisie
2. Appuyez sur Entrée ou cliquez sur "Générer le code barre"
3. Prévisualisez le code-barres généré
4. Cliquez sur "Enregistrer l'image" pour sauvegarder
5. Utilisez "Effacer" pour réinitialiser le formulaire

### Lecture de code-barres depuis une image
1. Cliquez sur "Lire code barre depuis image"
2. Sélectionnez une image contenant un code-barres (PNG, JPEG, BMP, TIFF)
3. L'application tentera de décoder le code-barres
4. Si c'est un EAN-13 valide, les 12 chiffres seront affichés dans le champ de saisie
5. Vous pouvez ensuite enregistrer l'image ou générer un nouveau code-barres

## How It Works
- **Generation**: Uses the `python-barcode` library to generate standard EAN-13 barcodes
- **Reading**: Uses `pyzbar` (based on ZBar) to detect and decode barcodes from images
- The 12 input digits are used to calculate the 13th checksum digit automatically during generation
- Barcode images are generated/loaded in memory and displayed using Tkinter Canvas
- Original PIL Image is preserved for saving to disk

## Requirements
- Python 3.x
- python-barcode>=0.16.1
- Pillow>=12.2.0
- pyzbar>=0.1.9

## Testing the Application
1. Run the application: `python barcode_generator.py`
2. **Test de génération**: Entrez `123456789012` pour générer un code-barres EAN-13 valide
3. **Test de lecture**: Utilisez l'image générée pour tester la fonction de lecture

## Customization Options
### Change Barcode Type (Generation)
Modify the barcode type in `generate_barcode()`:
```python
# Other options: 'ean8', 'upca', 'code128', etc.
ean = barcode.get('ean13', code12, writer=ImageWriter())
```

### Adjust Display Size
Change the display_width variable in `generate_barcode()` and `read_barcode_from_image()`:
```python
display_width = 500  # Increase for larger preview
```

## Notes
1. The application generates EAN-13 barcodes which require 12 data digits + 1 checksum digit
2. Input generation prevents invalid barcodes from being generated
3. The reading function works with various barcode formats but is optimized for EAN-13
4. Images are processed in memory first, then displayed and saved
5. The application is cross-platform (Windows, macOS, Linux)
6. No external services or API keys required

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError: No module named 'tkinter' | Install python3-tk package (Linux) or ensure Python includes Tkinter |
| Barcode generation fails | Verify input is exactly 12 numeric digits |
| Image save fails | Check file permissions and available disk space |
| No barcode detected in image | Ensure the barcode is clear, well-lit, and fully visible in the image |
| Poor image quality during display | Adjust resize method or display dimensions |
| pyzbar import errors | Ensure pyzbar is properly installed (may require system dependencies like libzbar0) |

## Dependencies Explained
- **python-barcode**: Generates barcode images in various formats (EAN, UPC, Code128, etc.)
- **Pillow (PIL)**: Python Imaging Library for image manipulation and display
- **pyzbar**: Barcode reading library that wraps ZBar for detecting and decoding barcodes from images
- **Tkinter**: Standard Python GUI library (included with most Python distributions)

-- 
*This application allows both generation and reading of barcodes, making it a complete tool for barcode handling.*
