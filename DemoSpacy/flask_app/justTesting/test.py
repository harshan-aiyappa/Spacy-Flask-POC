import spacy
# nlp = spacy.load("en_core_web_trf")

# nlp = spacy.load("pt_core_news_lg")

nlp = spacy.load("es_dep_news_trf")

text = "cómo estás"
doc = nlp(text)
pos_tags = [{'text': token.text, 'pos': token.pos_, "posExplain": spacy.explain(token.pos_), 'tagger': token.tag_, "taggerExplain": spacy.explain(token.tag_)}
            for token in doc]
print(doc, pos_tags)
