from khmernltk.utils.constants import *
from khmernltk.utils.data import *


def get_type(char: str):
    if char.lower() in EN:
        return NS
    if char in KHCONST:
        return "C"
    if char in KHVOWEL:
        return "W"
    if char in KHNUMBER:
        return NS
    if char in KHSUB:
        return "S"
    if char in KHDIAC:
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

    features = {"kcc": kcc, "t": kcc_type(kcc), "ns": is_no_space(kcc)}
    if i >= 1:
        features.update(
            {
                "kcc[-1]": kccs[i - 1],
                "kcc[-1]t": kcc_type(kccs[i - 1]),
                "kcc[-1:0]": kccs[i - 1] + kccs[i],
                "ns-1": is_no_space(kccs[i - 1]),
            }
        )
    else:
        features["BOS"] = True

    if i >= 2:
        features.update(
            {
                "kcc[-2]": kccs[i - 2],
                "kcc[-2]t": kcc_type(kccs[i - 2]),
                "kcc[-2:-1]": kccs[i - 2] + kccs[i - 1],
                "kcc[-2:0]": kccs[i - 2] + kccs[i - 1] + kccs[i],
            }
        )
    if i >= 3:
        features.update(
            {
                "kcc[-3]": kccs[i - 3],
                "kcc[-3]t": kcc_type(kccs[i - 3]),
                "kcc[-3:0]": kccs[i - 3] + kccs[i - 2] + kccs[i - 1] + kccs[i],
                "kcc[-3:-1]": kccs[i - 3] + kccs[i - 2] + kccs[i - 1],
                "kcc[-3:-2]": kccs[i - 3] + kccs[i - 2],
            }
        )

    if i < maxi - 1:
        features.update(
            {
                "kcc[+1]": kccs[i + 1],
                "kcc[+1]t": kcc_type(kccs[i + 1]),
                "kcc[+1:0]": kccs[i] + kccs[i + 1],
                "ns+1": is_no_space(kccs[i + 1]),
            }
        )
    else:
        features["EOS"] = True

    if i < maxi - 2:
        features.update(
            {
                "kcc[+2]": kccs[i + 2],
                "kcc[+2]t": kcc_type(kccs[i + 2]),
                "kcc[+1:+2]": kccs[i + 1] + kccs[i + 2],
                "kcc[0:+2]": kccs[i + 0] + kccs[i + 1] + kccs[i + 2],
                "ns+2": is_no_space(kccs[i + 2]),
            }
        )
    if i < maxi - 3:
        features.update(
            {
                "kcc[+3]": kccs[i + 3],
                "kcc[+3]t": kcc_type(kccs[i + 3]),
                "kcc[+2:+3]": kccs[i + 2] + kccs[i + 3],
                "kcc[+1:+3]": kccs[i + 1] + kccs[i + 2] + kccs[i + 3],
                "kcc[0:+3]": kccs[i + 0] + kccs[i + 1] + kccs[i + 2] + kccs[i + 3],
            }
        )

    return features


def create_kcc_features(kccs):
    return [kcc_to_features(kccs, i) for i in range(len(kccs))]
