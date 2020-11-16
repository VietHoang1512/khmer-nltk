from typing import List

from utils.constants import *
from utils.kcc import seg_kcc, create_kcc_features
from utils.file_utils import load_model
from utils.data import post_process


class WordTokenizer:

    def __init__(self):
        self.separator = "_"
        self.crf_model = None
        self.seg_kcc = seg_kcc
        self.create_kcc_features = create_kcc_features
        self.post_process = post_process

    def batch_encode(self, texts: List[str], return_tokens=False):
        if not self.crf_model:
            raise Exception(
                "CRF model must be trained or load from pretrained")
        features = []
        for text in texts:
            feature = self.create_kcc_features(self.seg_kcc(text))
            features.append(feature)
        pred = self.crf_model.predict(features)
        outputs = []
        for idx, feature in enumerate(features):
            tkcc = []
            for k in feature:
                tkcc.append(k['kcc'])
            complete = ""
            # token = ""
            # tokens = []
            for i, p in enumerate(pred[0]):
                if p == "1":
                    complete += self.separator + tkcc[i]
                    # if token:
                    #     tokens.append(token)
                    # token = tkcc[i]
                else:
                    complete += tkcc[i]
                    # token += tkcc[i]
                # if i == len(pred)-1:
                #     tokens.append(token)
            complete = self.post_process(complete, self.separator)
            outputs.append(complete)
        return outputs

    def encode(self, text: str):
        return self.batch_encode([text])[0]

    def from_pretrained(self, fp):
        self.crf_model = load_model(fp)
        # print(type(self.crf_model))

if __name__ == "__main__":
    t = "ចំណែកជើងទី២ នឹងត្រូវធ្វើឡើងឯប្រទេសកាតា៕"
    t_correct = "ចំណែក ជើង ទី ២ នឹង ត្រូវ ធ្វើឡើង ឯ ប្រទេស កាតា ៕ "
    tokenizer = WordTokenizer()
    tokenizer.from_pretrained(
        "/home/leonard/leonard/nlp/khmer_segmentation/outputs/sklearn_crf_model_10k.pkl")

    print(tokenizer.encode(t))
