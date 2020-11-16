from typing import List
from tqdm import tqdm

from utils.constants import *
from utils.data import cleanup_str, gen_char_with_label, seg_char


def data_generator(sentences: List):
    kccs_label = []
    kccs_only = []
    labels = []
    for sen in tqdm(sentences, desc="Processing text"):
        kcc_with_label = gen_kcc_with_label(sen)
        kccs_label.append(kcc_with_label)
        kccs_only.append(seg_kcc(sen))
        labels.append(create_labels_from_kccs(kcc_with_label))

    bad_count = 0
    for i, kccs in tqdm(enumerate(kccs_only), desc="Generating kcc features"):
        labels_count = len(labels[i])
        if len(kccs) != labels_count:
            logger.warning(
                f"i {i} entry didn't match. len kccs {len(kccs)} len labels {labels_count}")
            logger.warning(kccs)
            logger.warning(labels[i])
            bad_count = bad_count + 1
    if bad_count == 0:
        logger.info("No entry means we are good to go")
        logger.info("If there are entries, need to see which characters was not removed correctly.")
    else:
        logger.info("total count:", len(
            kccs_only), " bad count:", bad_count)

    chars_label = []
    chars_only = []
    labels_char = []

    for sen in tqdm(sentences, desc="Finalizing data generating"):
        chars_with_label = gen_char_with_label(sen)
        chars_label.append(chars_with_label)
        chars_only.append(seg_char(sen))
        labels_char.append(create_labels_from_kccs(chars_with_label))

    X_char = [create_kcc_features(kcc_line) for kcc_line in chars_only]
    y_char = labels_char
    logger.info("DONE")
    logger.info(f"Num X samples {len(X_char)}, num y samples {len(y_char)}")
    return X_char, y_char


def is_khmer_char(ch: str):
    if (ch >= '\u1780') and (ch <= '\u17ff'):
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
    # for phr in str_sentence.split(): #no longer split by space, use 200b
    #    logger.warning("phr: '", phr,"'")
    for word in sentence.split('\u200b'):
        #logger.warning("PHR:[%s] len:%d" %(phr, len(phr)))
        for i, c in enumerate(word):
            #logger.warning(i," c:", c)
            cur += c
            nextchar = word[i+1] if (i+1 < len(word)) else ""

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
        #segs.append(" ")
    return segs  # [:-1] # trim last space


def gen_kcc_with_label(sentence: str):
    sentence = cleanup_str(sentence)  # add 200b between space
    final_kccs = []
    # for ph in sentence.split():
    for w in sentence.split('\u200b'):
        kccs = seg_kcc(w)
        labels = [1 if (i == 0 or k == " ") else 0 for i, k in enumerate(kccs)]
        final_kccs.extend(list(zip(kccs, labels)))
    return final_kccs


def get_type(chr: str):
    if chr.lower() in EN:
        return NS
    if chr in KHCONST:
        return "C"
    if chr in KHVOWEL:
        return "W"
    if chr in KHNUMBER:
        return NS
    if chr in KHSUB:
        return "S"
    if chr in KHDIAC:
        return "D"
    return NS

# non-khmer character that we should not separate like number
# multiple characters are false


def is_no_space(k):
    if get_type(k[0]) == NS:
        return True
    return False


def kcc_type(k):
    if len(k) == 1:
        return get_type(k)
    else:
        return "K" + str(len(k))


def kcc_to_features(kccs, i):
    maxi = len(kccs)
    kcc = kccs[i]

    features = {
        'kcc': kcc,
        't': kcc_type(kcc),
        'ns': is_no_space(kcc)
    }
    if i >= 1:
        features.update({
            'kcc[-1]': kccs[i-1],
            'kcc[-1]t': kcc_type(kccs[i-1]),
            'kcc[-1:0]': kccs[i-1] + kccs[i],
            'ns-1': is_no_space(kccs[i-1])
        })
    else:
        features['BOS'] = True

    if i >= 2:
        features.update({
            'kcc[-2]': kccs[i-2],
            'kcc[-2]t': kcc_type(kccs[i-2]),
            'kcc[-2:-1]': kccs[i-2] + kccs[i-1],
            'kcc[-2:0]': kccs[i-2] + kccs[i-1] + kccs[i],
        })
    if i >= 3:
        features.update({
            'kcc[-3]': kccs[i-3],
            'kcc[-3]t': kcc_type(kccs[i-3]),
            'kcc[-3:0]': kccs[i-3] + kccs[i-2] + kccs[i-1] + kccs[i],
            'kcc[-3:-1]': kccs[i-3] + kccs[i-2] + kccs[i-1],
            'kcc[-3:-2]': kccs[i-3] + kccs[i-2],
        })

    if i < maxi-1:
        features.update({
            'kcc[+1]': kccs[i+1],
            'kcc[+1]t': kcc_type(kccs[i+1]),
            'kcc[+1:0]': kccs[i] + kccs[i+1],
            'ns+1': is_no_space(kccs[i+1])

        })
    else:
        features['EOS'] = True

    if i < maxi-2:
        features.update({
            'kcc[+2]': kccs[i+2],
            'kcc[+2]t': kcc_type(kccs[i+2]),
            'kcc[+1:+2]': kccs[i+1] + kccs[i+2],
            'kcc[0:+2]': kccs[i+0] + kccs[i+1] + kccs[i+2],
            'ns+2': is_no_space(kccs[i+2])
        })
    if i < maxi-3:
        features.update({
            'kcc[+3]': kccs[i+3],
            'kcc[+3]t': kcc_type(kccs[i+3]),
            'kcc[+2:+3]': kccs[i+2] + kccs[i+3],
            'kcc[+1:+3]': kccs[i+1] + kccs[i+2] + kccs[i+3],
            'kcc[0:+3]': kccs[i+0] + kccs[i+1] + kccs[i+2] + kccs[i+3],
        })

    return features


def generate_kccs_label_per_phrase(sentence):
    phrases = sentence.split()
    logger.warning("prep_kcc_labels -- number of phrases:", len(phrases))
    final_kccs = []
    for phrase in phrases:
        kccs = seg_kcc(phrase)
        labels = [1 if (i == 0) else 0 for i, k in enumerate(kccs)]
        final_kccs.extend(list(zip(kccs, labels)))
    return final_kccs


def create_kcc_features(kccs):
    return [kcc_to_features(kccs, i) for i in range(len(kccs))]

# take label in second element from kcc with label


def create_labels_from_kccs(kccs_label):
    return [str(part[1]) for part in kccs_label]
