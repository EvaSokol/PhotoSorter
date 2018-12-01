import PyPDF2
from PyPDF2 import PdfFileReader

file_name = 'm:\Projects\PhotoSorter\\files\price.pdf'


def run():
        # creating a pdf file object
        pdfFileObj = open(file_name, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print('total %s pages' % pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()

if __name__ == '__main__':
    run()

