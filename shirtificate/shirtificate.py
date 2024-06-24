from fpdf import FPDF
# The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.


class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', size=44)
        #assign width = 0 to get width to be full page width and align 'C'
        self.cell(w=0,txt='CS50 Shirtificate', border=False, align='C')
        #Line break for spacing
        self.ln(30)



#The format of the PDF should be A4, which is 210mm wide by 297mm tall.
#create FPDF object
#layout 'P' or 'L'
#Unit ('mm','cm','in')
#format('A3', 'A4'(default),'A5', 'Letter', 'Legal', (100,50)#custom size width,height)

pdf = PDF(orientation='P',format = 'A4', unit='mm')

#automatically add new pages when text reaches how close u specified to the margin
pdf.set_auto_page_break(auto=False, margin=0)

pdf.add_page()
pdf.set_margin(10)
#set 'image.png', x, y, w, h
#if only set the width then height will be changed proportionally
pdf.image('shirtificate.png', w = pdf.epw)


line_height = 10
#fonts = 'times', courier, helvetica, symbol, zpfdingbats
#'B' (bold), 'U' underline, "I', (italics), '' (regular), combinations ('BU')
pdf.set_font('helvetica', 'B', size =28)

#either in R,G,B 0-255 or grayscale 0-255
pdf.set_text_color(255)
#Add text
#w = width for cell, #h = height for cell if width = 0, it's the width of entire PDF
#ln=True - moves cursor down to next line
#border (0 False; 1 True - add border around cell)

#set y cursor to 80 mm from the top margin
pdf.set_y(80)

#get width of text string
txtstring =  input('Name: ')
txt_width = pdf.get_string_width(txtstring)
docwidth = pdf.w
docheight = pdf.h
#set x cursor to start writing the string so that it is centered and has equal blank space on either side
pdf.set_x((docwidth - txt_width)/2)
#print(txt_width)
#print(docwidth, docheight, sep="     ")


pdf.text(txt=f"{txtstring} took CS50", x = 60,  y=120)
pdf.output('shirtificate.pdf')


