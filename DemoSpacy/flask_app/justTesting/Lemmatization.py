import spacy
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "Harshan, a coding maestro immersed in the dynamic realm of Python development within a cutting-edge London-based Fintech enterprise, sets his sights on mastering the intricacies of Natural Language Processing."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
