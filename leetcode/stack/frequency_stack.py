#https://leetcode.com/problems/maximum-frequency-stack/description/

from collections import defaultdict, deque


class FreqStack:
    def __init__(self):
        self.data = defaultdict(list)
        self.freqmap = defaultdict(int)
        self.maxfreq = 0


    def push(self, val: int) -> None:
        self.freqmap[val] += 1
        if self.freqmap[val] > self.maxfreq:
            self.maxfreq = self.freqmap[val]
        self.data[self.freqmap[val]].append(val)
        

    def pop(self) -> int:
        item = self.data[self.maxfreq].pop()
        self.freqmap[item] -= 1
        if not self.data[self.maxfreq]:
            self.maxfreq -= 1
        return item

freqStack = FreqStack()
assert freqStack.push(5) == None
assert freqStack.push(7) == None
assert freqStack.push(5) == None
assert freqStack.push(7) == None
assert freqStack.push(4) == None
assert freqStack.push(5) == None
assert freqStack.pop() == 5
assert freqStack.pop() == 7
assert freqStack.pop() ==5   
assert freqStack.pop() ==4 

            



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()