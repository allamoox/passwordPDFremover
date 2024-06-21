#####Best PDF password remover EVER!!!!!!!######
######path the output  path and the password#####

# Importing the PDF read AND write libraries
from PyPDF2 import PdfReader, PdfWriter

# Defining a function to reomve the password from#the PDF taking 3 parameters
def removePDFpassword(input, output, passwd):
    reader = PdfReader(input)
    reader.decrypt(passwd)

    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        writer.add_page(page)

    with open(output, 'wb') as HalabesaElbesa:
        writer.write(HalabesaElbesa)
    print(f"Password removed. New file saved as {outputPdfPath}")

inputPdfPath = 'C:\\Users\\Assem Mahmoud\\Desktop\\removePDFpassword\\08099600195713508954227775638.pdf'
outputPdfPath = 'C:\\Users\\Assem Mahmoud\\Desktop\\removePDFpassword\\ba7rMesa3lekyaHaram.pdf'
password = '1985*0212#'
removePDFpassword(inputPdfPath, outputPdfPath, password)
