# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort()
    previous =segments[0]

    for segment in segments[1:]:
        current=list(range(segment.start,segment.end+1))
        if intersect(previous , current) :
            previous = intersect(previous, current)
        else:
            points.append(previous[-1])
            previous = current

    if intersect(previous, current):
        points.append(previous[-1])
return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
