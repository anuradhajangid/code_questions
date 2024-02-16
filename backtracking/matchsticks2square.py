
def matchstick_to_square(matchsticks):
    matchsticks = sorted(matchsticks,reverse=True)
    totalsum = sum(matchsticks)
    if matchsticks[0] > totalsum/4 or int(totalsum/4) * 4 != totalsum:
        return False
    sides = [0,0,0,0]
    return backtrack(sides, matchsticks, 0, int(totalsum/4))

def backtrack(sides, matchsticks, index, sum):
    if index >= len(matchsticks):
        return True
    for i in range(4):
        if sides[i] + matchsticks[index] <= sum:
            sides[i]  += matchsticks[index]
            if backtrack(sides,matchsticks, index+1, sum):
                return True
            sides[i]  -= matchsticks[index]
    return False

    

# driver code
def main():
    combinations = [[1,1,2,2,2],[3,3,3,3,4],[1,1,1,2,1],[3,4,4,1,2,2],[5,6,1,1,2,2]]

    for data  in combinations:
        print(f"Input matchsticks: {data}")
        print(f"Output: {matchstick_to_square(data)}")
        print("-" * 100)


if __name__ == '__main__':
    main()