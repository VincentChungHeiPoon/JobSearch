# -*- coding: utf-8 -*-
import nltk
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
class keyWordFilter:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    
    def tokenizeString(string):
        tokens = nltk.word_tokenize(string)
        return tokens
    
    def tagTokens(tokens):
        taggedTokens = nltk.pos_tag(tokens)
        return taggedTokens

    def filterTagAndSelectTokens(string):
        tokens = keyWordFilter.tokenizeString(string)
        taggedTokens = keyWordFilter.tagTokens(tokens)
        b = list(filter(lambda a: a[1] != 'NNP', taggedTokens))
        print(b)
        

keyWordFilter.filterTagAndSelectTokens('Strong Python/shell scripting experience')