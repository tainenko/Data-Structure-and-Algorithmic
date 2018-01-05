# Uses python3
import sys

def get_change(m):
    #write your code here
    count=0
    if m>=10:
        count+=m//10
        m=m%10
    if m >= 5:
        count += m // 5
        m = m % 5
    if m >= 1:
        count += m
        m = 0
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
