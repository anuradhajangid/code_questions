import pytest
def sort_colors(colors):

    start = 0
    current = 0
    end = len(colors) - 1
    
    while current <= end:
      if colors[current] == 0:
        colors[start], colors[current] = colors[current], colors[start]
        start += 1
        current += 1
      elif colors[current] == 1:
        current += 1
      elif colors[current] == 2:
        colors[current], colors[end] = colors[end], colors[current]
        end -= 1
      else:
        raise ValueError(f"Expected one of [0,1,2] found {colors[current]}")

    return colors
    
assert sort_colors([0,0,1,1,1,2]) == [0,0,1,1,1,2]
assert sort_colors([0,2,1,0,2,2,1,0]) == [0,0,0,1,1,2,2,2]
assert sort_colors([0,1,0]) == [0,0,1]
assert sort_colors([2,2,2])  == [2,2,2]
with pytest.raises(ValueError) as err: 
    sort_colors([3,4,5]) 
assert err.typename == 'ValueError'

"""
TimeComplexity: O(N)
SpaceComplexity: O(1)
"""