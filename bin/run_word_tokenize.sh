input_file="samples/input.txt"
output_file="samples/output.txt"
separator="_"

python -m scripts.word_tokenize \
            --input_file $input_file \
            --output_file $output_file \
            --separator $separator