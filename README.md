# QR Code Generator

This QR Code Generator is an advanced, yet user-friendly Python tool that allows for the creation of customized QR codes. It comes with enhanced capabilities, including color customization, logo insertion, and the addition of styled text. It's ideal for both personal and professional QR code generation needs.

## Features

- Generate customizable QR codes for any URL.
- Options to alter QR code color and background.
- Incorporate a logo within the QR code.
- Add styled text beneath the QR code for additional information or branding.
- Enhanced customization for logo size and text font size.

## Requirements

- Python 3.x
- Pillow library
- qrcode library

## Installation

Ensure Python is installed on your system. Install the required libraries (`Pillow` and `qrcode`) using pip if you haven't already:

```bash
pip install pillow qrcode
```

## Usage

Execute the script with Python to generate a QR code. The QR code will be saved as an image file:

```bash
python generate_qr.py
```

Default settings:

- URL: `https://ritwikdas.gitlab.io`
- Logo: `favicon-2.png` (place in the script's directory or specify the path)
- Text: "RITWIK DAS"
- QR Color: Navy
- Background: White
- Logo Size: 100 (pixels)
- Text Font Size: 35 (points)

These settings can be customized in the script.

## Customization

Modify the parameters in the `generate_qr` function call for personalization:

- `url`: URL for the QR code.
- `name`: Naming convention for the QR code image file.
- `logo_path`: Path to the logo image.
- `text`: Custom text below the QR code.
- `logo_size`: Size of the embedded logo.
- `text_font_size`: Font size of the text.
- `qr_color`: Color of the QR code.
- `background`: Background color of the QR code.

## Contributing

Contributions are welcome! Please open an issue first to discuss significant changes.

## License

This project is open source, available under the [MIT License](LICENSE).
