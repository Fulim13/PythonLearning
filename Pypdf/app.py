import PyPDF2
from pypdf import PdfReader

#OLD VERSION

#Reader and Writer
# with open("first.pdf","rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     print(len(reader.pages))
#     page1 = reader.pages[0]
#     page1.rotate(90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page1)
#     # writer.insert_page(page1,5)
#     # writer.insert_blank_page
#     with open("rotated.pdf","wb") as output:
#         writer.write(output)

#MERGER
# merger = PyPDF2.PdfMerger()
# file_names = ["first.pdf","second.pdf"]
# for file_name in file_names:
#     merger.append(file_name)
# merger.write("combined.pdf")
    
    
# NEWER VERSION
reader = PdfReader("first.pdf")
page = reader.pages[0]
print(page.extract_text())
#Git Cheat Sheet  The essential Git commands every developer must know

#DOCUMENTATION
# https://pypdf2.readthedocs.io/en/stable/user/extract-text.html