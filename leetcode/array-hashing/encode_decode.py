#https://leetcode.com/problems/encode-and-decode-strings/description/
from typing import List

class Codec:
    def __init__(self):
        pass

    def encode(self, strlist: List[str]) -> str:
        result = ""
        for word in strlist:
            result += str(len(word)) + "#" + word
        return result
    
    def decode(self, encoded: str) -> List[str]:
        result = []
        i = 0

        while i < len(encoded):
            j = i
            while encoded[j] != "#":
                j +=1
            wordlen = int(encoded[i:j])
            result.append(encoded[j+1 : j+1+wordlen])
            i = j+1+wordlen
        return result
codec = Codec()
assert codec.decode(codec.encode(["Hi", "how", "are", "you!"])) == ["Hi", "how", "are", "you!"]