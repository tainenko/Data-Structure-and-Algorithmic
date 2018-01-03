# Uses python3
import sys

def gcd_naive(a, b):
    while b!=0:
        a=a%b
        if a==0:
            break
        b=b%a
    current_gcd =a if a!=0 else b
    return current_gcd
def lcm_naive(a, b):
    gcd=(gcd_naive(a,b))
    lcm=gcd*(a//gcd)*(b//gcd)
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

