def find_repeated_sequences(dna, k):
    start = 0
    hashmap = {}
    result = set()
    for i in range(k, len(dna) + 1):
        value=hash(dna[start:i])
        if not value in hashmap:
            hashmap[value] = 1
        else:
            hashmap[value] += 1
            result.add(dna[start:i])
        if i-start >=k:
            start += 1
    return result

assert find_repeated_sequences("AAAAACCCCCAAAAACCCCCC", 8)
assert find_repeated_sequences("CGG" , 1)
assert find_repeated_sequences("GGGGGGGGGGGGGGGGGGGGGGGGG", 9)
assert find_repeated_sequences("TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", 10)
