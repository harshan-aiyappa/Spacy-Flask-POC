from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import WordNetError


def get_synonyms_and_antonyms(word, lang='por'):
    synonyms = set()
    antonyms = set()

    try:
        synsets = wordnet.synsets(word, lang=lang)
        for synset in synsets:
            for lemma in synset.lemmas(lang=lang):
                synonyms.add(lemma.name())

                # Retrieve antonyms
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())
    except WordNetError:
        pass

    return list(synonyms), list(antonyms)


# Example usage
is_word = "carro"
synonyms_list, antonyms_list = get_synonyms_and_antonyms(is_word)

print("Synonyms of", is_word, "are:", synonyms_list)
print("Antonyms of", is_word, "are:", antonyms_list)


# limitations :

# The wordnet module in NLTK supports multiple languages, and you can specify the language using the lang parameter. However, the availability and coverage of WordNet data vary across languages. Some of the supported languages include:

# https://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html#Synset

# English: 'eng' (default, so you don't need to explicitly specify it)
# Sure, here's a list of some languages supported by the NLTK WordNet module along with their language codes:

# - English: 'eng' (default)
# - Spanish: 'spa'
# - Portuguese: 'por'
# - French: 'fra'
# - Italian: 'ita'
# - German: 'deu'
# - Dutch: 'nld'
# - Russian: 'rus'
# - Japanese: 'jpn'
# - Persian: 'fas'
# - Norwegian (Nynorsk): 'nno'
# - Norwegian (Bokmål): 'nob'

# This is not an exhaustive list, and there may be additional languages supported by NLTK WordNet. If you have a specific language in mind or want more details, feel free to let me know!
