from pathlib import Path

import pytest

from khmernltk import pos_tag, sentence_tokenize, word_tokenize

root_path = Path(__file__).parent


@pytest.fixture(scope="module")
def test_pos_tag():
    text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
    yield pos_tag(text)


@pytest.fixture(scope="module")
def test_sentence_tokenize():
    text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
    yield sentence_tokenize(text)


@pytest.fixture(scope="module")
def test_word_tokenize():
    text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
    yield word_tokenize(text)
