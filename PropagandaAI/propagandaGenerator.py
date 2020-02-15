import random 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

imageID = random.randint(0, 10)
background = Image.open("test.png")
image = Image.open("monkey.png")
background.paste(image, (0, 0), image)
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 500)
draw = ImageDraw.Draw(background)
draw.text((0, 0),"Propaganda",(240,10,10),font=font)
background.show()