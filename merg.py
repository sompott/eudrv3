import os
from PyPDF2 import PdfFileMerger

def merge_pdfs_in_folder(folder_path, output_filename):
    merger = PdfFileMerger()

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            merger.append(pdf_path)

    merger.write(output_filename)
    merger.close()
# เรียกใช้งานฟังก์ชัน
folder_path = 'pdfs'  # แทนที่ด้วยเส้นทางของโฟลเดอร์ของคุณ
output_filename = 'merged_pdf1.pdf'  # ชื่อไฟล์ PDF ที่จะเป็นผลลัพธ์
merge_pdfs_in_folder(folder_path, output_filename)
