import markovify
import random 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

numberOfWords = 30
numberOfSentences = 10
numberOfGoodSentences = 0

slogans = [['' for x in  range(numberOfWords)] for y in range(numberOfSentences)]

def Original(slogan):
    current = slogan.split(" ")
    for i in slogans:
        counter = 0
        for j in i:
            for k in current:
                if k == j:
                    counter += 1
            if counter > len(current)/2:
                return False
    return True

# Get raw text as string.
with open("propaganda.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)


# Print five randomly-generated sentences
while (numberOfGoodSentences < numberOfSentences):
    slogan = str(text_model.make_sentence())
    if slogan != "None" and Original(slogan):
        slogans[numberOfGoodSentences] = slogan.split(" ")
        numberOfGoodSentences += 1

slogans = list(map(lambda x: " ".join(x), slogans))

imageID = random.randint(0, 16)
background = Image.open("famous/background.png")
image = Image.open('famous/image'+str(imageID)+'.png')
background.paste(image, (0, 300), image)
font = ImageFont.truetype("/Library/Fonts/Impact.ttf", 100)
draw = ImageDraw.Draw(background)
draw.text((10, 0),slogans[0],(0,0,80),font=font)
background.show()