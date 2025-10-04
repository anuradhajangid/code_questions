class Solution:
    def __init__(self):
        self.map = {}
    def shouldPrintMessage(self, timestamp:int, message: str):
        if message not in map:
            self.map[message] = 10
            return True
        if timestamp - self.map[message] >= 10:
            self.map[message] = timestamp
            return True
        return False

