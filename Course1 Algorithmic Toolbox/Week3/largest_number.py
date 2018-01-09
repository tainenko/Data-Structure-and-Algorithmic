#Uses python3

import sys
from functools import cmp_to_key

def largest_number(a):
    #write your code here
    res=""
    a.sort(key=cmp_to_key(lambda x,y: int(y+x)-int(x+y)))
    return '0' if a[0] == '0' else ''.join(x for x in a)
    '''
    m = len(max(a, key=len))
    newlist=[(i,i+i[-1]*(m-len(i)))for i in a]
    newlist.sort(key=lambda k:k[1], reverse=True)

    res=''.join((k[0] for k in newlist))
    return res
    '''


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
