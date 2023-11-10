import nltk
from nltk.corpus import wordnet


synonyms = set()

is_word = "big"
for syn in wordnet.synsets(is_word):
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

synonyms_list = list(synonyms)
print("synonyms of ", is_word, " is :", synonyms_list)

antonyms = set()

for syn in wordnet.synsets(is_word):
    for i in syn.lemmas():
        if i.antonyms():
            antonyms.add(i.antonyms()[0].name())

antonyms_list = list(antonyms)

print("antonyms of ", is_word, " is :", antonyms_list)


# LIMITATIONS : 
# Only English words can be achieved with nltk (wordnet)
