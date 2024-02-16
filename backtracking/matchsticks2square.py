
def matchstick_to_square(matchsticks):
    matchsticks = sorted(matchsticks,reverse=True)
    totalsum = sum(matchsticks)
    sidesum = int(totalsum/4)
    if matchsticks[0] > sidesum or sidesum * 4 != totalsum:
        return False
    sides = [0,0,0,0]
    def backtrack(index):
        if index >= len(matchsticks):
            return True
        for i in range(4):
            if sides[i] + matchsticks[index] <= sidesum:
                sides[i]  += matchsticks[index]
                if backtrack(index+1):
                    return True
                sides[i]  -= matchsticks[index]
        return False
    return backtrack(0)
    

# driver code
def main():
    combinations = [[1,1,2,2,2],[3,3,3,3,4],[1,1,1,2,1],[3,4,4,1,2,2],[5,6,1,1,2,2]]

    for data  in combinations:
        print(f"Input matchsticks: {data}")
        print(f"Output: {matchstick_to_square(data)}")
        print("-" * 100)


if __name__ == '__main__':
    main()