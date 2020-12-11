### Khmer natural language processing tookit

Adapted from original [repo](https://github.com/phylypo/segmentation-crf-khmer)


#### TODO

* [X] Sentence Segmentation
* [X] Word Segmentation
* [ ] Named Entity Recognition
* [ ] Part of speech Tagging


#### Word segmentation:

```
Iter 100 time=13.17 loss=14383.13 active=262344 feature_norm=742.32
L-BFGS terminated with the maximum number of iterations
Total seconds required for training: 1662.000
Storing the model
Number of active features: 262344 (5466873)
Number of active attributes: 180020 (5108385)
Number of active labels: 2 (2)
Writing labels
Writing attributes
Writing feature references for transitions
Writing feature references for attributes
Seconds required: 0.238
File: sklearn_crf_model_10000.sav
Train set num sentences: 58153
Performance on training set: 0.9997525919880873
Test set num sentences: 14539
Performance on test set: 0.9976550064522012
```
