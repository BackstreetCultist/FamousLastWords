import random 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

imageID = random.randint(0, 16)
background = Image.open("famous/background.png")
image = Image.open('famous/image'+str(imageID)+'.png')
background.paste(image, (0, 300), image)
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 100)
draw = ImageDraw.Draw(background)
draw.text((0, 0),"Propaganda",(0,0,80),font=font)
background.show()