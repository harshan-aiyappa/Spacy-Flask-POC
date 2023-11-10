import spacy

nlp = spacy.load("en_core_web_sm")
about_text = (
    "Harshan, a coding maestro immersed in the dynamic realm of Python development within a cutting-edge London-based Fintech enterprise, sets his sights on mastering the intricacies of Natural Language Processing."
)

about_doc = nlp(about_text)

for token in about_doc:
    print(token, token.idx)
