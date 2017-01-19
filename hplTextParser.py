import chardet # used to determine the charset used in the text file
import codecs # this is needed because the stuff we pulled was utf-8

# the below can be used to detect the encoding
dic = chardet.detect(f)
print(dic['encoding'])

# get the string that holds all the words in the file
text = codecs.open("./texts/callofcthulhu.txt" , "r" , encoding='utf-8').read()

# read in words, word by word
words = text.split()

# format words as all lowercase and remove trailing punctuation
for i in range(len(words)):
    words[i] = words[i].rstrip(".,;")
    words[i] = words[i].lower()
     

# tally the words in frequency
wordCount = {}

for i in range(len(words)):
    if(words[i] in wordCount):
        wordCount[words[i]] = wordCount[words[i]] + 1
    else:
        wordCount[words[i]] = 1

# store dictionary as a list for sorting
analysis = list(wordCount.items())

# sort analysis alphabetically
for i in range(1 , len(analysis)):
    index = i
    while(index > 0 and not (analysis[index][0] > analysis[index - 1][0])):
        tmp = analysis[index]
        analysis[index] = analysis[index - 1]
        analysis[index - 1] = tmp
        index = index - 1

print("alphebetized word distribution")
for i in range(len(analysis)):
    print(analysis[i][0] , ":" , analysis[i][1])

for i in range(1 , len(analysis)):
    index = i
    while(index > 0 and not (analysis[index][1] < analysis[index - 1][1])):
        tmp = analysis[index]
        analysis[index] = analysis[index - 1]
        analysis[index - 1] = tmp
        index = index - 1
print("numberical word distribution")
for i in range(len(analysis)):
    print(analysis[i][1] , ":" , analysis[i][0])
