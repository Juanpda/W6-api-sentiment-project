import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()


def text_tokenizer(text):
    tokens = nlp(text)
    tokenized_text = []
    for token in tokens:
        if not token.is_stop:
            lemma = token.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma):
                tokenized_text.append(lemma)
    tokenized_text = " ".join(tokenized_text)
    return tokenized_text
    


def sentiment_calculator(text):
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(text)
    pol = polaridad["compound"]
    return pol



