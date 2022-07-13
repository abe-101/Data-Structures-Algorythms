from collections import deque

def minimumDistance(area):
    # Write your code here
    start_row = 0
    start_col = 0
    visited = set((0, 0))
    queue = deque((start_row, start_col, 0))
    while queue:
        r, c, distance = queue.popleft()
        if area[r][c] == 9:
            return distance
        deltas = [(1,0), (-1,0), (0,1), (0,-1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = r + delta_row
            neighbor_col = c + delta_col
            pos = (neighbor_row, neighbor_col)
            row_inbounds = 0 <= neighbor_row < len(area)
            col_inbounds = 0 <= neighbor_col < len(area[0])
            if row_inbounds and col_inbounds and pos not in visited and area[neighbor_row][neighbor_col] != 0:
                visited.add(pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))
    return -1

area = [[1,0,0,], [1,0,0], [1,9,1]]
print(minimumDistance(area))
