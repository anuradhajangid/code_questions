class InvalidNumber(Exception):
    def __init__(self, message):
        super().__init__(message)

def valid_word_abbreviation(word, abbr):
    word = list(word)
    abbr = list(abbr)
    wp = 0
    lwp = len(word)-1
    ap=0
    lap = len(abbr)-1
    def get_number(abbr, start):
        if not abbr[start].isnumeric():
            return 0, start
        number = 0
        while start < len(abbr) and abbr[start].isnumeric():
            if int(abbr[start]) == 0 and number ==0:
                raise InvalidNumber("Incorrect number")
            number = number * 10 + int(abbr[start])
            start += 1
        return number, start
    while ap <= lap and wp <= lwp:
        try:
            number, ap = get_number(abbr, ap)
        except InvalidNumber as err:
            return False
        wp += number
        if lwp - wp + 1 < 0 or ( wp <=lwp and abbr[ap] != word[wp]):
            return False
        ap+=1
        wp+=1
    if wp <= lwp or ap <= lap:
        return False

    # Replace the following return statement with your code
    return True


assert valid_word_abbreviation("internationalization", "13iz4n")
assert valid_word_abbreviation("helloworld", "4orworld") == False
assert valid_word_abbreviation("minimum", "min2um")
assert valid_word_abbreviation("computation" , "compu03on") == False
assert valid_word_abbreviation("h" , "1")

#Time complexity = O(N)
#Space Complexity = O(1)