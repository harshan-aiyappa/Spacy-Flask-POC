import nltk

# Download the necessary resource for nltk
nltk.download('cmudict')
nltk.download('punkt')



def count_syllables(word):
    vowels = "aeiouy"
    word = word.lower()
    count = 0

    if word[0] in vowels:
        count += 1

    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1

    if word.endswith("e"):
        count -= 1

    if count == 0:
        count = 1

    return count


def extract_syllables(sentence):
    words = nltk.word_tokenize(sentence)
    syllables_per_word = [count_syllables(word) for word in words]
    return syllables_per_word


# Example usage
sentence = "NLTK is a powerful tool for natural language processing."
syllables = extract_syllables(sentence)
print(f"Syllables per word: {syllables}")
