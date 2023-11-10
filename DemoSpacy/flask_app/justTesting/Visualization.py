import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

about_interest_text = (
    "Harshan, a coding maestro immersed in the dynamic realm of Python development within a cutting-edge London-based Fintech enterprise, sets his sights on mastering the intricacies of Natural Language Processing."
)
about_interest_doc = nlp(about_interest_text)
displacy.serve(about_interest_doc, style="dep")
