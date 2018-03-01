# python3
import sys

NA = -1
class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.patternEnd = False

def build_trie(patterns):
    tree = dict()
    tree[0]={}
    index=0
    for pattern in patterns:
        current=tree[0]
        for letter in pattern:
            if letter in current.keys():
                current=tree[current[letter]]
            else:
                index += 1
                current[letter]=index
                tree[index]={}
                current=tree[index]
        if index:
            current['leaf']=True
    return tree

def prefix_trie_match(text,trie):
    index=0
    letter=text[index]
    current=trie[0]
    while True:
        if "leaf" in current:
            return True
        elif not current:
            return True
        elif letter in current.keys():
            current=trie[current[letter]]
            index+=1
            if index <len(text):
                letter=text[index]
            else:
                letter='$'
        else:
            return False

def solve (text, n, patterns):
	result = []
	# write your code here
	trie = build_trie(patterns)
	for i in range(len(text)):
		if prefix_trie_match(text[i:], trie):
			result.append(i)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
