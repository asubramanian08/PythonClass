# Generate a 2048 tile using Python's PIL package

# Important image generation library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Hardcode font sizes
SIZES = [200, 150, 110, 85]


def digitCount(x):  # Count digits -> used to pick the font size
    digits = 1
    while x // 10 > 0:
        x //= 10
        digits += 1
    return digits


def createTile(number, color):  # Create a tile

    # Create the background
    width = 200
    height = 200
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)

    # Add and center text
    text = str(number)
    font = ImageFont.truetype("Arial.ttf", SIZES[digitCount(number) - 1])

    temp1, temp2, w, h = draw.textbbox((0, 0), text, font=font)
    x = (width - (w + temp1)) // 2
    y = (height - (h + temp2)) // 2
    draw.text((x, y), text, fill=(0, 0, 0), font=font)

    # Save the image
    img.save(f'img/{number}.png')


# Create all tiles: 2 through 2048 with handpicked RGB colors
createTile(2, (250, 249, 234))
createTile(4, (206, 209, 188))
createTile(8, (220, 216, 128))
createTile(16, (227, 196, 90))
createTile(32, (227, 151, 46))
createTile(64, (229, 106, 23))
createTile(128, (241, 74, 18))
createTile(256, (248, 43, 8))
createTile(512, (255, 0, 60))
createTile(1024, (255, 0, 93))
createTile(2048, (241, 2, 118))
