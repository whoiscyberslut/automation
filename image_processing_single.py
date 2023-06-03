# Develop a script that processes a directory of images. The script should perform various operations on the images,
# such as resizing, cropping, applying filters, or converting file formats. It could also generate image thumbnails or
# create collages from multiple images.

import os
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

directory = '/Users/zvezdochka/Downloads/wetransfer_nia002-jpg_2022-09-09_1709/'
os.chdir(directory)

filepath = "mouse_in_snake.jpg"
img = Image.open(filepath)

# Rezising image

def resize(image, width, height):
    image = Image.open(image)
    new_image = image.resize((width, height))
    new_image.save('image_{}'.format(width) + '.jpg')

resize(filepath, 400, 400)

# Cropping image 

def crop(image, left, top, right, bottom):
    iml = img.crop((left, top, right, bottom))
    iml.show()
    iml.save('cropped_{}'.format(filepath) +'.jpg')

crop(filepath, 155, 65, 360, 270)

# Applying various filters 

def apply_filter(image, filter):
    img1 = img.filter(filter)
    img1.save('ImageFilter_{}'.format(image) + '.jpg')
    img1.show()

apply_filter(filepath, CONTOUR)

# Converting from .jpg to specified file format 

def converter(image, format):
    try:
        image = Image.open(image)
        image.save("converted-png-image.{}".format(format))
        print("Image successfully converted!")

    except FileNotFoundError:
        print("Couldn't find the provided image")

converter(filepath, "jpeg")
converter(filepath, "png")

# Generating image thumbnails

def tnails(t1, t2):
   try:
      img = Image.open(filepath)
      img.thumbnail((t1,t2))
      img.save('thumbnail.jpg')
      image1 = Image.open('thumbnail.jpg')
      image1.show()
   except IOError:
      pass

tnails(100, 250)

# Creating a collage from multiple images 

def collage_maker():
    image1 = Image.open("nia002.jpg")
    image1 = image1.resize((500, 500))
    image2 = Image.open("nia003.jpg")
    image2 = image2.resize((500, 500))
    image3 = Image.open("nia004.jpg")
    image3 = image3.resize((500, 500))
    image4 = Image.open("nia005.jpg")
    image4 = image4.resize((500, 500))
    image5 = Image.open("nia006.jpg")
    image5 = image5.resize((500, 500))

    # Creating an image which enables users to paste the images
    collage = Image.new("RGBA", (1500, 1500), color="black")
    collage.paste(image1, (0, 0))
    collage.paste(image3, (1000, 0))
    collage.paste(image2, (500, 500))
    collage.paste(image4, (0, 1000))
    collage.paste(image5, (1000, 1000))

    # Saving the newly generated collage image
    collage.save("Photo_Collage.png")

collage_maker()
