from PIL import Image

img = Image.open("Pictures/girl.jpg")
imgCrop = img.crop(box=(50,50,200,500))
imgCrop.show()