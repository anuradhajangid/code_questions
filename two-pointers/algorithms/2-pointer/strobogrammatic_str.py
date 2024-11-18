def is_strobogrammatic(num):
    num_map = {
        "1":"1",
        "8":'8',
        '0':'0',
        '6':'9',
        '9':'6'
    }
    start = 0
    end = len(num) -1
    while start <= end:
        if num[start] not in num_map or num[end] not in num_map:
            return False
        if num_map[num[start]] != num[end]:
            return False
        start += 1
        end -= 1
    return True

assert is_strobogrammatic("101") == True
assert is_strobogrammatic("808") == True
assert is_strobogrammatic("86098") == True
assert is_strobogrammatic("6710179") == False
assert is_strobogrammatic("818") == True
assert is_strobogrammatic("961196116996889696888896968888969688966911961196") == True

#Timecomplexity: O(N) + O(N/2) =  O(N)
#SpaceComplexity: O(2) = O(1)