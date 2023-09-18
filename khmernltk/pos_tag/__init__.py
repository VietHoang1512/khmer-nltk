import os
from typing import List, Tuple

from khmernltk import word_tokenize
from khmernltk.pos_tag.features import create_word_features
from khmernltk.utils.data import cleanup_str
from khmernltk.utils.file_utils import load_model

# sklearn_crf_pos_alt_0.9849.sav
model_path = os.path.join(os.path.dirname(__file__), "sklearn_crf_pos_alt_0.9846.sav")
crf_model = None


def pos_tag(text: str) -> List[Tuple[str, str]]:
    """Khmer language Part of speech tagging

    Args:
        text (str): Raw text

    Returns:
        List[Tuple[str, str]]: List of tuple (token, pos tag)
    """
    global crf_model
    if crf_model is None:
        crf_model = load_model(model_path)

    text = cleanup_str(text)
    tokens = word_tokenize.word_tokenize(text, return_tokens=True)
    features = create_word_features(tokens)
    pred = crf_model.predict([features])[0]
    return list(zip(tokens, pred))
