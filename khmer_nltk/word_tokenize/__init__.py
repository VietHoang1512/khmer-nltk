import os

from khmer_nltk.utils.constants import *
from khmer_nltk.utils.kcc import seg_kcc, create_kcc_features
from khmer_nltk.utils.file_utils import load_model


SEPARATOR = "-"
model_path = os.path.join(os.path.dirname(__file__), "sklearn_crf_ner_10000.sav")
crf_model = load_model(model_path)

def word_tokenize(text:str):

    skcc = seg_kcc(text)

    features = create_kcc_features(skcc)
    pred = crf_model.predict([features])

    
    tkcc = []
    for k in features:
        tkcc.append(k['kcc'])
    complete = ""
    for i, p in enumerate(pred[0]):
        if p == "1":
            complete += SEPARATOR + tkcc[i]
        else:
            complete += tkcc[i]
    complete = complete.strip(SEPARATOR)
    complete = complete.replace(SEPARATOR+" "+SEPARATOR, " ")
    
    return complete

if __name__=="__main__":
    text = "កប់! មួយជាតិការម្ដង Bitoey លេងឈុតស៊ិចស៊ីឡើងរាំជាមួយស្វាមីមុខភ្ញៀវជាច្រើន!(មានវីដេអូ)"
    correct = "​កប់​! ​មួយ​ជាតិ​ការ​ម្ដង​ Bitoey ​លេង​ឈុត​ស៊ិចស៊ី​ឡើង​រាំ​ជាមួយ​ស្វាមី​មុខ​ភ្ញៀវ​ជាច្រើន​!​(​មាន​វីដេអូ​)"
    print(word_tokenize(text))
    print(correct.replace("\u200b", SEPARATOR))