import hpl_text_parser
import hpl_utils
import os
import codecs

# list of all unique words used by hpl
hplDictionary = {}


def analyzeText(fileName):
    storyName = fileName.strip(".txt")
    # get the dictionary of unique words
    uwd = hpl_text_parser.formatTextIntoDictionary("./texts/" + fileName)
    # format it into a tuple list of word and frequency counts
    utl = hpl_text_parser.getUniqueTupleList(uwd)
    # get word counts
    totalWords = getTotalWords(utl)
    uniqueWords = len(utl)
    leastUsed, mostUsed, oneUse = getLists(utl)
    # add data to global
    # write out local data
    outputName = "./analysis/" + storyName + "_analysis" + ".txt"
    #f = open("./texts/"+outputName , "w")
    with codecs.open(outputName , "w" , encoding="utf-8") as f:
        f.write(storyName + "\r\n")
        f.write("Total words used: " + str(totalWords) + "\r\n")
        f.write("Total unique words: " + str(uniqueWords) + "\r\n")
        f.write("-----MOST USED WORDS------\r\n")
        for i in range(len(mostUsed)):
            f.write(str(mostUsed[i][0]) + ":" + str(mostUsed[i][1]) + "\r\n")
        f.write("-----LEAST USED WORDS------\r\n")
        for i in range(len(leastUsed)):
            f.write(str(leastUsed[i][0]) + ":" + str(leastUsed[i][1]) + "\r\n")
        f.write("------ONE USE WORDS------\r\n")
        for i in range(len(oneUse)):
            f.write(oneUse[i][0] + ":" + str(oneUse[i][1]) + "\r\n")
        f.close()

def getTotalWords(words):
    totalWordsUsed = 0
    for i in range(len(words)):
        totalWordsUsed = totalWordsUsed + words[i][1]
    return totalWordsUsed

def getLists(words):
    #words = hpl_utils.mergeSortNumeric(words)
    words = sorted(words , key=lambda value:value[1])
    leastUsed = words[0:25]
    mostUsed = words[len(words)-25:]
    mostUsed.reverse()
    # create list of one use words
    index = 0
    sentinel = True
    while(sentinel):
        if(words[index][1] > 1):
            sentinel = False
        index = index + 1
    oneUseList = words[0:index]
    oneUseList = sorted(oneUseList , key=lambda value:value[0])
    return leastUsed, mostUsed, oneUseList

# test just on call of cthulhu

# do this shit for each story
for fileName in os.listdir("./texts"):
    analyzeText(fileName)
