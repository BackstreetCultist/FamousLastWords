import markovify

numberOfWords = 30
numberOfSentences = 50
numberOfGoodSentences = 0

slogans = [['' for x in  range(numberOfWords)] for y in range(numberOfSentences)]

def Original(slogan):
    current = set(slogan.split(" "))
    for i in slogans:
        if len(current & set(i)) >= len(current):
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

for i in list(map(lambda x: " ".join(x), slogans)):
    print(i)