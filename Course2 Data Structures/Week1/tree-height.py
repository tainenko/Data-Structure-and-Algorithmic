# python3

import sys,threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

"""Compute the  height of a given tree.
   the definition about "Height of a  tree" 
   is the maximum depth of a node, or the maximum  distance from a leaf to the root.
   Examples:
   >>> tree = TreeHeight()
   >>> tree.n = 5
   >>> tree.parent = [4, -1, 4, 1, 1]
   >>> tree.compute_height()
   3
   >>> # Explanation:
   >>> # The input means that there are 5 nodes with numbers from 0 to 4.
   >>> # The parent list indicate the parent of current node.
   >>> #  tree.nodes  = [0, 1, 2 , 3, 4] 
   >>> #  tree.parent = [4, -1, 4, 1, 1]
   >>> # In this case:
   >>> # node 0 is a child of node 4, node 1 is the root, node 2 is a child of
   >>> # node 4, node 3 is a child of node 1 and node 4 is a child of node 1.
   >>> #
   >>> #       root
   >>> #          1
   >>> #        /   \
   >>> #       3    4
   >>> #            /  \
   >>> #          0    2
   >>> #
   >>> tree = TreeHeight()
   >>> tree.n = 5
   >>> tree.parent = [-1, 0, 4, 0, 3]
   >>> tree.compute_height()
   4
   >>> # Explanation:
   >>> # The input means that there are 5 nodes with numbers from 0 to 4,
   >>> # node 0 is the root, node 1 is a child of node 0, node 2 is a child of
   >>> # node 4, node 3 is a child of node 0 and node 4 is a child of node 3.
   >>> #
   >>> #       root
   >>> #         0 
   >>> #        /  \
   >>> #       1   3
   >>> #             |
   >>> #            4
   >>> #             |
   >>> #             2
   """
class TreeHeight:
    def __init__(self):
        self.n=0
        self.parents=[]

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parents = list(map(int, sys.stdin.readline().split()))
        self.heights=[None]*self.n
        self.maxHeight=0

    def compute_height(self,index):
        height=self.heights[index]
        if height is not None:
            return height
        parent=self.parents[index]
        if parent == -1:
            height=1
        else:
            height=self.compute_height(parent)+1
            self.heights[index]=height
        return height

    def max_height(self):
        if self.maxHeight==0:
            for index, parent in enumerate(self.parents):
                depth =self.compute_height(index)
                if self.maxHeight<depth:
                    self.maxHeight=depth
        return self.maxHeight




def main():
  tree = TreeHeight()
  tree.read()
  print(tree.max_height())

threading.Thread(target=main).start()