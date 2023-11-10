from translate import Translator
translator = Translator(from_lang='pt', to_lang='en')
translation = translator.translate("Eu dirijo o carro.")
print(translation)
