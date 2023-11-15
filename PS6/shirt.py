import sys
from PIL import Image, ImageOps

# sys.exit
# if the user does not specify exactly two command-line arguments
if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
if len(sys.argv) > 4:
    print("Too many command-line arguments")
    sys.exit(1)

inputfile_name = sys.argv[1]
outputfile_name = sys.argv[2]

# if the inut's and output's names do not end in .jpg, .jpeg, or .png
name, extension = inputfile_name.split(".")
if extension not in ["jpg", "jpeg", "png"]:
    print("Invalid input")
    sys.exit(1)

# if the input's name does not have the same extension as the output's name
name2, extension2 = outputfile_name.split(".")
if extension != extension2:
    print("Input and output have different extensions")
    sys.exit(1)

shirt = Image.open("shirt.png")
size = shirt.size
# print(size)

# open the input with image.open
# if the specified input does not exist
try:
    portrait = Image.open(inputfile_name, mode='r', formats=None)
except FileNotFoundError:
    print("Invalid input")
    sys.exit(1)
# print(portrait.size)

# resize and crop the input with ImageOps.fit
crop_portrait = ImageOps.fit(portrait, size)
# print(crop_portrait.size)

# overlay the shirt with Image.paste
crop_portrait.paste(shirt, shirt)

# save the result with Image.save
crop_portrait.save(outputfile_name)