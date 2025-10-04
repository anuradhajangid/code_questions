from typing import List
from collections import defaultdict
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def is_within_hour(time1, time2):
            h1, m1 = time1.split(":")
            h2, m2 = time2.split(":")
            if int(h1)+1<int(h2): return False
            if h1==h2: return True
            return m2 <= m1
        
        data = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            data[name].append(time)
        
        result = []
        for person, record in data.items():
            record.sort()
            if any(is_within_hour(t1,t2) for t1,t2 in zip(record, record[2:])):
                result.append(person)
        
        return sorted(result)

assert Solution().alertNames(["daniel","daniel","daniel","luis","luis","luis","luis"], ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]) == ["daniel"]