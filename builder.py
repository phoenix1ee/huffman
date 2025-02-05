#Shun Fai Lee Lab3
from huffman.lab3class import PQ
from huffman.lab3class import Htree
from huffman.helper2 import tablereader
from huffman.helper2 import tablechecker

#method: build an array of nodes, check the nodes, then push into the queue direct
def build(in_file, out_file):
    HuffQ = PQ()
    tablereader(in_file, HuffQ)
    HuffQ.sort("a")
    if not tablechecker(HuffQ.pq):
        return
    HuffQ.sort("huff")
    Hufftree = Htree()
    Hufftree.buildtree(HuffQ)
    out_file.write("The Tree order is ")
    out_file.write(Hufftree.traverse(Hufftree.root) + "\n" + "\n")
    out_file.write("The code is ")

    Hufftree.buildcode(Hufftree.root, "")

    for x in Hufftree.codetable:
        out_file.write(f'{x.key}: {x.fq}, ')
    out_file.write("\n" + "\n")

    Hufftree.sort("a")
    return Hufftree