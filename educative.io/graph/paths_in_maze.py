#https://www.educative.io/courses/grokking-coding-interview-patterns-python/paths-in-maze-that-lead-to-same-room
from collections import defaultdict


def number_of_paths(n, corridors):
    graph = defaultdict(set)
    cycles = 0
    for x,y in corridors:
        graph[x].add(y)
        graph[y].add(x)
        cycles += len(graph[x].intersection(graph[y]))
    return cycles




assert number_of_paths(5,[[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]) == 2