import PyPDF2

#input the file path for the pdf you wish to extract pages from
#this will open the pdf file in binary mode
input_file = open(r"C:\Users\IanRitchie\Downloads\gtm 1.13.pdf","rb")

#input the file path for the pdf you wish to save the extracted pages to
#this will open the new pdf file in binary mode
output_file = open(rb"C:\Users\IanRitchie\Downloads\output_file.pdf", 'wb')


#enter the page numbers that you would like to extract from the pdf
pages_to_extract = [5, 9, 14, 16, 26, 28, 32, 34, 45, 46, 62 63]
#this allows us to read the input file and access the pages and data
reader = PyPDF2.PdfReader(input_file)

#this allows us to add pages to the output file
writer = PyPDF2.PdfWriter()

#loops through the pages to extract list, adjusts for python indexing, and adds pages to output
for page_num in pages_to_extract:
    page_index = page_num - 1  #adjust for python indexing
    writer.add_page(reader.pages[page_index])

writer.write(output_file)

input_file.close()
output_file.close()
print("Pages extracted and saved to output_file.pdf")