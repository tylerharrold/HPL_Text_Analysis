import chardet 
import codecs

def openFile(fileName):
    # load file into a binary dataset
    binData = open(fileName , "rb").read()
    encoding = chardet.detect(binData) # analyze the binary data
    encoding = encoding['encoding']
    text = codecs.open(fileName , "r" , encoding=encoding).read()
    return text

def splitText(text):
    text = text.split()
    return text

# function that makes all chars lowercase and strips punctuation
def stripWords(words):
    for i in range(len(words)):
        words[i] = words[i].lstrip("(.\"!, \'")
        words[i] = words[i].rstrip(").\"!, \':;")
        words[i] = words[i].lower()
    return words

def getDictionaryOfUniqueWords(words):
    dictionary = {}
    for i in range(len(words)):
        if(words[i] in dictionary):
            dictionary[words[i]] = dictionary[words[i]] + 1
        else:
            dictionary[words[i]] = 1

    return dictionary

def getUniqueTupleList(dictionary):
    tupleList = list(dictionary.items())
    return tupleList

def formatTextIntoDictionary(fileName):
    text = openFile(fileName)
    text = splitText(text)
    text = stripWords(text)
    text = getDictionaryOfUniqueWords(text)
    return text
