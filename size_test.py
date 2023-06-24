from PIL import Image

filename = "Pictures/car.jpg"

img = Image.open(filename)
print(img.width, img.height)
img.show()

img = img.resize((int(img.width/2), int(img.height/2)), resample=Image.NEAREST)
print(img.width, img.height)
img.show()