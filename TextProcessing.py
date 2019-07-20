# -*- coding: utf-8 -*-
"""
    >>>nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    Installing nltk: tokenizer, tagger
    dafault path are in \AppData\Roaming\nltk_data
    Search '%appdata%' will open up roaming folder
    
    tokenizeString takes a string and break it into tokens
    
    tagTokens will tag the tokens from tokenizeString according to its type
    
    filterTagAndSelectTokens will both tokenizeString and tag, after that, it will filter the word by tags
        with this, there are no need to use tokenizeString, tagTokens
    
    addWordToList add, create new word in the keyWord list, which contains word and it's frequency
        used to select most common word
        
    returnTopWordWithCount return topNUmber of element in the sort list, list sorted decending by count
    
"""
import nltk

class keyWord:
    def __init__(self, word):
        self.word = word
        self.count = 1


class keyWordFilter:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    
    def __init__(self):
        self.wordFrequencyList = []
    
    def tokenizeString(string):
        tokens = nltk.word_tokenize(string)
        return tokens
    
    def tagTokens(tokens):
        taggedTokens = nltk.pos_tag(tokens)
        return taggedTokens
    #select possible keywords base on tag
    def filterTagAndSelectTokens(string):
        tokens = keyWordFilter.tokenizeString(string)
        taggedTokens = keyWordFilter.tagTokens(tokens)
        filteredList = list(filter(lambda a: a[1] == 'NNP' or a[1] == 'NN' or a[1] == 'JJ', taggedTokens))
        return filteredList
    
    def addWordToList(self, word):
        existList = [words for words in self.wordFrequencyList if words.word == word]
        if len(existList) == 1: 
            #print(self.wordFrequencyList.index(word))
            self.wordFrequencyList[self.wordFrequencyList.index(existList[0])].count += 1
        else:
            self.wordFrequencyList.append(keyWord(word))
            
    def returTopWordWithCount(self, topNumber):
        self.wordFrequencyList.sort(key=lambda x: x.count, reverse = True)
        
        if(len(self.wordFrequencyList) >= topNumber):
            return self.wordFrequencyList[:topNumber]
        else:
            return self.wordFrequencyList[:len(self.wordFrequencyList)]

