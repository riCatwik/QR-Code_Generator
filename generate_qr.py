#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2023-12-08 at 01:56:36 CET

Machine: ritwikdas @ C2N_Linux 
OS: Red Hat® Enterprise Linux® 8.6 (RHEL LF Unix)
RHEL License Holder: Ritwik Das (Individual license)
License Information: RHDS 10x7xx17, Beta Access 10x7xx19

@author: Ritwik DAS (ritwik.das29@gmail.com)
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont


def generate_qr(
    url,
    name="website",
    logo_path=None,
    text=None,
    logo_size=80,
    text_font_size=20,
    qr_color="purple",
    background="white",
):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color=qr_color, back_color=background).convert("RGB")

    if logo_path:
        # Add logo to the QR code
        logo = Image.open(logo_path)
        logo.thumbnail((logo_size, logo_size))
        logo_pos = (
            (img.size[0] - logo.size[0]) // 2,
            (img.size[1] - logo.size[1]) // 2,
        )
        img.paste(logo, logo_pos, mask=logo)

    if text:
        # Add artistic text under the QR code
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", text_font_size)

        # Calculate the bounding box for the text
        text_box = draw.textbbox((0, 0), text, font=font)
        text_width = text_box[2] - text_box[0]
        text_height = text_box[3] - text_box[1]

        # Calculate the position for the text to appear at the bottom center
        text_x = (img.size[0] - text_width) // 2
        text_y = img.size[1] - text_height - 10  # 10 pixels from the bottom

        # Add some artistic styling (e.g., shadow effect)
        shadow_color = "grey"
        # Draw shadow first
        draw.text((text_x + 2, text_y + 2), text, font=font, fill=shadow_color)
        # Draw text
        draw.text((text_x, text_y), text, font=font, fill=qr_color)

    # Save it somewhere, change the path as needed
    img.save(f"QR_{name}.png")


## ======================================================== ##
## ======================================================== ##


## Define the full website URL (will be redirected to this link)
url = "https://ritwikdas.gitlab.io"

## Naming convention of the website URL
name = "ritwikdas.gitlab.io"

## Path to logo image (optional)
logo_path = "favicon-2.png"

## Text to add under the QR code (optional)
text = "RITWIK DAS"

## Call the generate_qr function with the given URL, logo path, and text
## You can now specify the logo size, text font size, QR color, and background color as needed
generate_qr(
    url,
    name,
    logo_path=logo_path,
    text=text,
    logo_size=100,
    text_font_size=35,
    qr_color="navy",
    background="white",
)
