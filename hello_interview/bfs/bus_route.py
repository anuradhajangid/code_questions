from collections import deque
class Solution:
    def bus_routes(self, routes: list[list[int]], source: int, target: int):
        # create a bus_stop_map, which is the adjcency map
        bus_stops = dict()
        for i, stops in enumerate(routes):
            for stop in stops:
                if stop in bus_stops:
                    bus_stops[stop].append(i)
                    continue
                bus_stops[stop] = [i]
        
        visited = set()
        queue = deque()
        #create a queue from the start destination
        for bus in bus_stops[source]:
            queue.append((bus,1))
            visited.add(bus)

        while queue:
            curr_bus, no_of_changes = queue.popleft()

            for stop in routes[curr_bus]:
                if stop == target:
                    return no_of_changes
                
                for bus in bus_stops[stop]:
                    if bus not in visited:
                        queue.append((bus, no_of_changes +1))
                        visited.add(bus)

        return no_of_changes
    
assert Solution().bus_routes(routes = [[3, 8, 9], [5, 6, 8], [1, 7, 10]],source = 3, target = 6) == 2
