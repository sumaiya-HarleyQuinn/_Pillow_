from PIL import Image 
  
# creating a object 
image = Image.open("Pictures/c2.jpg")
area = (475, 175, 725, 350)
cropped = image.crop(area)
cropped.show()