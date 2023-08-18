import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from writebytes import extractImg
from reverse import revertb64ToImg
import os

def get_post_projects(input_name: str):
    """Scrap past project of given name from itb's web then generate pdf"""
    # Get HTML document from web page
    name = "-".join(input_name.lower().split(" "))
    url = f'https://www.itb.ac.id/staf/profil/{name}'
    response = requests.get(url)
    html_content = response.text

    # save html
    with open('docs.html', 'w') as html:
        html.writelines(html_content)

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    post_proj = soup.find("ul", class_="post-project")
    post_proj_text = post_proj.get_text(separator='\n') if post_proj else "No post projects found."

    # Clean and split the text
    cleaned_text = "\n".join(line.strip() for line in post_proj_text.splitlines() if line.strip())
    post_proj_text = cleaned_text

    with open("postprojs.txt", "w", encoding="utf-8") as txt_file:
        txt_file.writelines(post_proj_text)

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=25)
    pdf.set_margins(27, 27, 27)
    pdf.set_font("Arial", size=15)
    pdf.set_x(27)
    pdf.cell(0, 27, txt=input_name, align='C')
    pdf.set_font("Arial", size=10)

    try:
        extractImg(name, html_content)
        pdf, img_h = revertb64ToImg(name=name, pdfile=pdf)
        print(f"Gambar {input_name} berhasil disimpan!")
    except:
        print("Gagal mengonversi gambar")

    with open("postprojs.txt", "r", encoding="utf-8") as txt:
        entry = 1
        for line in txt.readlines():
            if line == '\n':
                continue
            if entry == 1:
                pdf.set_y(42 + img_h)
                pdf.set_x(27)  # Adjust the horizontal position for the first line
            pdf.multi_cell(0, 10, txt=f"{entry}. " + line, align='J')
            entry += 1

    pdf.output(" ".join(name.capitalize() for name in name.split("-")) + ".pdf")

    print(f"PDF berhasil dibuat: " + " ".join(name.capitalize() for name in name.split("-")) + ".pdf")
    os.remove('docs.html')
    os.remove('image-data.txt')
    os.remove('temp_image.png')
    os.remove('postprojs.txt')


    


nama = input("Masukkan nama dosen: ")
get_post_projects(nama)