#https://leetcode.com/problems/valid-word-abbreviation?envType=problem-list-v2&envId=7p59281
class Solution:
    def validAbbreviation(self, input_string:str, abbreviation:str) -> bool:
        i = 0
        j = 0
        number = 0
        while i < len(input_string) and j < len(abbreviation):
            if abbreviation[j].isdigit():
                number += number * 10 + int(abbreviation[j])
                if number ==0:
                    break
                j += 1
            else:
                i += number
                if i >= len(input_string) or abbreviation[j] != input_string[i]:
                    return False
                i += 1
                j += 1
                number = 0
        i += number
        return i == len(input_string) and j == len(abbreviation)
                