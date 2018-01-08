# Uses python3
import sys
import numpy as np
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    winbag=0.

    value_weight = values/weights

    sortindex=value_weight.argsort()[::-1]
    value_weight=value_weight[sortindex]
    weights=weights[sortindex]
    values=values[sortindex]

    while winbag < capacity:
        if len(weights)==0:
            break
        if weights[0] <= capacity-winbag:
            winbag+=weights[0]
            value+=values[0]

            weights=weights[1:]
            values=values[1:]
        else:
            fraction=(capacity-winbag)/weights[0]
            winbag+=weights[0]*fraction
            value+=values[0]*fraction

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = np.array(data[2:(2 * n + 2):2])
    weights = np.array(data[3:(2 * n + 2):2])
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
