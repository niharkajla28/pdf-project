import PyPDF2

if __name__ == '__main__':
    template = PyPDF2.PdfFileReader(open('new_merger.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()

    for item in range(template.getNumPages()):
        page = template.getPage(item)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open('New_merged_file_output1.pdf', 'wb') as file:
        output.write(file)
        print('File is written')