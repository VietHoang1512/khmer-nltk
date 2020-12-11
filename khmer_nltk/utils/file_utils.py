import os
import re
import glob
import pickle
from tqdm import tqdm

from khmer_nltk.utils.data import cleanup_str
from khmer_nltk.utils.constants import *


def get_data_from_folder(data_dir: str, max_sentences=100000):
    path = data_dir + '/*_seg_200b.txt'  # earlier format: *_seg.txt
    files = glob.glob(path)

    # global variables that use through out
    sentences = []
    seg_text = []
    orig_text = []
    # unique id of the article that can be matched to docId in meta.txt
    doc_ids = []
    for file in tqdm(files, desc=f"Getting data from {data_dir}", leave=True):
        filenum = re.search(r'\d+_', file).group(0)
        doc_ids.append(filenum.replace("_", ""))
        f = open(file, 'r')
        lines = f.readlines()
        f.close()

        seg_text.append(lines)

        if len(seg_text) >= max_sentences:
            break

        # read orig text -- comment out (10K docs which do not have orig text)
        f = open(file.replace('_seg_200b.txt', '_orig.txt'), 'r')
        lines = f.readlines()
        f.close()
        orig_text.append(lines)

    for i, text in enumerate(seg_text):
        for sentence in text:
            sentences.append(cleanup_str(sentence))

    logger.info(f"number of file: {len(files)}")
    logger.info(f"number of doc_ids: {len(doc_ids)}")
    logger.info(f"number of sentences: {len(sentences)}")
    return sentences  # , orig_text


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
    get_data_from_folder(
        "/home/leonard/leonard/nlp/khmer_segmentation/data/kh_data_10000")
