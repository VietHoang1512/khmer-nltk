import os
from typing import List, Union

from khmernltk.utils import constants
from khmernltk.utils.data import cleanup_str, seg_kcc
from khmernltk.utils.file_utils import load_model
from khmernltk.word_tokenize.features import create_kcc_features

# sklearn_crf_ner_alt_0.9725.sav / sklearn_crf_ner_10000.sav
model_path = os.path.join(os.path.dirname(__file__), "sklearn_crf_ner_10000.sav")
crf_model = None


def word_tokenize(text: str, separator: str = "-", return_tokens: bool = True) -> Union[List, str]:
    """Khmer language word tokenization

    Args:
        text(str): Raw text
        separator(str, optional): Token - separator in case return_tokens = True. Defaults to "-".
        return_tokens(bool, optional): Whether return a tokenized text or a list of tokens. Defaults to True.

    Returns:
        Union[List, str]: Tokens or tokenized text, separated by the separator
    """
    global crf_model
    if crf_model is None:
        crf_model = load_model(model_path)

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
