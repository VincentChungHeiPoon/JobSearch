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
        

string = 'As a member of our Software Engineering Group we look first and foremost for people who are passionate around solving business problems through innovation & engineering practices. You will be required to apply your depth of knowledge and expertise to all aspects of the software development lifecycle, as well as partner continuously with your many stakeholders on a daily basis to stay focused on common goals. We embrace a culture of experimentation and constantly strive for improvement and learning. You’ll work in a collaborative, trusting, thought-provoking environment—one that encourages diversity of thought and creative solutions that are in the best interests of our customers globally.'
a = keyWordFilter()
a.addWordToList('hi')
a.addWordToList('2')
a.addWordToList('2')