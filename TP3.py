import nltk
import xml.etree.ElementTree as ET
from nltk.corpus import brown
from nltk.corpus import treebank
#import matplotlib.pyplot as plt
from nltk.app.wordfreq_app import app as wordfreq
from nltk.corpus import conll2000
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.chunk import ne_chunk
#
import re


#get all questions from XML where lang = en
questions = []
tree = ET.parse('questions.xml')
root = tree.getroot()
for string in root.iter('string'):
    if(string.attrib["lang"] == "en"):
        questions.append(string.text.strip('\t\n'))

#tokenize questions
tokenized = []
for question in questions:
    tokenized_string = nltk.word_tokenize(question)
    tokenized.append(nltk.pos_tag(tokenized_string))

res_chunk = ne_chunk(tokenized[1])
print(res_chunk)

# list of regex
re_list = [
    '^[wW]ho',
    '^[wW]hen',
    '^[wW]here',
    '^[wW]hich'
]


#find the object of our search
generic_re = re.compile( '|'.join( re_list)).findall(questions[1])
if generic_re[0] == 'Where' or generic_re[0] == 'where'  :
    print("We are looking for a place")
if generic_re[0] == 'When' or generic_re[0] == 'when'  :
    print("We are looking for a date")
if generic_re[0] == 'Who' or generic_re[0] == 'who'  :
    print("We are looking for a person or organisation")
if generic_re[0] == 'Which' or generic_re[0] == 'which'  :
    print("request with the word just next to which and the named entity we get from txt")

# print named entities
print("and our named entities for this query are :")
for chunk in res_chunk:
    if hasattr(chunk, 'label'):
       print(chunk.label(), ' '.join(c[0] for c in chunk))


