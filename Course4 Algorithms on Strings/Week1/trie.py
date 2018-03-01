#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    #create root node of trie
    tree[0]={}
    index=0

    for pattern in patterns:
        #traverse the trie from root node
        current=tree[0]
        for letter in pattern:
        #find whether the letter already exist or not
        #if True, keep going traversing the trie
            if letter in current.keys():
                current=tree[current[letter]]

        #else, create a new node  and add it to the trie
        #also chang the reference  to the new node from previous
            else:
                index += 1
                current[letter]=index
                tree[index]={}
                current=tree[index]

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
