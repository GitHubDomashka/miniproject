
import PyPDF2
pl = open('b.pdf', 'rb')
plread = PyPDF2.PdfFileReader(pl)
getpage = plread.getPage(0)
text = getpage.extractText()