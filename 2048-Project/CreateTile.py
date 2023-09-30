# Generate a 2048 tile using Py2thon's PIL package

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def createTile(number, color, file):
   
    # Create the background
    width = 200
    height = 200
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)

    # Add and center text
    text = str(number)
    font = ImageFont.truetype("Arial.ttf", 200)
    _, _, w, h = draw.textbbox((0, 0), text, font=font)
    x = (width - w) / 2
    y = (height - h) / 2
    draw.text((x, y), text, fill=(0,0,0), font=font)

    # Save the image
    img.save(file)

createTile(2, (255, 255, 0), 'img/2.png')