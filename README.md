### Khmer natural language processing tookit

#### TODO:

* [X] Sentence Segmentation
* [X] Word Segmentation
* [ ] Named Entity Recognition
* [ ] Part of speech Tagging

##### Word segmentation:

- Original [repo](https://github.com/phylypo/segmentation-crf-khmer)

```bash
Iter 100 time=13.34 loss=14383.13 active=262344 precision=0.998  recall=0.998  F1=0.998  Acc(item/seq)=0.998 0.818  feature_norm=742.32
================================================
  Label    Precision    Recall     F1    Support
-------  -----------  --------  -----  ---------
      0        0.998     0.998  0.998     791456
      1        0.998     0.998  0.998     721981
------------------------------------------------
Total seconds required for training: 1355.816
Number of active features: 262344 (5466873)
Number of active attributes: 180020 (5710703)
Number of active labels: 2 (2)
Train set num sentences: 58153
Performance on training set: 0.9997525919880873
Test set num sentences: 14539
Performance on test set: 0.9976550064522012
```


- [Asian Language Treebank (ALT)](https://www2.nict.go.jp/astrec-att/member/mutiyama/ALT/)

```bash
Iter 100 time=2.01  loss=83190.08 active=102602 precision=0.970  recall=0.970  F1=0.970  Acc(item/seq)=0.973 0.223  feature_norm=157.96
================================================
  Label    Precision    Recall     F1    Support
-------  -----------  --------  -----  ---------
      0        0.979     0.978  0.978     183201
      1        0.962     0.963  0.963     105562
------------------------------------------------
Total seconds required for training: 221.182
Number of active features: 102602 (2501777)
Number of active attributes: 64735 (2676196)
Number of active labels: 2 (2)
Train set num sentences: 16084
Performance on training set: 0.9819638316441394
Test set num sentences: 4022
Performance on test set: 0.9725380329197301
```


#### References:

- [NLP: Text Segmentation Using Conditional Random Fields](https://medium.com/@phylypo/nlp-text-segmentation-using-conditional-random-fields-e8ff1d2b6060)
- [Khmer Word Segmentation Using
  Conditional Random Fields](https://www2.nict.go.jp/astrec-att/member/ding/KhNLP2015-SEG.pdf)
- [Underthesea](https://github.com/undertheseanlp/underthesea)
