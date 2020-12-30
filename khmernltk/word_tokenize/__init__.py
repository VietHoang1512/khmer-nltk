import os

from khmernltk.utils.constants import *
from khmernltk.utils.data import *
from khmernltk.utils.file_utils import load_model
from khmernltk.word_tokenize.features import create_kcc_features

# sklearn_crf_ner_alt_0.9725.sav / sklearn_crf_ner_10000.sav
model_path = os.path.join(os.path.dirname(__file__), "sklearn_crf_ner_10000.sav")
crf_model = load_model(model_path)


def word_tokenize(text: str, separator: str = "-", return_tokens: bool = True):
    """
    Khmer language word tokenization
    ================================
    :param text: (str) Raw text
    :param separator: (str) Token-separator in case return_tokens=True
    :param return_tokens: (bool) Whether return a tokenized text or a list of tokens
    ================================
    if return_tokens is True
    :return: (list) Tokens
    or else
    :return: (str) Tokenized text, separated by the separator
    """
    text = cleanup_str(text)
    skcc = seg_kcc(text)

    features = create_kcc_features(skcc)
    pred = crf_model.predict([features])

    tkcc = []
    for k in features:
        tkcc.append(k["kcc"])
    complete = ""
    tokens = []
    for i, p in enumerate(pred[0]):
        if p == "1" or i == 0:
            tokens.append(tkcc[i])
        else:
            tokens[-1] += tkcc[i]
    if return_tokens:
        return tokens

    complete = separator.join(tokens)
    complete = complete.replace(separator + " " + separator, " ")

    return complete


if __name__ == "__main__":
    text = "កប់! មួយជាតិការម្ដង Bitoey លេងឈុតស៊ិចស៊ីឡើងរាំជាមួយស្វាមីមុខភ្ញៀវជាច្រើន!(មានវីដេអូ)"
    correct = (
        "​កប់​! ​មួយ​ជាតិ​ការ​ម្ដង​ Bitoey ​លេង​ឈុត​ស៊ិចស៊ី​ឡើង​រាំ​ជាមួយ​ស្វាមី​មុខ​ភ្ញៀវ​ជាច្រើន​!​(​មាន​វីដេអូ​)"
    )
    print(word_tokenize(text))
    print(correct.replace(SEPARATOR, separator))
