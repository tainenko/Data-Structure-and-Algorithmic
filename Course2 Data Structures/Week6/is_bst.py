#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

result=[]
root_index=0

def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if not tree:
        return True
    inorder_trie=inOrder(tree)
    for i in range(len(inorder_trie)-1):
        if i<root_index and  inorder_trie[i] >=inorder_trie[i+1]:
            return False
        elif i >= root_index and inorder_trie[i] > inorder_trie[i+1]:
            return False
    return True

def inOrder(tree):
    rec_inOrder(0, tree)
    return result

def rec_inOrder(index,tree):
    global root_index
    if tree[index][1] != -1:
          rec_inOrder(tree[index][1],tree)
    result.append(tree[index][0])
    if index == 0:
        root_index = (len(result)-1)
    if tree[index][2] != -1:
        rec_inOrder(tree[index][2],tree)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
