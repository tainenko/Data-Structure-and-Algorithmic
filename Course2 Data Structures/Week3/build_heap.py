# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def AdvancedSwaps(self):
      for i in range(len(self._data) , -1, -1):
          self.Siftdown(i)

#Siftdown: compare the value between parent (i) ,left.child(2i+1) and right.child(2*i+2)
#(if the root of tree is started from 1, the child would be 2i(left) and 2i+1(right))
#if the left.child or right.child is larger than parent, swap them.
  def Siftdown(self,i):
      index=i
      left=2*i+1
      right=2*i+2
      if left < len(self._data) and self._data[left] < self._data[index]:
          index=left
      if right < len(self._data) and self._data[right] < self._data[index]:
          index=right
      if index != i:
          self._swaps.append((i, index))
          self._data[i], self._data[index] = self._data[index], self._data[i]
          self.Siftdown(index)




  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def Solve(self):
    self.ReadData()
    #self.GenerateSwaps()
    self.AdvancedSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
