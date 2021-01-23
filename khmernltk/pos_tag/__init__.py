import os

from khmernltk import word_tokenize
from khmernltk.pos_tag.features import create_word_features
from khmernltk.utils.constants import *
from khmernltk.utils.data import *
from khmernltk.utils.file_utils import load_model

# sklearn_crf_pos_alt_0.9849.sav
model_path = os.path.join(os.path.dirname(__file__), "sklearn_crf_pos_alt_0.9849.sav")
crf_model = load_model(model_path)


def pos_tag(text: str):
    """
    Khmer language Part of speech tagging
    =====================================
    :param text: (str) Raw text
    =====================================
    :return: (list) List of tuple (token, pos tag)
    """
    text = cleanup_str(text)
    tokens = word_tokenize.word_tokenize(text, return_tokens=True)
    features = create_word_features(tokens)
    pred = crf_model.predict([features])[0]
    return list(zip(tokens, pred))


if __name__ == "__main__":
    pass
    # text = "កប់! មួយជាតិការម្ដង Bitoey លេងឈុតស៊ិចស៊ីឡើងរាំជាមួយស្វាមីមុខភ្ញៀវជាច្រើន!(មានវីដេអូ)"
    # print(pos_tag(text))
