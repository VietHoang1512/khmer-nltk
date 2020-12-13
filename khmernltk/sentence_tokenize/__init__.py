import re
from khmernltk.sentence_tokenize.features import SENTENCE_SEPARATOR

def sentence_tokenize(text:str):
    sentences = re.split(r"(?<=[" +"".join(SENTENCE_SEPARATOR) + "])\s*", text)
    return sentences
    

if __name__ == "__main__":
    text = "ខេត្តកំពង់ធំ ៖ ឪពុកនិង​កូន​ប្រុស​នាំគ្នា​យកម៉ូទ័រ​​ទៅ​ ។"
    print(len(sentence_tokenize(text)))
    print(sentence_tokenize(text))