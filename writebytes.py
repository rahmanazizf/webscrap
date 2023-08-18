import requests
from bs4 import BeautifulSoup
# from fpdf import FPDF
# import base64
# from PIL import Image
# from io import BytesIO

# Get HTML document from web page
def extractImg(name: str, html):
    """Extract bytes image from html document then store it in 'image-data.txt'"""
    # url = f'https://www.itb.ac.id/staf/profil/{"-".join(name.lower().split(" "))}'  # Ganti dengan URL yang sesuai
    # response = requests.get(url)
    # html_content = response.text

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find the img element containing base64-encoded image
    img_element = soup.find("img", class_='img-fluid')
    with open('image-data.txt', 'w') as img:
        img.writelines(str(img_element['src'].split(',')[-1]))
# if img_element:
#     img_src = img_element['src']
#     print(img_src)
#     # img_data = img_src.split(',')[1]  # Extract base64-encoded data

#     # Decode base64 image data
#     image_bytes = base64.b64decode(img_src)

#     # Open image using PIL
#     image = Image.open(BytesIO(image_bytes))

#     # Create PDF
#     pdf = FPDF()
#     pdf.add_page()

#     # Calculate width and height to maintain aspect ratio
#     img_width, img_height = image.size
#     pdf_width = 210  # A4 width in mm
#     scale_factor = pdf_width / img_width
#     pdf_height = img_height * scale_factor

#     pdf.image(BytesIO(image_bytes), x=10, y=10, w=pdf_width-20, h=pdf_height-20)

#     # Output PDF
#     pdf.output("image_to_pdf.pdf")

#     print("PDF generated successfully.")
# else:
#     print("Image element not found in HTML.")
