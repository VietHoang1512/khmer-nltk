## 🏅Khmer natural language processing toolkit🏅

### 💪💪💪 TODO:

* [X] Sentence Segmentation
* [X] Word Segmentation
* [ ] Named Entity Recognition
* [X] Part of speech Tagging
* [ ] Text classification

### 🎯🎯🎯 Installation

```bash
$ pip install python-khmernltk
```

### 🏹🏹🏹 Quick tour:

#### Sentence tokenization:

```python
>>> from khmernltk import sentence_tokenize
>>> raw_text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
>>> print(sentence_tokenize(raw_text))
['ខួបឆ្នាំទី២៨!', '២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី']
```

#### [Word tokenization](https://github.com/VietHoang1710/khmer-nltk/tree/main/khmernltk/word_tokenize/README.md):

```python
>>> from khmernltk import word_tokenize
>>> raw_text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
>>> print(word_tokenize(raw_text, return_tokens=True))
['ខួប', 'ឆ្នាំ', 'ទី', '២៨', '!', ' ', '២៣', ' ', 'តុលា', ' ', 'ស្មារតី', 'ផ្សះផ្សា', 'ជាតិ', 'រវាង', 'ខ្មែរ', 'និង', 'ខ្មែរ', ' ', 'ឈាន', 'ទៅ', 'បញ្ចប់', 'សង្រ្គាម', ' ', 'នាំ', 'ពន្លឺ', 'សន្តិភាព', ' ', 'និង', 'ការរួបរួម', 'ជាថ្មី']
```

#### [POS Tagging](https://github.com/VietHoang1710/khmer-nltk/tree/main/khmernltk/pos_tag/README.md):

#### Usage:

```python
>>> from khmernltk import pos_tag
>>> raw_text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
>>> print(pos_tag(raw_text))
[('ខួប', 'n'), ('ឆ្នាំ', 'n'), ('ទី', 'n'), ('២៨', '1'), ('!', '.'), (' ', 'n'), ('២៣', '1'), (' ', 'n'), ('តុលា', 'n'), (' ', 'n'), ('ស្មារតី', 'n'), ('ផ្សះផ្សា', 'n'), ('ជាតិ', 'n'), ('រវាង', 'o'), ('ខ្មែរ', 'n'), ('និង', 'o'), ('ខ្មែរ', 'n'), (' ', 'n'), ('ឈាន', 'v'), ('ទៅ', 'v'), ('បញ្ចប់', 'v'), ('សង្រ្គាម', 'n'), (' ', 'n'), ('នាំ', 'v'), ('ពន្លឺ', 'n'), ('សន្តិភាព', 'n'), (' ', 'n'), ('និង', 'o'), ('ការរួបរួម', 'n'), ('ជាថ្មី', 'o')]
```

### ✍️✍️✍️ Citation

```bibtex
@misc{hoang-khmer-nltk,
  author = {Phan Viet Hoang},
  title = {Khmer Natural Language Processing Tookit},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/VietHoang1710/khmer-nltk}}
}
```

### 👨‍🎓👨‍🎓👨‍🎓 References:

- [NLP: Text Segmentation Using Conditional Random Fields](https://medium.com/@phylypo/nlp-text-segmentation-using-conditional-random-fields-e8ff1d2b6060)
- [Khmer Word Segmentation Using
  Conditional Random Fields](https://www2.nict.go.jp/astrec-att/member/ding/KhNLP2015-SEG.pdf)
- [Underthesea](https://github.com/undertheseanlp/underthesea)
