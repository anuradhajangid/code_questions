#https://leetcode.com/problems/time-based-key-value-store/description/
class TimeMap:

    def __init__(self):
        self.keymap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keymap:
            self.keymap[key] = [[value,timestamp]]
        else:
            self.keymap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        val = ""
        if key not in self.keymap:
            return val
        temp = self.keymap.get(key, [])
        start, end = 0, len(temp)-1
        while start <= end:
            mid = (start + end)//2
            if temp[mid][1] <=timestamp:
                val = temp[mid][0]
                start = mid + 1
            else:
                end = mid - 1
        return val

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("love","high",10)
obj.set("love","low",20)
param_2 = obj.get("love", 20)
param_2 = obj.get("love", 5)
param_2 = obj.get("love", 10)
param_2 = obj.get("love", 15)
param_2 = obj.get("love", 20)
param_2 = obj.get("love", 25)
