import argparse
from tqdm import tqdm

from khmernltk import word_tokenize

parser = argparse.ArgumentParser()

parser.add_argument("--input_file", type=str,
                    default="samples/input.txt",
                    help='path to the non-tokenized input text file')

parser.add_argument("--output_file", type=str,
                    default="samples/output.txt",
                    help='path to the expected tokenized output file')
                    
parser.add_argument("--separator", type=str,
                    default="_")

args = parser.parse_args()

if __name__== "__main__":
    
    with open(args.input_file, "r") as f:
        sentences = f.read().strip().split("\n")
    
    total = len(sentences)
    tokenized_sentences = []
    for sentence in tqdm(sentences, desc=f"Tokenizing {total} sentences", total=total):
        tokenized_sentences.append(word_tokenize(sentence, separator=args.separator))
    
    with open(args.output_file, "w") as f:
        f.write("\n".join(tokenized_sentences))
    