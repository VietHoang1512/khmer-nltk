from khmernltk import sentence_tokenize, word_tokenize, pos_tag

text = "ដោយឡែកសាកសពជនរងគ្រោះទាំង២ ត្រូវបានសមត្ថកិច្ចប្រគល់ទៅឲ្យក្រុមគ្រួសារយកទៅចាត់ចែងធ្វើបុណ្យតាមប្រពៃណីរៀងៗខ្លួន ៕"
correct = "ដោយឡែក​សាកសព​ជនរងគ្រោះ​ទាំង ២ ​ត្រូវបាន​សមត្ថកិច្ច​ប្រគល់​ទៅឲ្យ​ក្រុមគ្រួសារ​យក​ទៅ​ចាត់ចែង​ធ្វើ​បុណ្យ​តាម​ប្រពៃណី​រៀង​ៗ​ខ្លួន​ ៕"

# test sentence tokenizer
print("sentence-level tokenized text")
print(sentence_tokenize(text))

# test word tokenizer
sep = "_"
print("word-level tokenized text")
print(word_tokenize(text, separator = sep))
print("correct text")
print(correct.strip("\u200b").replace("\u200b", sep))

# test pos tagger
print(pos_tag(text))