"""App module"""

from textblob import TextBlob

def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contains_words(word, text):
    
    return word in text

