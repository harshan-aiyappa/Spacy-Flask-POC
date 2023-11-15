from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
from translate import Translator
from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import WordNetError

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

# language mapping for different ISO language Codes
# from language_mapping import map_iso_639_1_to_nltk_corpus


language_mapping_for_translation = {
    'en': 'english',
    'es': 'spanish',
    'pt': 'portuguese',
    'hi': 'hindi',
    'kn': 'kannada',
    # Add more mappings as needed
}


app = Flask(__name__)
# translator = Translator()
CORS(app)  # Enable CORS for your app

# Load the spaCy model for English
# nlp = spacy.load("en_core_web_sm")


# Load the Portuguese model
# nlp = spacy.load("pt_core_news_sm")


# Load the Spanish model
# nlp = spacy.load('es_core_news_sm')

nlp_en = spacy.load("en_core_web_trf")
nlp_pt = spacy.load("pt_core_news_lg")
nlp_es = spacy.load("es_dep_news_trf")

# Function to load spaCy model based on language

# used_languages = ["en", "es", "pt"]


def load_spacy_model(language, text):
    if language == "en":
        print("English Loaded")
        return nlp_en(text)
    elif language == "pt":
        print("Portuguese Loaded")
        return nlp_pt(text)
    elif language == "es":
        print("Spanish Loaded")
        return nlp_es(text)
    else:
        raise ValueError("Unsupported language")




@app.route('/')
def hello_world():
    return 'Hello, World!'

def normalize_language(language):
    # Normalize the target language to accept either ISO code or full abbreviation
    return language_mapping_for_translation.get(language.lower(), language.lower())

@app.route('/api/data', methods=['GET'])
def get_json_data():
    data = {
        'message': 'Hello, World!',
        'value': 42,
        'items': ['item1', 'item2', 'item3']
    }
    return jsonify(data)


@app.route('/tokenize', methods=['POST'])
def tokenize_text():
    data = request.get_json()
    text = data['text']
    lng = data['lng']
    doc = load_spacy_model(lng, text)
    tokens = [token.text for token in doc]
    return jsonify(tokens)


@app.route('/ner', methods=['POST'])
def named_entity_recognition():
    data = request.get_json()
    text = data['text']
    lng = data['lng']
    doc = load_spacy_model(lng, text)
    entities = [{'text': ent.text, 'label': spacy.explain(ent.label_)}
                for ent in doc.ents]
    return jsonify(entities)


@app.route('/pos', methods=['POST'])
def pos_tagging():
    data = request.get_json()
    text = data['text']
    lng = data['lng']
    doc = load_spacy_model(lng, text)
    pos_tags = [{'text': token.text, 'pos': token.pos_, "posExplain": spacy.explain(token.pos_), 'tagger': token.tag_, "taggerExplain": spacy.explain(token.tag_)}
                for token in doc]
    print(pos_tags)
    return jsonify(pos_tags)


@app.route('/dependency', methods=['POST'])
def dependency_parsing():
    data = request.get_json()
    text = data['text']
    lng = data['lng']
    doc = load_spacy_model(lng, text)
    dependencies = [{'text': token.text,
                     'dep': spacy.explain(token.dep_)} for token in doc]
    return jsonify(dependencies)


@app.route('/lemmatize', methods=['POST'])
def lemmatization():
    data = request.get_json()
    text = data['text']
    lng = data['lng']
    doc = load_spacy_model(lng, text)
    lemmas = [{'text': token.text, 'lemma': token.lemma_} for token in doc]
    return jsonify(lemmas)


@app.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing 'text' field in request data"}), 400

    text = data['text']
    lng = data['lng']
    doc = load_spacy_model(lng, text)

    token_attributes = []
    for token in doc:
        token_data = {
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "tag": token.tag_,
            "dep": token.dep_,
            "shape": token.shape_,
            "is_alpha": token.is_alpha,
            "is_stop": token.is_stop,
            "is_punct": token.is_punct,
            "is_space": token.is_space,
            "is_digit": token.is_digit,
            "is_lower": token.is_lower,
            "is_upper": token.is_upper,
            "is_title": token.is_title,
            "like_num": token.like_num,
            "is_currency": token.is_currency,
        }
        token_attributes.append(token_data)

    return jsonify({"tokens": token_attributes})


def detect_language(text):
    detected_language = detect(text)
    print(f'Detected language: {detected_language}')
    return detected_language

# translator Translator
@app.route('/translate/translator', methods=['POST'])
def translate_text():
    data = request.get_json()

    if 'text' not in data or 'to_lang' not in data:
        return jsonify({'error': 'Missing required parameters'}), 400

    text = data['text']
    from_lang = data['from_lang']
    to_lang = data['to_lang']

    try:
        # Detect source language dynamically
        # detected_language = detect_language(text)
        # print(f'Source language: {detected_language}')

        # Translate the text
        translator = Translator(from_lang=from_lang, to_lang=to_lang)
        translated_text = translator.translate(text)
        print(f'Translated text: {translated_text}')

        result = {
            'original_text': text,
            'from_lang': from_lang,
            'translated_text': translated_text,
            'to_lang': to_lang
        }

        return jsonify(result)

    except Exception as e:
        print(f'Error: {str(e)}')
        return jsonify({'error': str(e)}), 500


# MyMemory Translator
@app.route('/translate/mymemory', methods=['POST'])
def translate_mymemory():
    try:
        data = request.get_json()
        text_to_translate = data['text']
        target_language = normalize_language(data['target_language'])

        translated_text = MyMemoryTranslator(source='english', target=target_language).translate(text_to_translate)

        response = {
            'input_text': text_to_translate,
            'translated_text': translated_text,
            'target_language': target_language
        }

        return jsonify(response)

    except Exception as e:
        error_response = {
            'error': str(e)
        }
        return jsonify(error_response), 500
    

# Google Translator
@app.route('/translate/google', methods=['POST'])
def translate_google():
    try:
        data = request.get_json()
        text_to_translate = data['text']
        target_language = normalize_language(data['target_language'])

        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text_to_translate)

        response = {
            'input_text': text_to_translate,
            'translated_text': translated_text,
            'target_language': target_language
        }

        return jsonify(response)

    except Exception as e:
        error_response = {
            'error': str(e)
        }
        return jsonify(error_response), 500

# Pons Translator
@app.route('/translate/pons', methods=['POST'])
def translate_pons():
    try:
        data = request.get_json()
        text_to_translate = data['text']
        target_language = normalize_language(data['target_language'])

        translator = PonsTranslator(source='english', target=target_language)
        translated_text = translator.translate(text_to_translate)

        # Check if the translation is successful
        if translated_text:
            response = {
                'input_text': text_to_translate,
                'translated_text': translated_text,
                'target_language': target_language
            }
            return jsonify(response)
        else:
            raise Exception("Translation failed. Empty response from PonsTranslator.")

    except Exception as e:
        error_response = {
            'error': str(e)
        }
        print(f"Error in translate_pons: {e}")
        return jsonify(error_response), 500

# Linguee Translator
@app.route('/translate/linguee', methods=['POST'])
def translate_linguee():
    try:
        data = request.get_json()
        
        text_to_translate = data['text']
        target_language = normalize_language(data['target_language'])

        translated_text = LingueeTranslator(source='english', target=target_language).translate(text_to_translate)

        response = {
            'input_text': text_to_translate,
            'translated_text': translated_text,
            'target_language': target_language
        }

        return jsonify(response)

    except Exception as e:
        error_response = {
            'error': str(e)
        }
        return jsonify(error_response), 500
    
def get_synonyms_and_antonyms(word, lang='eng'):
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


@app.route('/synonyms_antonyms', methods=['POST'])
def synonyms_antonyms():
    data = request.json
    print(data)
    word = data.get('word')

    # Default to English if lang parameter is not provided
    lang = map_iso_639_1_to_nltk_corpus(data.get('lang', 'en'))

    if not word:
        return jsonify({'error': 'Word parameter is missing'}), 400

    synonyms, antonyms = get_synonyms_and_antonyms(word, lang)
    result = {'word': word, 'synonyms': synonyms, 'antonyms': antonyms}

    return jsonify(result)


@app.route('/get_token_info', methods=['POST'])
def get_token_info():
    # Get the sentence and language from the POST request data
    data = request.get_json()
    
    text = data.get('sentence')
    lang = data.get('lang', 'en')
    print("get_token_info :",text,lang)
    # Load the appropriate spaCy model based on the language
    if lang == "en":
        nlp_model = nlp_en
    elif lang == "pt":
        nlp_model = nlp_pt
    elif lang == "es":
        nlp_model = nlp_es
    else:
        return jsonify({'error': 'Unsupported language'}), 400

    # Process the sentence using spaCy
    doc = nlp_model(text)

    # Calculate the similarity to a specific token dynamically
    target_token = 'processing'
    target_token_similarity = doc[0].similarity(nlp_model.vocab[target_token])

    token_info_list = []

    for token in doc:
        token_info = {
            "Token": token.text,
            "Lemma": token.lemma_,
            "DependencyParsing": {
                "Dependency": token.dep_,
                "HeadText": token.head.text
            },
            "NER": {
                "EntityType": token.ent_type_,
                "IOBCode": token.ent_iob_
            },
            "SimilarityToProcessing": target_token_similarity,
            "WordShape": token.shape_,
            "IsStopWord": token.is_stop,
            "IsPunctuation": token.is_punct,
            "IsSpace": token.is_space,
            "IsNumeric": token.is_digit,
            "SentenceIndex": token.sent.start,
            "PositionInSentence": token.i
        }
        token_info_list.append(token_info)

    return jsonify(token_info_list)


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'message': error.description}), 400


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error', 'message': 'Something went wrong on the server'}), 500


def map_iso_639_1_to_nltk_corpus(iso_639_1_code):
    # Define the mapping dictionaries
    iso_639_1_codes_to_names = {
        'en': 'English',
        'es': 'Spanish',
        'pt': 'Portuguese',
        'fr': 'French',
        'it': 'Italian',
        'de': 'German',
        'nl': 'Dutch',
        'ru': 'Russian',
        'ja': 'Japanese',
        'fa': 'Persian',
        'nn': 'Norwegian (Nynorsk)',
        'nb': 'Norwegian (Bokmål)',
    }

    nltk_corpus_codes = {
        'English': 'eng',
        'Spanish': 'spa',
        'Portuguese': 'por',
        'French': 'fra',
        'Italian': 'ita',
        'German': 'deu',
        'Dutch': 'nld',
        'Russian': 'rus',
        'Japanese': 'jpn',
        'Persian': 'fas',
        'Norwegian (Nynorsk)': 'nno',
        'Norwegian (Bokmål)': 'nob',
    }

    # Map ISO 639-1 code to NLTK corpus code
    language_name = iso_639_1_codes_to_names.get(iso_639_1_code)
    nltk_corpus_code = nltk_corpus_codes.get(language_name)

    return nltk_corpus_code


if __name__ == '__main__':
    app.run(debug=True)
