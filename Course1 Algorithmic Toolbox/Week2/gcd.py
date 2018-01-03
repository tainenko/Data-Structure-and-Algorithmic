# Uses python3
import sys

def gcd_naive(a, b):
    while b!=0:
        a=a%b
        if a==0:
            break
        b=b%a
    if a==0:
        current_gcd=b
    else:
        current_gcd=a
    return current_gcd


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
