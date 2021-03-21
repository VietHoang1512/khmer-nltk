import re
from typing import List

from khmernltk.sentence_tokenize.features import SENTENCE_SEPARATOR


def sentence_tokenize(text: str) -> List[str]:
    """Khmer language sentence tokenization

    Args:
        text (str): Raw text

    Returns:
        List[str]: List of sentences
    """
    sentences = re.split("(?<=[" + "".join(SENTENCE_SEPARATOR) + "])\s*", text)
    if sentences[-1]:
        return sentences
    return sentences[:-1]
