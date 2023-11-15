from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

# Use any translator you like, in this example GoogleTranslator
translated = MyMemoryTranslator(source='english', target='portuguese').translate("Good morning!")
translated2 = GoogleTranslator(source='auto', target='pt').translate(text="Good morning!") 

print(translated,translated2)


# Mapping between ISO codes and full language names
language_mapping = {
    'en': 'english',
    'es': 'spanish',
    'pt': 'portuguese',
    'hi': 'hindi',
    'kn': 'kannada',
    # Add more mappings as needed
}
def normalize_language(language):
    # Normalize the target language to accept either ISO code or full abbreviation
    return language_mapping.get(language.lower(), language.lower())

print(normalize_language("en"))
