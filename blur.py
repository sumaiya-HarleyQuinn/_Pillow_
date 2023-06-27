from PIL import Image, ImageFilter

im = Image.open("Pictures/girl.jpg")
im.filter(ImageFilter.EMBOSS).show()   #blur conteur