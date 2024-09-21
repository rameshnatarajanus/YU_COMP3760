import math
import state

# s = state.create(4)
# puzzle = s[0]

puzzle = [0, 1, 2, 3, 6, 5, 8, 4, 9, 10, 11, 7, 15, 14, 12, 13]

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
    goal_cols = [tile % n for tile in row_tiles]
    print(f"row: {row}, goal_cols: {goal_cols}")
    tiles_in_conflict = [0]*n
    for i in range(n):
        for j in range(i):
            if (row_tiles[i] // n == row and row_tiles[j] // n == row and goal_cols[i] < goal_cols[j]):
                tiles_in_conflict[i] += 1
                tiles_in_conflict[j] += 1
    max_tiles_in_conflict = max(tiles_in_conflict)
    print(f"row: {row}, initial max_tiles_in_conflict: {max_tiles_in_conflict}")
    linear_conflicts_in_row = 0
    while max_tiles_in_conflict > 0:
        index = tiles_in_conflict.index(max_tiles_in_conflict)
        tiles_in_conflict[index] = 0
        for j in range(n):
            if (row_tiles[j] // n == row and j != index and goal_cols[index] > goal_cols[j]):
                tiles_in_conflict[j] -= 1
        max_tiles_in_conflict = max(tiles_in_conflict)  
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
    goal_rows = [tile // n for tile in col_tiles]
    print(f"col: {col}, goal_rows: {goal_rows}")
    tiles_in_conflict = [0]*n
    for i in range(n):
        for j in range(i):
            if (col_tiles[i] % n == col and col_tiles[j] % n == col and goal_rows[i] < goal_rows[j]):
                tiles_in_conflict[i] += 1
                tiles_in_conflict[j] += 1

    max_tiles_in_conflict = max(tiles_in_conflict)
    print(f"row: {row}, initial max_tiles_in_conflict: {max_tiles_in_conflict}")

    linear_conflicts_in_col = 0
    while max_tiles_in_conflict > 0:
        index = tiles_in_conflict.index(max_tiles_in_conflict)
        tiles_in_conflict[index] = 0
        for j in range(n):
            if (col_tiles[j] % n == col and j != index and goal_rows[index] > goal_rows[j]):
                tiles_in_conflict[j] -= 1
        max_tiles_in_conflict = max(tiles_in_conflict)  
        linear_conflicts_in_col += 1
    
    print(f"col: {col}, linear_conflicts_in_col: {linear_conflicts_in_col}")



    