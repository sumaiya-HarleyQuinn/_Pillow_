from PIL import Image

filen = "Pictures/c1.jpg"
im = Image.open(filen)

print(im.size, im.format, im.mode, im.info)

im.save("car-new.png", "PNG")
im.show()