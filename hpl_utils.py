
def mergeSortAlpha(dataList):
    # return the list if it is single element
    if(len(dataList) == 1):
        return dataList
    else:
        half = len(dataList) // 2
        firstHalf = dataList[0:half]
        secondHalf = dataList[half:]
        return mergeLists(mergeSortAlpha(firstHalf) , mergeSortAlpha(secondHalf) , 0)

def mergeSortNumeric(dataList):
    # return the list if it is single element
    if(len(dataList) == 1):
        return dataList
    else:
        half = len(dataList) // 2
        firstHalf = dataList[0:half]
        secondHalf = dataList[half:]
        return mergeLists(mergeSortNumeric(firstHalf) , mergeSortNumeric(secondHalf), 1)


def mergeLists(list1 , list2, crit):
    mergedList = []
    while(len(list1) > 0 and len(list2) > 0 ):
        if(list1[0][crit] < list2[0][crit]):
            mergedList.append(list1.pop(0))
        else:
            mergedList.append(list2.pop(0))
    if(len(list1) > 0):
        while(len(list1) > 0):
            mergedList.append(list1.pop(0))
    if(len(list2) > 0):
        while(len(list2) > 0):
            mergedList.append(list2.pop(0))
    return mergedList

def getOutputFileName(path):
    index = len(path) - 1
    sentinel = True
    while(sentinel and not index < 0):
        if(path[index] != '/'):
            index = index - 1
        else:
            sentinel = False
    storyName = path[index:].lstrip("/")
    storyName = storyName.rstrip(".txt")
    return storyName + "_analysis.txt"

def getStoryName(path):
    index = len(path) - 1
    sentinel = True
    while(sentinel and not index < 0 ):
        if(path[index] != '/'):
            index = index - 1
        else:
            sentinel = False
    storyName = path[index:].lstrip("/")
    storyName = storyName.rstrip(".txt")
    return storyName
    
