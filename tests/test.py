import pytest

from khmernltk import pos_tag, sentence_tokenize, word_tokenize

text = (
    "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
)
correct = "​ខួប​ឆ្នាំ​ទី ២៨ !​ ២៣ ​តុលា ​ស្មារតី​ផ្សះផ្សា​ជាតិ​រវាង​ខ្មែរ​និង​ខ្មែរ ​ឈាន​ទៅ​បញ្ចប់​សង្រ្គាម ​នាំ​ពន្លឺ​សន្តិភាព​ ​និង​ការរួបរួម​ជាថ្មី​"

# test sentence tokenizer
print("sentence-level tokenized text")
print(sentence_tokenize(text))

# test word tokenizer
sep = "_"
print("word-level tokenized text")
print(word_tokenize(text, separator=sep, return_tokens=True))
print("correct text")
print(correct.strip("\u200b").replace("\u200b", sep))

# test pos tagger
print(pos_tag(text))
