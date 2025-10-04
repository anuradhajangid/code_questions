#https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-sliding-window-median

from heapq import heappop, heappush, heapify


def median_sliding_window(nums, k):
    medians = []

    outgoing_num = {}

    small_list = []

    large_list = []

    for i in range(0, k):
        heappush(small_list, -1 * nums[i])

    for i in range(0, k//2):
        element = heappop(small_list)
        heappush(large_list, -1 * element)

    balance = 0

    i = k
    while True:
        if (k & 1) == 1:
            medians.append(float(small_list[0] * -1))
        else:
            medians.append((float(small_list[0] * -1) + float(large_list[0])) * 0.5)

        if i >= len(nums):
            break

        out_num = nums[i - k]

        in_num = nums[i]
        i += 1

        if out_num <= (small_list[0] * -1):
            balance -= 1
        else:
            balance += 1

        if out_num in outgoing_num:
            outgoing_num[out_num] = outgoing_num[out_num] + 1
        else:
            outgoing_num[out_num] = 1

        if small_list and in_num <= (small_list[0] * -1):
            balance += 1
            heappush(small_list, in_num * -1)
        else:
            balance -= 1
            heappush(large_list, in_num)

        if balance < 0:
            heappush(small_list, (-1 * large_list[0]))
            heappop(large_list)
        elif balance > 0:
            heappush(large_list, (-1 * small_list[0]))
            heappop(small_list)

        balance = 0

        while (small_list[0] * -1) in outgoing_num and (outgoing_num[(small_list[0] * -1)] > 0):
            outgoing_num[small_list[0] * -1] = outgoing_num[small_list[0] * -1] - 1
            heappop(small_list)

        while large_list and large_list[0] in outgoing_num and (outgoing_num[large_list[0]] > 0):
            outgoing_num[large_list[0]] = outgoing_num[large_list[0]] - 1
            heappop(large_list)

    return medians

# driver code
def main():
    input = (
            ([3, 1, 2, -1, 0, 5, 8],4), 
            ([1, 2], 1), 
            ([4, 7, 2, 21], 2), 
            ([22, 23, 24, 56, 76, 43, 121, 1, 2, 0, 0, 2, 3, 5], 5), 
            ([1, 1, 1, 1, 1], 2))
    x = 1
    for i in input:
        print(x, ".\tInput array: ", i[0],  ", k = ", i[1], sep = "")
        print("\tMedians: ", median_sliding_window(i[0], i[1]), sep = "")
        print(100*"-", "\n", sep = "")
        x += 1


if __name__ == "__main__":
    main()