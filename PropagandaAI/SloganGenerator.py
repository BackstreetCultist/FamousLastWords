import pandas as pd
from numpy.random import choice

def make_a_sentence(start):
    word= start
    sentence=[word]
    while len(sentence) < 30:
        next_word = choice(a = list(pivot_df.columns), p = (pivot_df.iloc[pivot_df.index ==word].fillna(0).values)[0])
        if next_word == 'EndWord':
                continue
        elif next_word in end_words:
            if len(sentence) > 2:    
                sentence.append(next_word)
                break
            else :
                continue
        else :
            sentence.append(next_word)
        word=next_word
    sentence = ' '.join(sentence)
    return sentence



#Creating words list
words = ["The", "text", "is", "everything.", "The", "propaganda", "machine", "is", "working.", "Humanity", "is", "lost."]

#Create a data frame to analyse word combinations
dict_df = pd.DataFrame(columns = ['lead', 'follow', 'freq'])
dict_df['lead'] = words
follow = words[1:]
follow.append('EndWord')

#Create an array of final words in strings
end_words = []
for word in words:
    if word[-1] in ['.','!','?'] and word != '.':
        end_words.append(word)
print(end_words)

#Count the occurence of each combination of lead and follow
dict_df['freq']= dict_df.groupby(by=['lead','follow'])['lead','follow'].transform('count').copy()

#Delete duplicate rows
dict_df = dict_df.drop_duplicates()

#Turn dict_df into matrix of every lead word as row-index and every follow word
#as column
pivot_df = dict_df.pivot(index = 'lead', columns= 'follow', values='freq')

#Assign probablities to follow words
sum_words = pivot_df.sum(axis=1)
pivot_df = pivot_df.apply(lambda x: x/sum_words)

sentence = make_a_sentence('The')
