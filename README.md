<div align="center">

# 🏅Khmer natural language processing toolkit🏅

[![circleci](https://circleci.com/gh/VietHoang1512/khmer-nltk/tree/main.svg?style=svg)](https://circleci.com/gh/VietHoang1512/khmer-nltk/tree/main)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/807f43366b314887946cd9e88df700c6)](https://www.codacy.com/gh/VietHoang1512/khmer-nltk/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=VietHoang1512/khmer-nltk&amp;utm_campaign=Badge_Grade)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![release](https://img.shields.io/pypi/v/khmer-nltk.svg)](https://pypi.org/project/khmer-nltk/)
![versions](https://img.shields.io/pypi/pyversions/khmer-nltk.svg)
[![fownloads](https://pepy.tech/badge/khmer-nltk)](https://pepy.tech/project/khmer-nltk)
[![DOI](https://zenodo.org/badge/313328421.svg)](https://zenodo.org/badge/latestdoi/313328421)

</div>

## 🎯TODO

- [X] Sentence Segmentation
- [X] Word Segmentation
- [X] Part of speech Tagging
- [ ] Named Entity Recognition
- [ ] Text classification

## 💪Installation

```bash
pip install khmer-nltk
```

## 🏹 Quick tour

[[Blog]](https://towardsdatascience.com/khmer-natural-language-processing-in-python-c770afb84784)

To get the evaluation result of khmer-nltk's functionalities, please refer the sub-modules's readme

### Sentence tokenization

```python
>>> from khmernltk import sentence_tokenize
>>> raw_text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
>>> print(sentence_tokenize(raw_text))
['ខួបឆ្នាំទី២៨!', '២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី']
```

### [Word tokenization](khmernltk/word_tokenize)

```python
>>> from khmernltk import word_tokenize
>>> raw_text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
>>> print(word_tokenize(raw_text, return_tokens=True))
['ខួប', 'ឆ្នាំ', 'ទី', '២៨', '!', ' ', '២៣', ' ', 'តុលា', ' ', 'ស្មារតី', 'ផ្សះផ្សា', 'ជាតិ', 'រវាង', 'ខ្មែរ', 'និង', 'ខ្មែរ', ' ', 'ឈាន', 'ទៅ', 'បញ្ចប់', 'សង្រ្គាម', ' ', 'នាំ', 'ពន្លឺ', 'សន្តិភាព', ' ', 'និង', 'ការរួបរួម', 'ជាថ្មី']
```

### [POS Tagging](khmernltk/pos_tag)

### Usage

```python
>>> from khmernltk import pos_tag
>>> raw_text = "ខួបឆ្នាំទី២៨! ២៣ តុលា ស្មារតីផ្សះផ្សាជាតិរវាងខ្មែរនិងខ្មែរ ឈានទៅបញ្ចប់សង្រ្គាម នាំពន្លឺសន្តិភាព និងការរួបរួមជាថ្មី"
>>> print(pos_tag(raw_text))
[('ខួប', 'n'), ('ឆ្នាំ', 'n'), ('ទី', 'n'), ('២៨', '1'), ('!', '.'), (' ', 'n'), ('២៣', '1'), (' ', 'n'), ('តុលា', 'n'), (' ', 'n'), ('ស្មារតី', 'n'), ('ផ្សះផ្សា', 'n'), ('ជាតិ', 'n'), ('រវាង', 'o'), ('ខ្មែរ', 'n'), ('និង', 'o'), ('ខ្មែរ', 'n'), (' ', 'n'), ('ឈាន', 'v'), ('ទៅ', 'v'), ('បញ្ចប់', 'v'), ('សង្រ្គាម', 'n'), (' ', 'n'), ('នាំ', 'v'), ('ពន្លឺ', 'n'), ('សន្តិភាព', 'n'), (' ', 'n'), ('និង', 'o'), ('ការរួបរួម', 'n'), ('ជាថ្មី', 'o')]
```

### ✍️ Citation

```bibtex
@misc{hoang-khmer-nltk,
  author = {Phan Viet Hoang},
  title = {Khmer Natural Language Processing Toolkit},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/VietHoang1512/khmer-nltk}}
}
```
#### Used in:
- [stopes: A library for preparing data for machine translation research](https://github.com/facebookresearch/stopes)
- [LASER Language-Agnostic SEntence Representations](https://github.com/facebookresearch/LASER)
- [Pretrained Models and Evaluation Data for the Khmer Language](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9645441)
- [Multilingual Open Text 1.0: Public Domain News in 44 Languages](https://arxiv.org/pdf/2201.05609.pdf)
- [ZusammenQA: Data Augmentation with Specialized Models for Cross-lingual Open-retrieval Question Answering System](https://arxiv.org/pdf/2205.14981.pdf)
- [Shared Task on Cross-lingual Open-Retrieval QA](https://www.aclweb.org/portal/content/shared-task-cross-lingual-open-retrieval-qa)
- [No Language Left Behind: Scaling Human-Centered Machine Translation](https://research.facebook.com/publications/no-language-left-behind/)
- [Wordless](https://github.com/BLKSerene/Wordless)
- [A Simple and Fast Strategy for Handling Rare Words in Neural Machine Translation](https://aclanthology.org/2022.aacl-srw.6/)

### 👨‍🎓 References

- [NLP: Text Segmentation Using Conditional Random Fields](https://medium.com/@phylypo/nlp-text-segmentation-using-conditional-random-fields-e8ff1d2b6060)
- [Khmer Word Segmentation Using Conditional Random Fields](https://www2.nict.go.jp/astrec-att/member/ding/KhNLP2015-SEG.pdf)
- [Word Segmentation of Khmer Text Using Conditional Random Fields](https://medium.com/@phylypo/segmentation-of-khmer-text-using-conditional-random-fields-3a2d4d73956a)

### 📜 Advisor

- Prof. [Huong Le Thanh](https://users.soict.hust.edu.vn/huonglt/)
