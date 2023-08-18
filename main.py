"""

Project PDF_merge
Author: MC
Date: 2023-08-18

Main file of the project

"""

import PyPDF2
from os import listdir
from datetime import date

# output and input directory
IN_DIR = 'in_data'
OUT_DIR = 'out_data'

# file filter
FILE_FILTER = '.pdf'

# read all files in in_data dir
lidar = listdir(IN_DIR)

files_name = [match for match in lidar if FILE_FILTER in match.__str__().lower()]

# create pdf writer
pdf_writer = PyPDF2.PdfWriter()

print('------------------------------- READ INPUT FILES -------------------------------')

# main loop to read file from dir
for f in files_name:
    ff = IN_DIR + '/' + f
    print('------------------------------- FILE: ' + ff + ' -------------------------------')
    pdf = open(ff, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf)

    # loop to read pages from PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    pdf.close()

ff = OUT_DIR + '/' + 'all_' + date.today().__str__() + '.pdf'

print('------------------------------- WRITE OUTPUT FILE: ' + ff + ' -------------------------------')

# write out file
with open(ff, 'wb') as output:
    pdf_writer.write(output)

