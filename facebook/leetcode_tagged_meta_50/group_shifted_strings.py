class Solution():
    def groupShiftedStrings(string, right_shift):
        result = ""
        for char in string:
            if char.isLower():
                result += chr((char - 'a')%26 + 'a')
            elif char.isUpper():
                result += chr((char - 'A')%26 + 'A')
            elif char.isDigit():
                result += chr((char - 45)%10 + '0')
            else:
                result += char  
        return result