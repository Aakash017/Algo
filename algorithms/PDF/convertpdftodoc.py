from pdf2docx import Converter

# pdf_file="/Users/aakashsharma/Documents/projects/Algo/Aakash_Sharma's_Offer_Letter.pdf"
# docx_file="/Users/aakashsharma/Documents/projects/Algo/sample.docx"
# cv=Converter(pdf_file)
# cv.convert(docx_file)
# cv.close()


from docx2pdf import convert
docx_file="/Users/aakashsharma/Documents/projects/Algo/sample.docx"
pdf_file="/Users/aakashsharma/Documents/projects/Algo/sample.pdf"
convert(docx_file)