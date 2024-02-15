#https://www.educative.io/courses/grokking-coding-interview-patterns-python/restore-ip-addresses
def restore_ip_addresses(s):
    result = []
    segments = []
    backtrack(s, -1, 3, segments, result)
    return result

def backtrack(s, predot, dots, segments, result):
    size = len(s)
    for currdot in range(predot+1,min(size-1,predot+4)):
        segment = s[predot+1:currdot+1]
        if isValid(segment):
            segments.append(segment)
            if dots-1==0:
                updateSegments(s, currdot, segments, result)
            else:
                backtrack(s,currdot,dots-1,segments, result)
            segments.pop()

def isValid(segment):
    if int(segment) <= 255:
        return True
    return False


def updateSegments(s,currdot,segments, results):
    segment = s[currdot+1:]
    if isValid(segment):
        segments.append(segment)
        results.append(".".join(segments))
        segments.pop()

# driver code
def main():
    ip_addresses = ["0000", "25525511135", "12121212",
                    "113242124", "199219239", "121212", "25525511335"]

    for i in range(len(ip_addresses)):
        print(i + 1, ".\t Input addresses: '", ip_addresses[i], "'", sep="")
        print("\t Possible valid IP Addresses are: ",
              restore_ip_addresses(ip_addresses[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()