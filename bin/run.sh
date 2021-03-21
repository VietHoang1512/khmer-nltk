#!/bin/bash

python scripts/run.py \
            -i samples/input.txt \
            -o samples/output.txt \
            -f sentence_tokenize

python scripts/run.py \
            -i samples/input.txt \
            -o samples/output.txt \
            -f word_tokenize

python scripts/run.py \
            -i samples/input.txt \
            -o samples/output.txt \
            -f pos_tag

