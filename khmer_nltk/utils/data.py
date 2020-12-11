import re
from utils.constants import *


def correct_text(text: str):
    for token, normalized_token in mistokenized_dict.items():
        text = text.replace(token, normalized_token)
    return text


def cleanup_str(text: str):
    text = text.strip('\u200b').strip()
    text = text.replace("  ", " ")  # clean up 2 spaces to 1
    text = text.replace(" ", "\u200b \u200b")   # ensure 200b around space
    # clean up
    text = text.replace("\u200b\u200b", '\u200b')   # clean up dupe 200b
    text = text.replace("\u200b\u200b", '\u200b')   # in case multiple
    text = correct_text(text)  # assume space has 200b wrapped around

    # remove special characters
    text = text.replace(u"\u2028", "")  # line separator
    text = text.replace(u"\u200a", "")  # hair space
    text = text.strip().replace('\n', '').replace('  ', ' ')
    return text


# character base segmentation
def seg_char(str_sentence: str):
    #str_sentence = str_sentence.replace(u'\u200b','')
    segs = []
    for phr in str_sentence.split('\u200b'):
        #phr_char = phr.replace(' ','')
        for c in phr:
            segs.append(c)
    return segs

# generate list of (word, label), not splitting into phrases, just remove spaces


def gen_char_with_label(sentence: str):
    sentence = cleanup_str(sentence)  # add 200b between space
    words = sentence.split('\u200b')
    final_kccs = []
    for word in words:
        kccs = seg_char(word)
        labels = [1 if (i == 0 or k == " ") else 0 for i, k in enumerate(kccs)]
        final_kccs.extend(list(zip(kccs, labels)))
    return final_kccs


def post_process(text, separator):
    text = text.strip(separator)
    return re.sub(f"(?:{separator}| )+", separator, text)
