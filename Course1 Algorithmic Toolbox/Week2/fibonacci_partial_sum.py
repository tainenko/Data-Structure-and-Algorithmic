# Uses python3
import sys
def get_fibonacci_last_digit(n):
    m=10
    # Initialize a matrix [[1,1],[1,0]]
    v1, v2, v3 = 1, 1, 0
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2
def fibonacci_sum(n):
    sum=get_fibonacci_last_digit(n+2)-1
    if n<=2:
        return n
    return sum if sum >=0 else sum+10
def fibonacci_partial_sum(from_, to):
    sum_partial=fibonacci_sum(to)-fibonacci_sum(from_-1)
    return sum_partial if sum_partial>=0 else sum_partial+10
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))