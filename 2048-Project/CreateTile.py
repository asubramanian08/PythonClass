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

    temp1, temp2, w, h = draw.textbbox((0, 0), text, font=font)
    x = (width - (w + temp1)) // 2
    y = (height - (h + temp2)) // 2
    draw.text((x, y), text, fill=(0,0,0), font=font)

    # Save the image
    img.save(file)


# Idea for changing colors
# 1. You have a set "step length" of distance away from the previous hue and saturation
# 2. Saturation will start at 10 and decrease by .5 every time
# 3. The hue will be such that the distance is 10: hue = sqrt(10^2 - value^2)

x = 2
while x <= 2048:
    createTile(x, (255, 255, 0), f'img/{x}.png')
    x *= 2