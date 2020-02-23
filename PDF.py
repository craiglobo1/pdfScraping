import fitz 
import PyPDF2 as p2

filename = 'Kinematics'
QN = 1
with open(filename + '.pdf','rb') as PDFtext:
    PDFpic = fitz.open(filename + '.pdf')
    PDFread = p2.PdfFileReader(PDFtext)
    page = len(PDFpic)

    for i in range(page):
        x = PDFread.getPage(i)
        data = x.extractText()
        print(data)
        for j,image in enumerate(PDFpic.getPageImageList(i)):
            
            '''
            data = data.replace('.','')
            if data[0] == 'Q':
                QN = ''
                for letter in data:
                    if letter == '\n':break
                    QN += letter
            '''           
            
            
            xref = image[0]
            pic= fitz.Pixmap(PDFpic,xref)
            finalPic = fitz.Pixmap(fitz.csRGB,pic)
            finalPic.writePNG('{}_{}.png'.format('Q'+ str(QN),j+1))
            pic= None
            finalPic = None
            QN+=1

