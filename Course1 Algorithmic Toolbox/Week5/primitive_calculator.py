# Uses python3
import sys
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dynamic_sequence(n):
    sequence=[]
    a=[0]*(n+1)
    #build a reach table from zero to number n
    #we have three operation methods:
    #-add 1
    #-times 2
    #-times 3
    #for each i-th element we have to find the minimun steps from( i-1)th element
    #which means we chose the minimun from (i-1)th element add 1, (i/2)th element times 2 and (i/3)th element times 3
    #all of them add the steps by 1
    for i in range(1,len(a)):
        a[i]=a[i-1]+1
        if i % 2 == 0:
            a[i]=a[i//2]+1 if a[i//2] < a[i-1] else a[i-1]+1
        if i % 3 == 0:
            a[i]=a[i//3]+1 if a[i//3] < a[i-1] else a[i-1]+1
    while n>0:
        sequence.append(n)
        if a[n - 1] == a[n] - 1:
            n = n - 1
        elif n % 2 == 0 and a[n // 2] == a[n] - 1:
            n = n // 2
        elif n % 3 == 0 and a[n // 3] == a[n] - 1:
            n = n // 3
    return reversed(sequence)




input = sys.stdin.read()
n = int(input)
sequence = list(dynamic_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
