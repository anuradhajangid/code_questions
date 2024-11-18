def calculate_sum_square(num):
    sq = 0
    while num > 0:
        sq += int(num % 10) ** 2
        num = int(num/10)
    return sq

def is_happy_number(n):

    slow = n
    fast = n
    while fast != 1:
        slow = calculate_sum_square(slow)
        fast = calculate_sum_square(calculate_sum_square(fast))
        if fast == slow:
            return False
    return True

assert is_happy_number(4) == False
assert is_happy_number(28) == True

#Timcomplexity
#Space complexity = O(1)