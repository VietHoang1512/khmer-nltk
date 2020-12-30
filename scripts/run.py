import argparse

from tqdm import tqdm

from khmernltk import pos_tag, sentence_tokenize, word_tokenize

funtionalities = ["sentence_tokenize", "word_tokenize", "pos_tagging"]

parser = argparse.ArgumentParser()

parser.add_argument(
    "-i",
    "--input_file",
    type=str,
    # default="samples/input.txt",
    help="path to the non-tokenized input text file",
)

parser.add_argument(
    "-o",
    "--output_file",
    type=str,
    # default="samples/output.txt",
    help="path to the expected tokenized output file",
)

parser.add_argument("-f", "--function", type=str, help="Select functionality in list {funtionalities} ")


args = parser.parse_args()

if __name__ == "__main__":

    with open(args.input_file, "r") as f:
        sentences = f.read().strip().split("\n")

    print("args.function", args.function)
    if args.function == "sentence_tokenize":
        function = sentence_tokenize
    elif args.function == "word_tokenize":
        function = word_tokenize
    elif args.function == "pos_tag":
        function = pos_tag
    else:
        raise Exception(f"Not Implemented Error. Function can only be in {funtionalities}.")

    total = len(sentences)
    outputs = []
    for sentence in tqdm(sentences, desc=f"Processing {total} sentences", total=total):
        str_outputs = str(function(sentence))
        outputs.append(str_outputs)

    with open(args.output_file, "w") as f:
        f.write("\n".join(outputs))
