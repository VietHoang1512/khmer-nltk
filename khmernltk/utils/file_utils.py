import glob
import os
import pickle
import re
import shutil

from tqdm import tqdm

from khmernltk.utils.constants import *
from khmernltk.utils.data import cleanup_str
from khmernltk.utils.log_utils import logger


def get_data_from_folder(data_dir: str, max_sentences=100000):
    path = data_dir + "/*_seg_200b.txt"  # earlier format: *_seg.txt
    files = glob.glob(path)

    # global variables that use through out
    sentences = []
    seg_text = []
    orig_text = []
    # unique id of the article that can be matched to docId in meta.txt
    doc_ids = []
    for file in tqdm(files, desc=f"Getting data from {data_dir}", leave=True):
        filenum = re.search(r"\d+_", file).group(0)
        doc_ids.append(filenum.replace("_", ""))
        f = open(file, "r")
        lines = f.readlines()
        f.close()

        seg_text.append(lines)

        if len(seg_text) >= max_sentences:
            break

        # read orig text -- comment out (10K docs which do not have orig text)
        f = open(file.replace("_seg_200b.txt", "_orig.txt"), "r")
        lines = f.readlines()
        f.close()
        orig_text.append(lines)

    for text in seg_text:
        for sentence in text:
            sentences.append(cleanup_str(sentence))

    logger.info(f"number of file: {len(files)}")
    logger.info(f"number of doc_ids: {len(doc_ids)}")
    logger.info(f"number of sentences: {len(sentences)}")
    return sentences  # , orig_text


def _normalize_token(token):
    assert token.count("[") == token.count("]"), f"token {token} is not valid"
    token = token.replace("-", "")
    assert token[0] == token[-1], f"confused in specify token {token}"
    return token[0]


def cache_nova_text(tok_fp, tag_fp, output_dir):
    with open(tag_fp, "r", encoding="utf8") as f:
        tagged_sentences_text = f.read().strip().split("\n")
    with open(tok_fp, "r", encoding="utf8") as f:
        sentences_text = f.read().strip().split("\n")

    tagged_sentences = {index: tagged for index, tagged in map(lambda text: text.split("\t"), tagged_sentences_text)}
    sentences = {index: tagged for index, tagged in map(lambda text: text.split("\t"), sentences_text)}

    new_tagged_sentences_text = dict()
    new_sentences_text = dict()

    for sentence_id in tqdm(tagged_sentences.keys(), desc="Processing data"):
        new_sentence = ""
        new_tokens = []
        start_of_token = False
        for i, token in enumerate(tagged_sentences[sentence_id].split()):
            if "[" in token:
                new_sentence += SEPARATOR + sentences[sentence_id].split()[i]
                #             token = _normalize_token(token)
                new_tokens.append(token)
                start_of_token = True
                continue

            if start_of_token:
                new_sentence += sentences[sentence_id].split()[i]
                new_tokens[-1] += "+" + token
            else:
                new_sentence += SEPARATOR + sentences[sentence_id].split()[i]
                token = _normalize_token(token)
                new_tokens.append(token)

            if "]" in token:
                start_of_token = False
                new_tokens[-1] = _normalize_token(new_tokens[-1])

        new_sentence = new_sentence.strip(SEPARATOR).strip()
        new_tagged_sentences_text[sentence_id] = " ".join(new_tokens).strip()
        new_sentences_text[sentence_id] = new_sentence
        assert len(new_tokens) == len(new_sentence.split(SEPARATOR)), f"{sentence_id}"

    # new_tagged_sentences_text = OrderedDict(sorted(new_tagged_sentences_text.items()))
    # new_sentences_text = OrderedDict(sorted(new_sentences_text.items()))

    # recreate the output directory (cause we're writing in adding mode)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    for sentence_id in tqdm(sorted(new_tagged_sentences_text.keys()), f"Saving data to {output_dir}"):
        id_ = sentence_id.split(".")
        doc_id = ".".join(id_[:-1])

        tok_fp = os.path.join(output_dir, doc_id + "_seg_200b.txt")
        with open(tok_fp, "a") as f:
            # f.write(sentence_id)
            # f.write("\t")
            f.write(new_sentences_text[sentence_id])
            f.write("\n")

        orig_fp = os.path.join(output_dir, doc_id + "_orig.txt")
        with open(orig_fp, "a") as f:
            # f.write(sentence_id)
            # f.write("\t")
            f.write(new_sentences_text[sentence_id].replace(SEPARATOR, ""))
            f.write("\n")

        tag_fp = os.path.join(output_dir, doc_id + "_tag.txt")

        with open(tag_fp, "a") as f:
            # f.write(sentence_id)
            # f.write("\t")
            f.write(new_tagged_sentences_text[sentence_id])
            f.write("\n")


def save_model(model, fn, output_dir="../../outputs/"):
    os.makedirs(output_dir, exist_ok=True)
    fp = os.path.join(output_dir, fn)
    with open(fp, "wb") as f:
        pickle.dump(model, f)
    logger.info(f"Saved model to {fp}")


def load_model(fp):
    with open(fp, "rb") as f:
        model = pickle.load(f)
    logger.info(f"Loaded model from {fp}")
    return model


if __name__ == "__main__":
    pass
    # get_data_from_folder(
    #     "data/kh_data_10000")
    # cache_nova_text(
    #     tok_fp="data/km-nova-181101/data_km.km-tok.nova",
    #     tag_fp="data/km-nova-181101/data_km.km-tag.nova",
    #     output_dir="data/new-km-nova-181101",
    # )
