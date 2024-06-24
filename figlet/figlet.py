import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 1 :
    font = figlet.getFonts() #font is returned as a list
    font = random.choice(font)

elif len(sys.argv)==3 and (sys.argv[1] == "-f" or sys.argv[1]== "--font") :

    if sys.argv[2] in fonts:
       font = sys.argv[2]
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')

figlet.setFont(font=font)
s = input("Input: ")
print(figlet.renderText(s))