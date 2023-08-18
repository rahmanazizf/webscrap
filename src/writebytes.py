from bs4 import BeautifulSoup

# Get HTML document from web page
def extractImg(html):
    """Extract bytes image from html document then store it in 'image-data.txt'"""

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find the img element containing base64-encoded image
    img_element = soup.find("img", class_='img-fluid')
    with open('image-data.txt', 'w') as img:
        img.writelines(str(img_element['src'].split(',')[-1]))

