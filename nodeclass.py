#Shun Fai Lee Lab3
class H_node:
    def __init__(self, in_k: str, in_f: str):
        """
        This class is used to hold a/a group of character and its frequency and function as a node
        """
        self.key = in_k
        self.fq = in_f
        self.left = None
        self.right = None