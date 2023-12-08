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
    logo_size=100,
    text_font_size=40,
    qr_color="navy",
    background="white",
    canvas_color="navy",
    border_size=10,
):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_img = qr.make_image(fill_color=qr_color, back_color=background).convert("RGB")

    # Add logo to the QR code if a path is provided
    if logo_path:
        logo = Image.open(logo_path)
        logo.thumbnail((logo_size, logo_size))
        logo_pos = (
            (qr_img.size[0] - logo.size[0]) // 2,
            (qr_img.size[1] - logo.size[1]) // 2,
        )
        qr_img.paste(logo, logo_pos, mask=logo)

    # Calculate the total canvas size, accounting for the border
    canvas_width = qr_img.size[0] + 2 * border_size
    canvas_height = qr_img.size[1] + 2 * border_size + text_font_size

    # Create a larger canvas for QR code and text
    canvas = Image.new("RGB", (canvas_width, canvas_height), canvas_color)

    # Paste the QR image onto the canvas, centered at the top with a border
    qr_position = (border_size, border_size)
    canvas.paste(qr_img, qr_position)

    # Initialize drawing context for text
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("arial.ttf", text_font_size)

    # Use textbbox to calculate the bounding box for the text
    text_box = draw.textbbox((0, 0), text, font=font)
    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]

    # Calculate text position for center alignment within the blue box
    text_x = (canvas_width - text_width) // 2
    text_y = canvas_height - border_size - (text_font_size + text_height)//1.8

    # Draw the text
    draw.text((text_x, text_y), text, font=font, fill=background)

    # Save the resulting image
    canvas.save(f"QR_{name}.png")


## ======================================================== ##
## ======================================================== ##


# Define the full website URL (will be redirected to this link)
url = "https://ritwikdas.gitlab.io"

# Naming convention of the website URL
name = "ritwikdas.gitlab.io"

# Path to logo image (optional)
logo_path = "favicon-2.png"  # Replace with the path to your logo image

# Text to add under the QR code (optional)
text = "RITWIK DAS"

# Call the generate_qr function with the given URL and text
generate_qr(
    url,
    name,
    logo_path=logo_path,
    text=text,
    logo_size=100,
    text_font_size=50,
    qr_color="navy",
    background="white",
    canvas_color="navy",
    border_size=10,
)
