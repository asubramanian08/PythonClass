# Generate a 2048 tile using Python's PIL package

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SIZES = [200, 150, 110, 85]

def digitCount(x):
    digits = 1
    while x // 10 > 0:
        x //= 10
        digits += 1
    return digits

def createTile(number, color, file):
   
    # Create the background
    width = 200
    height = 200
    img = Image.new('HSV', (width, height), color) # 'RGB'
    draw = ImageDraw.Draw(img)

    # Add and center text
    text = str(number)
    font = ImageFont.truetype("Arial.ttf", SIZES[digitCount(number) - 1])

    temp1, temp2, w, h = draw.textbbox((0, 0), text, font=font)
    x = (width - (w + temp1)) // 2
    y = (height - (h + temp2)) // 2
    draw.text((x, y), text, fill=(0,0,0), font=font)

    # Save the image
    img.save(file)


# Idea for changing colors
# 1. You have a set "step length" of distance away from the previous hue and saturation
# 2. Saturation jump will start at 10 and decrease by .5 every time
# 3. The hue will be such that the distance is 10: hue = sqrt(10^2 - saturation^2)

# HSV -> RGB

x = 2 
while x <= 2048:
    H = 66
    S = 40
    V= 100
    HD = 2
    VD = 10
    while VD > 0 and HD > 0:
        VD = VD - 0.5
        HD = HD + 1


    createTile(x, (255, 255, 0), f'img/{x}.png')
    x *= 2