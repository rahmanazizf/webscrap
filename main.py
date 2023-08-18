from src.readpdf import get_post_projects
import os

welcome = """
==========================================================
Selamat Datang di Web Scrapper untuk Data Proyek Dosen ITB
==========================================================
1. Ambil Data
2. Keluar
"""

while True:
    print(welcome)
    opt = input("Pilih: ")
    if opt == '1':
        nama = input("Masukkan nama dosen: ")
        get_post_projects(nama)
    elif opt == '2':
        break
    else:
        print("Input yang Anda berikan tidak valid.")
        continue