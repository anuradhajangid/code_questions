from typing import List
import collections
#https://leetcode.com/problems/detect-squares/description/
class DetectSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1
        

    def count(self, point: List[int]) -> int:
        count = 0
        x, y = point

        for (xt, yt), n in self.points.items():
            x_dist, y_dist = abs(x-xt), abs(y - yt)
            if x_dist == y_dist and x_dist > 0:
                c1 = (x, yt)
                c2 = (xt, y)
                if c1 in self.points and c2 in self.points:
                    count += n * self.points[c1] * self.points[c2]
        return count
                    
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
    


                    
        


# Your DetectSquares object will be instantiated and called as such:
# "add","add","add","count","count","add","count"
# [[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]
obj = DetectSquares()
obj.add([3,10])
obj.add([11,2])
obj.add([3,2])
print(obj.count([11,10]))
print(obj.count([14,8]))
obj.add([11,2])
print(obj.count([11,10]))