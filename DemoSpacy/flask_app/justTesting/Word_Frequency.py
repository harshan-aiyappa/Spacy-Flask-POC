import spacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")
complete_text = (
    "Harshan, a coding maestro immersed in the dynamic realm of Python development within a cutting-edge London-based Fintech enterprise, sets his sights on mastering the intricacies of Natural Language Processing."
)
complete_doc = nlp(complete_text)

words = [
    token.text
    for token in complete_doc
    if not token.is_stop and not token.is_punct
]

print(Counter(words).most_common(5))
