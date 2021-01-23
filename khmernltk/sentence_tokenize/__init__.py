import re

from khmernltk.sentence_tokenize.features import SENTENCE_SEPARATOR


def sentence_tokenize(text: str):
    """
    Khmer language sentence tokenization
    ====================================
    :param text: (str) Raw text
    ====================================
    :return: (list) List of sentences
    """
    sentences = re.split("(?<=[" + "".join(SENTENCE_SEPARATOR) + "])\s*", text)
    if sentences[-1]:
        return sentences
    return sentences[:-1]


if __name__ == "__main__":
    pass
    # text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
    # print(len(sentence_tokenize(text)))
    # print(sentence_tokenize(text))
