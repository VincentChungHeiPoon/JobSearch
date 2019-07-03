# -*- coding: utf-8 -*-
import nltk
import nltk.data
"""
Spyder Editor

This is a temporary script file.
"""

"""
    >>>nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    Installing nltk: tokenizer, tagger
    dafault path are in \AppData\Roaming\nltk_data
    Search '%appdata%' will open up roaming folder
"""
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
tokens = nltk.word_tokenize(sentence)

print(tokens)

taggedTokens = nltk.pos_tag(tokens)

print(taggedTokens)