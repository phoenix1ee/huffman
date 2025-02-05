#Shun Fai Lee Lab3
from huffman.nodeclass import H_node
from huffman.helper import combine
from huffman.quicksort import quicksort

class PQ:
    def __init__(self):
        """
        This class implement a priority queue of nodes for building huffman tree
        """
        self.pq = []
        self.size = 0

    def push(self, innode: H_node):
        """
        append a node into priority queue without concerning priority
        :param innode: the input node
        """
        self.pq.append(innode)
        self.size +=1

    def sort(self, mode: str):
        """
        accept a pass in parameter to sort the private queue inside the object
        :param mode: parameters for controlling sort logic, "huff"->huffman tree logic, any others ->alphabetical logic
        """
        quicksort(self.pq,0,self.size-1, mode)

    def pop(self) -> H_node:
        """
        pop the node with the highest priority, by design, the 1st item in the list
        :return: a H_node object
        """
        if self.size <= 0:
            raise Exception("queue is empty")
        else:
            self.size -= 1
            return self.pq.pop(0)

    def len(self) -> int:
        """
        Determines the number of elements the stack currently have
        :return: an int value
        """
        return len(self.pq)

class Htree:
    def __init__(self):
        """
        This class is used to hold a huffman tree
        """
        self.root = None
        self.current = None
        self.codetable = []

    def buildtree(self, q: PQ):
        """
        take an input of priority queue and build a huffman tree
        :param q: a priority queue under the PQ object
        """
        while q.len()>1:
            temp_l = q.pop()
            temp_r = q.pop()
            temp_p = combine(temp_l, temp_r)
            temp_p.left = temp_l
            temp_p.right = temp_r
            q.push(temp_p)
            q.sort("huff")
        self.root = q.pop()

    def traverse(self, curr):
        """
        take an input of a node and perform a preorder traversal to itself and all child nodes
        :param curr: a node under the Huffman Tree
        """
        output = ""
        if curr:
            #print(f'{curr.key}: {curr.fq}, ', end="")
            output = output + curr.key + ": " + curr.fq + ", "
            if curr.left:
                output = output + self.traverse(curr.left)
            if curr.right:
                output = output + self.traverse(curr.right)
            return output
        else:
            print("the Tree is empty, please run 'Htree'.buildtree('queue') to build the tree first")
            return

    def buildcode(self, curr, prefix):
        """
        Build an array of H_node for storing the code and return nothing
        :param curr: a node from the Huffman Tree, typically the root node
        :param prefix: the initial prefix for the code, typically "" at the initial call
        """
        if (not curr.left) and (not curr.right):
            temp = H_node(curr.key, prefix)
            self.codetable.append(temp)
            return
        else:
            self.buildcode(curr.left, prefix + "0")
            self.buildcode(curr.right, prefix + "1")

    def sort(self, mode: str):
        quicksort(self.codetable,0,len(self.codetable)-1, mode)

    def encode2(self, index: int):
        """
        For use when code table is an array of H_nodes
        Return the corresponding code with an index
        :param index: an input character
        """
        return self.codetable[index].fq


    def finds(self, in_k: str, start: int, end: int) -> int:
        """
        use recursive binary search to find and locate the position a key value inside the encode table
        :param in_k: the input key
        :param start: the start index
        :param end: the end index
        :return: an int value
        """
        if end >= start:
            mid = (start + end) // 2
            #base case: only 1 item remains
            if in_k == self.codetable[mid].key:
                return mid
            #recursive case:
            else:
                if in_k < self.codetable[mid].key:
                    return self.finds(in_k, start, mid-1)
                else:
                    return self.finds(in_k, mid + 1, end)
        else:
            return -1

    def decode(self, in_s: str):
        """
        Take a stream of input string and Return the decoded characters
        :param in_s: input string
        """
        temp = self.root
        output = ""
        for b in in_s:
            if temp.left and temp.right:
                if b == "0":
                    temp = temp.left
                else:
                    temp = temp.right
            if (not temp.left) and (not temp.right):
                output += temp.key
                temp = self.root
        if temp != self.root:
            return "{corrupted line~decoded failed}"
        else:
            if len(output) == 0:
                return "{empty line}"
            else:
                return output