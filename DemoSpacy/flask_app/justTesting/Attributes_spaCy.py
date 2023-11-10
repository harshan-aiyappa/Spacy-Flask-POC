import spacy

nlp = spacy.load("en_core_web_sm")
about_text = "Harshan, a coding maestro immersed in the dynamic realm of Python development within a cutting-edge London-based Fintech enterprise, sets his sights on mastering the intricacies of Natural Language Processing."

about_doc = nlp(about_text)

print(
    f"{'Text with Whitespace':22}"
    f"{'Is Alphanumeric?':15}"
    f"{'Is Punctuation?':18}"
    f"{'Is Stop Word?'}"
)


for token in about_doc:
    print(
        f"{str(token.text_with_ws):22}"
        f"{str(token.is_alpha):15}"
        f"{str(token.is_punct):18}"
        f"{str(token.is_stop)}"
    )
