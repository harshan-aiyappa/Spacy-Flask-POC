from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == "__main__":
    input_text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'fr' for French): ")

    translated_text = translate_text(input_text, target_language)
    print(f"Translated text: {translated_text}")

