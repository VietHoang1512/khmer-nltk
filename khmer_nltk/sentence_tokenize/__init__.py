import re
from khmer_nltk.utils.constants import SENTENCE_SEPARATOR

def sentence_tokenize(text:str):
    sentences = re.findall(".*?[" + "".join(SENTENCE_SEPARATOR) + "]+", text)
    return sentences

if __name__ == "__main__":
    text = "ខេត្តកំពង់ធំ ៖ ឪពុកនិង​កូន​ប្រុស​នាំគ្នា​យកម៉ូទ័រ​​ទៅ​ ។"
    print(len(sentence_tokenize(text)))
    print(sentence_tokenize(text))