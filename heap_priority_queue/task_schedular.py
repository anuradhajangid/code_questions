# https://leetcode.com/problems/task-scheduler/
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        charfreq = [0] * 26
        for char in tasks:
            charfreq[ord(char) - ord("A")] += 1

        charfreq.sort()
        maxfreq = charfreq[25] -1
        max_idle_slots = maxfreq * n

        for i in range(24, -1, -1):
            if charfreq[i] > 0:
                max_idle_slots -= min(maxfreq, charfreq[i])
        return max_idle_slots + len(tasks) if max_idle_slots > 0 else len(tasks)
        
print(Solution().leastInterval(["A","A", "B", "C", "D", "E", "F"],2))
        