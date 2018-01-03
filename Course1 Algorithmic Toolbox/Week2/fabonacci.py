# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    n_1=0
    n_2=1
    for i in range(0,n-1):
        result=n_1+n_2
        n_1=n_2
        n_2=result
    return result

n = int(input())
print(calc_fib(n))
