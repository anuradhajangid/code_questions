#https://www.educative.io/courses/grokking-coding-interview-patterns-python/bus-routes
from collections import defaultdict, deque


def minimum_buses(routes, src, dest):
    adj_list = {}
    for i, stations in enumerate(routes):
        for station in stations:
            if station not in adj_list:
                adj_list[station] = []
            adj_list[station].append(i)

    queue = deque()
    queue.append([src,0])
    visited_buses = set()
    
    while queue:
        station, buses_taken = queue.popleft()
        if station == dest:
            return buses_taken
        
        if station in adj_list:
            for bus in adj_list[station]:
                if bus not in visited_buses:
                    for s in routes[bus]:
                        queue.append([s, buses_taken+1])
                visited_buses.add(bus)  
    return -1  
    

assert minimum_buses([[2,5,7],[4,6,7]], 2,6) == 2
assert minimum_buses([[1,12],[4,5,9],[9,19],[10,12,13]], 9, 12) == -1
assert minimum_buses([[1,12],[10,5,9],[4,19],[10,12,13]], 1,9) ==3
assert minimum_buses([[1,9,7,8],[3,6,7],[4,9],[8,2,3,7],[2,4,5]], 1, 5) ==3
assert minimum_buses([[1,2,3],[4,5,6],[7,8,9]], 4,6) ==1