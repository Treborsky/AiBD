"""Tests for the app module"""

import pytest
from app import extract_sentiment, text_contains_words

"""Test function written without the pytest functionality"""

def test_extract_sentiment():

    text = "I think today will be a great day"

    sentiment = extract_sentiment(text)

    assert sentiment > 0

"""Tests written using pytest functionalities"""

testdata = [("I think today will be a great day", True), ("I do not think this will turn out well", False)]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_extract_sentiment(sample, expected_output):

    sentiment = extract_sentiment(sample)

    assert (sentiment > 0) == expected_output

contains_words_testdata = [
        ('There is a duck in this text', 'duck', True),
        ('There is nothing here', 'duck', False)
        ]

@pytest.mark.parametrize('sample, word, expected_output', contains_words_testdata)
def test_text_contains_words(sample, word, expected_output):

    assert text_contains_words(word, sample) == expected_output

