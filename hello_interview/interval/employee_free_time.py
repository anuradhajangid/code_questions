class Solution:
    def employeeFreeTime(self, intervals: list):
        flatten  = [i for employee in intervals for i in employee]
        flatten.sort(key=lambda x: x[0])
        merged = []
        for i in range (len(flatten)):
            if not merged or merged[-1][1] < flatten[i][0]:
                merged.append(flatten[i])
            else:
                merged[-1][1] = max(merged[-1][1], flatten[i][1])
                merged[-1][0] = min(merged[-1][0], flatten[i][0])
        free_time = []
        for i in range(1, len(merged)):
            free_time.append([merged[i-1][1], merged[i][0]])
        return free_time

assert Solution().employeeFreeTime([[[2,4],[7,10]],[[1,5]],[[6,9]]]) == [[5,6]]