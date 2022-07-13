import math
import heapq

def findRestaurants(allLocations, numRestaurants):
    # Write your code here
    min_heap = []
    location_map = {}
    result = []
    
    for location in allLocations:
        x, y = location
        distance = (math.sqrt((abs(x) ** 2) + (abs(y) ** 2)))
        if distance in location_map:
            tie_x, tie_y = location_map[distance]
            if tie_x < x:
                continue
        location_map[distance] = location
        heapq.heappush(min_heap, distance)
        
    for _ in range(numRestaurants):
        result.append(location_map[heapq.heappop(min_heap)])
    return result



print(findRestaurants([[1,2],[2,3],[2,3], [2,4]], 2))
