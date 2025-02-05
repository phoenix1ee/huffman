#Shun Fai Lee Lab3
from huffman.nodeclass import H_node

def minalpha(s1: str) -> str:
    """
    find the lowest letter in the input string
    :param s1: the input string
    :return: the lowest letter of the input string
    """
    temp_c = s1[0].upper()
    for i in range(1, len(s1)):
        if s1[i] < temp_c:
            temp_c = s1[i].upper()
    return temp_c

def priority(a: H_node, b: H_node, mode = "huff") -> bool:
    """
    determine if the 1st H_node has higher priority then 2nd H_node, contain two modes
    by design, there won't be node of equal priority because there would not be any node containing the same alphabet
    default: mode = "huff" check priority according to huffman tree logic
    alternative: mode = any other values. check priority according to only alphabetical order
    :param a: the 1st input node
    :param b: the 2nd input node
    :param mode: toggle the mode of priority checking, "huff" or any other
    :return: boolean value, True if 1st H_node has priority > 2nd H_node, otherwise false
    """
    if mode == "huff":
        if int(a.fq) < int(b.fq):
            return True
        elif int(a.fq) > int(b.fq):
            return False
        else:
            if len(a.key) == 1 and len(b.key) > 1:
                return True
            elif len(b.key) == 1 and len(a.key) > 1:
                return False
            else:
                if minalpha(a.key) < minalpha(b.key):
                    return True
                else:
                    return False
    else:
        if a.key < b.key:
            return True
        else:
            return False

def combine(a: H_node, b: H_node) -> H_node:
    """
    take 2 nodes as input and return a combined node according
    :param a: the node from the left child
    :param b: the node from the right child
    """
    temp_c = a.key+b.key
    temp_f = int(a.fq)+int(b.fq)
    return H_node(temp_c,str(temp_f))
