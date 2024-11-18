import re
def reverse_words(inpstring):
    inpstring = re.sub(' +', ' ', inpstring.strip())
    def sub_reverse(tstring, start=None, end=None):
        start = 0 if start is None else start
        end = len(tstring) - 1 if end is None else end
        while start < end:
            tstring[start], tstring[end] = tstring[end], tstring[start]
            start += 1
            end -= 1
    inpstring = list(inpstring)
    sub_reverse(inpstring)
    start = 0
    end = 0
    while end < len(inpstring):
        if inpstring[end] == " " and start != end:
            sub_reverse(inpstring, start, end-1)
            end += 1
            start = end
            continue
        if end == len(inpstring) -1:
            sub_reverse(inpstring, start, end)
            end += 1
            continue
        end += 1
    return "".join(inpstring)

    

assert reverse_words("The quick brown fox jumped over a lazy dog") == "dog lazy a over jumped fox brown quick The"
assert reverse_words("We love Python ") == "Python love We"
# Can there be multiple space seperated strings?