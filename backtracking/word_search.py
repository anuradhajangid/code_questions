#https://www.educative.io/courses/grokking-coding-interview-patterns-python/word-search
# Function to search a specific word in the grid
def word_search(grid, word):
    n = len(grid)
    m = len(grid[0])
    for row in range(n):
        for col in range(m):
            if depth_first_search(row, col, word, grid):
                return True
    return False

# Apply backtracking on every element to search the required word
def depth_first_search(row, col, word, grid):
    if len(word) == 0:
        return True

    if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) \
            or grid[row][col].lower() != word[0].lower():
        return False

    grid[row][col] = '*'

    for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if depth_first_search(row + rowOffset, col + colOffset, word[1:], grid):
            return True

    grid[row][col] = word[0]

    return False

def main():
    input = [
             ([['E', 'D', 'X', 'I', 'W'],
              ['P', 'U', 'F', 'M', 'Q'],
              ['I', 'C', 'Q', 'R', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']], "educative"),

             ([['O', 'Y', 'O', 'I'],
              ['B', 'I', 'E', 'M'],
              ['K', 'D', 'Y', 'R'],
              ['M', 'T', 'W', 'I'],
              ['Z', 'I', 'T', 'O']], "DYNAMIC"),

             ([['h', 'e', 'c', 'm', 'l'],
              ['w', 'l', 'i', 'e', 'u'],
              ['a', 'r', 'r', 's', 'n'],
              ['s', 'i', 'i', 'o', 'r']], "WARRIOR"),

             ([['C', 'Q', 'N', 'A'],
              ['P', 'S', 'E', 'I'],
              ['Z', 'A', 'P', 'E'],
              ['J', 'V', 'T', 'K']], "save"),

             ([['A']], "ABC"),

             ([['P', 'S', 'S', 'I', 'W', 'P'],
              ['P', 'Y', 'C', 'A', 'Q', 'T'],
              ['I', 'S', 'H', 'P', 'F', 'Y'],
              ['M', 'T', 'O', 'L', 'O', 'I'],
              ['J', 'I', 'N', 'O', 'G', 'K'],
              ['I', 'M', 'D', 'T', 'Y', 'T']], "PSYCHOLOGY")
            ]
    num = 1

    for i in input:
        print(num, ".\tGrid =", sep="")
        for j in range(len(i[0])):
            print("\t\t", i[0][j])
        if i[1] == "":
            print('\n\tWord = ""')
        else:
            print(f"\n\tWord =  {i[1]}")
        search_result = word_search(i[0], i[1])
        if search_result:
            print("\n\tSearch result = Word found")
        else:
            print("\n\tSearch result = Word could not be found")
        num += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()