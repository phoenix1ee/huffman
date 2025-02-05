#Shun Fai Lee Lab3
from huffman.nodeclass import H_node
from huffman.lab3class import PQ

def tablereader(input_f: input, in_Q: PQ):
    """
    Read from the input file object and Output an array of H_nodes
    ignoring all spaces and escape character "\t"
    :argument: in_path :a file object which contain some expression
    :return: an array of nodes
    """
    for line in input_f:
        in_c = line.strip().replace(" ", "")
        if in_c:
            delimiter = in_c.find("-")
            if delimiter > 0:
                temp_c = in_c[0:delimiter]
                temp_f = in_c[delimiter+1:]
            #if temp_c.isalpha() and temp_f.isnumeric():
                in_Q.push(H_node(temp_c.upper(),temp_f))
            else:
                in_Q.push(H_node("please refers", in_c))

def tablechecker(in_list: list):
    """
    for an array of H_nodes, determine if the input frequency table list is legitimate
    the table list is sorted before input
    : input in the form of "key - frequency"
    : each key is single
    : free of duplicates
    : each frequency is numeric
    :param in_list: the list of alphabets read from frequency table
    """
    l = len(in_list)
        #print("input frequency file do not contain all 26 alphabets")
    for i in range(l):
        if i == 0:
            if not in_list[i].fq.isnumeric() or not len(in_list[i].key) == 1:
                print(f'detected invalid input [{in_list[i].key}: {in_list[i].fq}]')
                return False
        elif i > 0:
            if not in_list[i].fq.isnumeric() or not len(in_list[i].key) == 1 or in_list[i].key == in_list[i-1].key:
                print(f'detected invalid input [{in_list[i].key}: {in_list[i].fq}]')
                return False
    return True