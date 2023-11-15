import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

# get a list of available fonts
figlet.getFonts()

# expect zero or two command-line arguments

# zero if the user would like to output text in a random font
if len(sys.argv) == 1:
    randomfont = True
# two if the user would like to output text in a specific font
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or "--font"):
    randomfont = False
else:
    sys.exit("Invalid input")

if randomfont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid font")
else:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)

prompt = input("Input: ")

print("Output:")
print(figlet.renderText(prompt))