
import os

from khmernltk.utils.constants import *
from khmernltk.utils.data import *
from khmernltk.pos_tag.features import create_word_features
from khmernltk.utils.file_utils import load_model
from khmernltk import word_tokenize

# sklearn_crf_pos_alt_0.9830.sav
model_path = os.path.join(os.path.dirname(
    __file__), "sklearn_crf_pos_alt_0.9830.sav")
crf_model = load_model(model_path)


def pos_tag(text: str):
    # text = cleanup_str(text)
    tokens = word_tokenize(text, return_tokens=True)
    features = create_word_features(tokens)
    pred = crf_model.predict([features])[0]
    return list(zip(tokens, pred))


if __name__ == "__main__":
    text = "កប់! មួយជាតិការម្ដង Bitoey លេងឈុតស៊ិចស៊ីឡើងរាំជាមួយស្វាមីមុខភ្ញៀវជាច្រើន!(មានវីដេអូ)"
    print(pos_tag(text))