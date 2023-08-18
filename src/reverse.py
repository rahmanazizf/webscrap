import base64
import io
from PIL import Image
from fpdf import FPDF
import os

def revertb64ToImg(name :str, pdfile:FPDF, path: str = 'image-data.txt'):
    """
    Reverting bytes data extracted from html to image
    
    """
    # Read base64 data from text file
    input_file_path = path

    with open(input_file_path, 'r') as input_file:
        image_base64 = input_file.read()

    # Decode base64 data to binary
    image_data = base64.b64decode(image_base64)

    # Create Image object from binary data
    image = Image.open(io.BytesIO(image_data))

    # Save the image temporarily in a format like PNG or JPEG
    temp_image_path = 'temp_image.png'
    image.save(temp_image_path)

    # Calculate width and height to maintain aspect ratio
    img_width, img_height = image.size
    pdf_width = 40  # A4 width in mm
    scale_factor = pdf_width / img_width
    pdf_height = img_height * scale_factor

    # Add image to PDF
    pdfile.image(
            temp_image_path, 
              x=pdf_width + 45, 
              y=30, 
              w=pdf_width, 
              h=pdf_height
              )

    return pdfile, pdf_height

