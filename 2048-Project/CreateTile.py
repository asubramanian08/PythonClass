# Generate a 2048 tile using Py2thon's PIL package

import PIL

def createTile(number, color, file):

    # Create the image
    width = 200
    hight = 200
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("sans-serif.ttf", 46)
    draw.text((x, y), "" + number + "",(r,g,b), font = font)

    # Save the image
    img.save(file)

# To create a square image with the specified color and the number (in the center).
# Save the image in the given file
# createTile(2, "FFFF00", 'img/2.png')