###### Best PDF password remover EVER!!!!!!! ######
###### Path, output path, and the password ######

# Importing the PDF read AND write libraries
from PyPDF2 import PdfReader, PdfWriter

# Defining a function to remove the password from the PDF taking 3 parameters
def removePDFpassword(input_path, output_path, passwd):
    try:
        print(f"Input Path: {input_path}")
        print(f"Output Path: {output_path}")
        print(f"Password: {passwd}")
        
        reader = PdfReader(input_path)
        reader.decrypt(passwd)

        writer = PdfWriter()
        for pageNum in range(len(reader.pages)):
            page = reader.pages[pageNum]
            writer.add_page(page)

        with open(output_path, 'wb') as HalabesaElbesa:
            writer.write(HalabesaElbesa)
        print(f"Password removed. New file saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Take user input for file paths and password with custom prompts
input_pdf_path = input("Give me the file Path ya3am el7aaaaaaaag:- ")
output_pdf_path = input("Give me the output file Path ya3am el7aaaaaaaag:- ")
password = input("Give me the PDF password ya3am el7aaaaaaaag:- ")

# Call the function with the user-provided input
removePDFpassword(input_pdf_path, output_pdf_path, password)
