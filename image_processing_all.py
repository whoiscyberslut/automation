# The script uses the Python Imaging Library (PIL) module to open and process the images. It performs operations such as
# resizing, applying filters (in this case, converting to grayscale), and creating thumbnails. The processed images are
# saved in the specified output directory. Additionally, the script generates a collage from the thumbnail images and
# saves it as "collage.jpg" in the output directory.

import os
from PIL import Image

image_directory = "/Users/zvezdochka/Downloads/wetransfer_nia002-jpg_2022-09-09_1709/"
output_directory = "/Users/zvezdochka/Downloads/wetransfer_nia002-jpg_2022-09-09_1709/"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Process each image file in the directory
for filename in os.listdir(image_directory):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(image_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Open the image using PIL
        image = Image.open(image_path)

        # Resize the image
        resized_image = image.resize((800, 600))

        # Apply image filters (example: convert to grayscale)
        filtered_image = resized_image.convert("L")

        # Create a thumbnail version of the image
        thumbnail_image = resized_image.copy()
        thumbnail_image.thumbnail((100, 100))

        # Save the processed images
        resized_image.save(output_path)
        filtered_image.save(output_path.replace(".", "_filtered."))
        thumbnail_image.save(output_path.replace(".", "_thumbnail."))

# Generate a collage from multiple images
collage_images = []
for filename in os.listdir(output_directory):
    if filename.endswith("_thumbnail.jpg"):
        image_path = os.path.join(output_directory, filename)
        image = Image.open(image_path)
        collage_images.append(image)

if collage_images:
    collage_width = 400
    collage_height = 400
    collage = Image.new("RGB", (collage_width, collage_height))
    x_offset = 0
    y_offset = 0

    for image in collage_images:
        collage.paste(image, (x_offset, y_offset))
        x_offset += image.width

    collage.save(os.path.join(output_directory, "collage.jpg"))
