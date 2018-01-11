# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    inbag=[0]*(W+1)
    for i in range(len(w)):
        for j in range(W, w[i]-1, -1):
            inbag[j] = max(inbag[j], inbag[j - w[i]] + w[i])
    return inbag[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
