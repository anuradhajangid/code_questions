from typing import List

class Solution:
    def countBits_2(self, n: int) -> List[int]:
        #[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,3,4,1,2,2,3,2,3,3,4,]
        output = [0] * (n+1)
        for i in range (1, n+1):
            output[i] = output[i>> 1] + (i & 1)
        return output

    def countBits(self, n: int) -> List[int]:
        #[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,3,4,1,2,2,3,2,3,3,4,]
        output = [0] * (n+1)
        offset = 1
        for i in range (1, n+1):
            if offset * 2  == i:
                offset *= 2
            output[i] = output[i - offset] + 1
        return output

        