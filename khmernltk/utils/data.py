import re

from khmernltk.utils.constants import *


def correct_text(text: str):
    for token, normalized_token in mistokenized_dict.items():
        text = text.replace(token, normalized_token)
    return text


def cleanup_str(text: str):
    text = text.strip(SEPARATOR).strip()
    text = text.replace("  ", " ")  # clean up 2 spaces to 1
    text = text.replace(" ", "\u200b \u200b")  # ensure 200b around space
    # clean up
    text = text.replace("\u200b\u200b", "\u200b")  # clean up dupe 200b
    text = text.replace("\u200b\u200b", "\u200b")  # in case multiple
    text = correct_text(text)  # assume space has 200b wrapped around

    # remove special characters
    text = text.replace("\u2028", "")  # line separator
    text = text.replace("\u200a", "")  # hair space
    text = text.strip().replace("\n", "").replace("  ", " ")
    return text


def post_process(text, separator):
    text = text.strip(separator)
    return re.sub(f"(?:{separator}| )+", separator, text)


def is_khmer_char(ch: str):
    if (ch >= "\u1780") and (ch <= "\u17ff"):
        return True
    if ch in KHSYM:
        return True
    if ch in KHLUNAR:
        return True
    return False


def is_start_of_kcc(ch: str):
    if is_khmer_char(ch):
        if ch in KHCONST:
            return True
        if ch in KHSYM:
            return True
        if ch in KHNUMBER:
            return True
        if ch in KHLUNAR:
            return True
        return False
    return True


# kcc base - must surround space with \u200b using cleanupstr()


def seg_kcc(str_sentence: str):
    segs = []
    cur = ""
    sentence = str_sentence
    for word in sentence.split(SEPARATOR):
        for i, c in enumerate(word):
            cur += c
            nextchar = word[i + 1] if (i + 1 < len(word)) else ""

            # cluster non-khmer chars together
            if not is_khmer_char(c) and nextchar != " " and nextchar != "" and not is_khmer_char(nextchar):
                continue
            # cluster number together
            if c in KHNUMBER and nextchar in KHNUMBER:
                continue

            # cluster non-khmer together
            # non-khmer character has no cluster
            if not is_khmer_char(c) or nextchar == " " or nextchar == "":
                segs.append(cur)
                cur = ""
            elif is_start_of_kcc(nextchar) and not (c in KHSUB):
                segs.append(cur)
                cur = ""
        # add space back after split
        # segs.append(" ")
    return segs  # [:-1] # trim last space
