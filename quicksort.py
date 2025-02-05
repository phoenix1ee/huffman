#Shun Fai Lee Lab3
from huffman.helper import priority

def partitiion(ndlist: list, lowid, hid, mode = "a"):
    """
    the partition function for use by quicksort function, contain two modes
    default: mode = "a", suppose the list contains nodes of single alphabet, sort by alphabetical order
    alternative: mode = "huff" suppose the list contains nodes of huffman tree, sort by huffman tree logic
    :param ndlist: the list to be sorted
    :param lowid: the starting index of partitioning
    :param hid: the end index of partitioning
    :param mode: the parameter to toggle default or alternative mode, input "huff" for huffman tree logic
    :return: nothing
    """
    mid = lowid + (hid - lowid)//2
    pivot = ndlist[mid]
    finish  = False
    while not finish:
        while priority(ndlist[lowid],pivot,mode):
            lowid+=1
        while priority(pivot,ndlist[hid],mode):
            hid -= 1
        if lowid >= hid:
            finish = True
        else:
            temp = ndlist[lowid]
            ndlist[lowid] = ndlist[hid]
            ndlist[hid] = temp
            lowid +=1
            hid-=1
    return hid

def quicksort(target: list, low, high, mode = "a"):
    """
    sort the input list of nodes, contain two modes
    default: mode = "a", suppose the list contains nodes of single alphabet, sort by alphabetical order
    alternative: mode = "huff" suppose the list contains nodes of huffman tree, sort by huffman tree logic
    :param target: the list to be sorted
    :param low: the starting index of sorting
    :param high: the end index of sorting
    :param mode: the parameter to toggle default or alternative mode, input "huff" for huffman tree logic
    :return: nothing
    """
    if low >= high:
        return
    new = partitiion(target, low, high, mode)
    quicksort(target,low,new, mode)
    quicksort(target, new+1, high, mode)