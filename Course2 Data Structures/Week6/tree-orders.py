# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    self.rec_inOrder(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.result

  def rec_inOrder(self,index):
      if self.left[index] != -1:
          self.rec_inOrder(self.left[index])
      self.result.append(self.key[index])
      if self.right[index] != -1:
          self.rec_inOrder(self.right[index])


  def preOrder(self):
    self.result = []
    self.rec_preOrder(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.result

  def rec_preOrder(self,index):
      self.result.append(self.key[index])
      if self.left[index]!=-1:
          self.rec_preOrder(self.left[index])
      if self.right[index]!=-1:
          self.rec_preOrder(self.right[index])


  def postOrder(self):
    self.result = []
    self.rec_postOrder(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.result

  def rec_postOrder(self,index):
      if self.left[index] != -1:
          self.rec_postOrder(self.left[index])
      if self.right[index] != -1:
          self.rec_postOrder(self.right[index])
      self.result.append(self.key[index])

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
