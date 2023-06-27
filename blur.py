from PIL import Image, ImageFilter

im = Image.open("Pictures/girl.jpg")
im.filter(ImageFilter.DETAIL).show()   #blur conteur boxblur(3/5/10) edge_enhance smooth sharpen detail