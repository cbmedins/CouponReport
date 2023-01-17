from logging import root
import os
from tkinter import filedialog
import PyPDF2

root.directory = filedialog.askdirectory()

route = root.directory+'/'
#print(route)
coupons = os.listdir(route)

for coupons in coupons:
    pdfFileObject = open(route+coupons, 'rb')
    pdfReader     = PyPDF2.PdfReader(pdfFileObject)
    pageObject    = pdfReader.pages[0]
    text          = pageObject.extract_text()
    lines         = text.splitlines()
    numLines      = len(lines)
    startLine     = None
    endLine       = None 
    lineRange     = []

    for lineIndex in range(numLines):
        currentLine  = lines[lineIndex]
        search       = 'NOMBRE PESO (KG)'
        endSearch    = 'TOTAL PESO CARGA'
        if search == currentLine:   
            if startLine is None:
                startLine = lineIndex + 1              
        
        if endSearch in currentLine:
            if endLine is None:
                endLine = lineIndex

#    if startLine is not None and endLine is not None:
#        print("El rango de líneas que contienen el parametro {} en la pagina {} es de {} a {}".format(search, coupons, startLine, endLine))

    for lineView in range(startLine,endLine):
        currentLine = lines[lineView]
        #print("Linea {} del documento {}: {}".format(lineView, coupons, currentLine))
        lineRange.append("Nombre del documento: {}, Carga: {}".format(coupons, currentLine))

    with open('lineRange.txt','a') as file:
        file.writelines('%s\n' % line for line in lineRange)

    with open("lineRange.txt", "r") as file:
        print(file.read())
        