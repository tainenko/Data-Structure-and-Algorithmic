# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a.sort()
result = a[n-1]*a[n-2]
print(result)