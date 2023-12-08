# QR Code Generator

This QR Code Generator is a simple yet powerful Python tool that creates QR codes with the option to customize the color, add a logo, and include artistic text. Designed to be easy to use and modify, it's perfect for generating QR codes for personal or professional use.

## Features

- Generate QR codes for any URL.
- Customize QR code color and background.
- Add a logo to the center of the QR code.
- Include custom text beneath the QR code with artistic effects.

## Requirements

- Python 3.x
- Pillow library
- qrcode library

## Installation

To run this script, you will need Python installed on your system. If you don't have the required libraries (`Pillow` and `qrcode`), install them using pip:

```bash
pip install pillow qrcode
```

## Usage

To generate a QR code, simply execute the script with Python and the generated QR code will be saved as an image file:

```bash
python generate_qr.py
```

The default settings are:

- URL: `https://ritwikdas.gitlab.io`
- Logo: `favicon-2.png` (Place your logo in the script's directory or specify the path)
- Text: "RITWIK DAS"
- QR Color: Navy
- Background: White

You can customize these settings directly in the script.

## Customization

To customize your QR code, modify the parameters in the `generate_qr` function call at the bottom of the script:

- `url`: The URL that the QR code will point to.
- `logo_path`: The path to the logo image you want to embed in the QR code.
- `text`: The text you want to display beneath the QR code.
- `logo_size`: The size of the logo within the QR code.
- `text_font_size`: The font size of the text beneath the QR code.
- `qr_color`: The color of the QR code.
- `background`: The background color of the QR code.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [MIT License](LICENSE).
