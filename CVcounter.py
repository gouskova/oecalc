#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import regex as re

'''
a module for counting various CV patterns in a .txt file. The file should have one word per line, with segments separated by spaces--like this:

p̩ʲ u t i
r i n t u
f a ʃ o

To use:

$ CVcounter LearningData.txt

This will print:

sequence		count
V C V		1369
V V		0
C V C C C		0
C V V C		0
C C V C		35
C C		1249
V C C V		1071
C V C		2414
V C C C V		0
C C C		0
C V C C		963

Other options:

$ CVcounter ~/you/yourdirectory/textfilewithwords.txt 'C V C'

This will print just the count for CVC

$ 

if the regex module is not installed:

$ pip3 install regex --user

'''

def countCVC(path, searchseqs='default', vs=['a','e','i','o','u']):
    '''
    path is a path to a LearningData.txt file (or similar)
    '''
    if searchseqs == 'default':
        seqs = ['C V C', 'C V C C', 'C V V C', 'C V C C C', 'C C C', 'C C V C', 'C C', 'V C V', 'V V', 'V C C V', 'V C C C V']
    else:
        seqs = [searchseqs]
    if vs != ['a','e','i','o','u']:
        vowels = vs.split(' ')
        print('the vowels are: '+ ' '.join(vowels))
    else:
        vowels = vs
        print('the vowels are: ' + ' '.join(vowels))
    CVdic = {}.fromkeys(seqs, 0)
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.rstrip("\n")
            for seg in word:
                if not seg in vowels and seg != ' ':
                    word = word.replace(seg, 'C')
                if seg in vowels:
                    word = word.replace(seg, 'V')
            for seq in CVdic:
                #we want to count overlapped instances of CVC in every word, so must use 
                #special module (easier than writing an overwrought regex)
                matches = re.findall(seq, word, overlapped=True)
                n = len(matches)
                CVdic[seq]+=n
    return CVdic


def printCVC(dic):
    '''
    prints CVC counts to screen
    '''
    print('sequence\t\tcount')
    for seq in dic:
        print(seq + '\t\t' + str(dic[seq]))


def CVC(path, searchseqs='default', vs=['a','e','i','o','u']):
    '''
    path is a path to a LearningData.txt file
    '''
    dic =  countCVC(path, searchseqs, vs)
    return printCVC(dic)
        


if __name__ == '__main__':
    import sys
    filepath = sys.argv[1]
    if len(sys.argv)==2:
        CVC(filepath)
    if len(sys.argv)==3:
        CVC(filepath, sys.argv[2])
    else:
        CVC(filepath, sys.argv[2], sys.argv[3])
