import math
import state

# s = state.create(4)
# puzzle = s[0]

puzzle = [0, 1, 2, 3, 4, 6, 5, 7, 11, 10, 8, 9, 15, 14, 13, 12]

n = int(math.sqrt(len(puzzle)))  

print(f"puzzle: {puzzle}")

for row in range(n):
    print("\n")
    row_tiles = puzzle[row*n:(row+1)*n:1]
    print(f"row:{row}, row_tiles: {row_tiles}")
    tiles_in_goal_row = sum(1 if tile // n == row  else 0 for tile in row_tiles)
    print(f"row: {row}, # in goal row: {tiles_in_goal_row}")
    if tiles_in_goal_row < 2:
        continue

    conflict_per_tile = [0]*n
    for i in range(n):
        for j in range(i):
            if (row_tiles[i] // n == row and row_tiles[j] // n == row and row_tiles[i] < row_tiles[j]):
                conflict_per_tile[i] += 1
                conflict_per_tile[j] += 1
    max_conflict_per_tile = max(conflict_per_tile)
    print(f"row: {row}, initial max_conflict_per_tile: {max_conflict_per_tile}")
    linear_conflicts_in_row = 0
    while max_conflict_per_tile > 0:
        index = conflict_per_tile.index(max_conflict_per_tile)
        conflict_per_tile[index] = 0
        for j in range(n):
            if (row_tiles[j] // n == row and j != index and row_tiles[index] > row_tiles[j]):
                conflict_per_tile[j] -= 1
        max_conflict_per_tile = max(conflict_per_tile)  
        linear_conflicts_in_row += 1
    
    print(f"row: {row}, linear_conflicts_in_row: {linear_conflicts_in_row}")




print("\n")
for col in range(n):
    print("\n")
    col_tiles = puzzle[col:(n-1)*n+col+1:n]
    print(f"col:{col} col_tiles:{col_tiles}")
    tiles_in_goal_col = sum(1 if tile % n == col else 0 for tile in col_tiles)
    print(f"col: {col}, # in goal col: {tiles_in_goal_col}")
    if tiles_in_goal_col < 2:
        continue

    conflict_per_tile = [0]*n
    for i in range(n):
        for j in range(i):
            if (col_tiles[i] % n == col and col_tiles[j] % n == col and col_tiles[i] < col_tiles[j]):
                conflict_per_tile[i] += 1
                conflict_per_tile[j] += 1

    max_conflict_per_tile = max(conflict_per_tile)
    print(f"row: {row}, initial max_conflict_per_tile: {max_conflict_per_tile}")

    linear_conflicts_in_col = 0
    while max_conflict_per_tile > 0:
        index = conflict_per_tile.index(max_conflict_per_tile)
        conflict_per_tile[index] = 0
        for j in range(n):
            if (col_tiles[j] % n == col and j != index and col_tiles[index] > col_tiles[j]):
                conflict_per_tile[j] -= 1
        max_conflict_per_tile = max(conflict_per_tile)  
        linear_conflicts_in_col += 1
    
    print(f"col: {col}, linear_conflicts_in_col: {linear_conflicts_in_col}")



    