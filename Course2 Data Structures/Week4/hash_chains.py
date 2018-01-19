# python3
import sys
from collections import deque

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [deque() for i in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_chain(self, chain):
        if chain:
            print(' '.join(chain))
        else:
            print()

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.elems[query.ind])
            return

        s = query.s
        h = self._hash_func(s)
        #print(h, self.elems[h])
        if query.type == "find":
            print(self.find(query.s, h))
        elif query.type == "add":
            if self.find(query.s, h) == 'no':
                self.elems[h].appendleft(s)
        else:
            try:
                self.elems[h].remove(s)
            except:
                pass

    def find(self, s, h):
        if s in self.elems[h]:
            return 'yes'
        else:
            return 'no'


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
