from PIL import Image
filen = "Pictures/car.jpg"
img = Image.open(filen)

img = img.rotate(angle=70, expand=True, fillcolor="gray")      #angle=90, expand=True

img.show()