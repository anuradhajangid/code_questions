from heapq import *
class MedianOfStream:
  def __init__(self):
    self.max_small_num = []
    self.min_large_num = []

  def insert_num(self, num):
    if not self.max_small_num or -self.max_small_num[0] >= num:
        heappush(self.max_small_num, -num)
    else:
        heappush(self.min_large_num, num)
    if len(self.max_small_num) > len(self.min_large_num) + 1:
        heappush(self.min_large_num, -heappop(self.max_small_num))
    elif len(self.max_small_num) < len(self.min_large_num):
        heappush(self.max_small_num, -heappop(self.min_large_num))

  def find_median(self):
    if len(self.max_small_num) == len(self.min_large_num):
        return -self.max_small_num[0] / 2.0 + self.min_large_num[0] / 2.0
    return -self.max_small_num[0] / 1.0


median = MedianOfStream()
for num in [35, 22, 30, 25, 1]:
    median.insert_num(num)
print(median.find_median())


