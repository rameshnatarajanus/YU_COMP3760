'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''
import random
import math

#returns a random board nXn
def create(n):
    s=list(range(n*n))      # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m="<>v^"                # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n**3):  # makes n^3 random moves to mix the tiles
        if_legal(s,m[random.randrange(4)])
    return [s,""]           # at the beginning "" is an empty path, later on path
                            # contains the path that leads from the initial state to the state

def get_next(x):            # returns a list of the children states of x
    ns=[]                   # the next state list
    for i in "<>v^":
        s=x[0][:]           # [:] - copies the board in x[0]
        if_legal(s,i)       # try to move in direction i
        # checks if the move was legal and...
        if s.index(0)!=x[0].index(0) and \
           (x[1]=="" or x[1][-1]!="><^v"["<>v^".index(i)]): # check if it's the first move or it's a reverse move
            ns.append([s,x[1]+i])   # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])

def is_target(x):
    n=len(x[0])                     # the size of the board
    return x[0]==list(range(n))     # list(range(n)) is the target state

#############################
def if_legal(x,m):                  # gets a board and a move and makes the move if it's legal
    n=int(math.sqrt(len(x)))        # the size of the board is nXn
    z=x.index(0)                    # z is the place of the empty tile (0)
    if z%n>0 and m=="<":            # checks if the empty tile is not in the first col and the move is to the left
        x[z]=x[z-1]                 # swap x[z] and x[z-1]...
        x[z-1]=0                    # ...and move the empty tile to the left
    elif z%n<n-1 and m==">":        # check if the empty tile is not in the n's col and the move is to the right
        x[z]=x[z+1]
        x[z+1]=0
    elif z>=n and m=="^":           # check if the empty tile is not in the first row and the move is up
        x[z]=x[z-n]
        x[z-n]=0
    elif z<n*n-n and m=="v":        # check if the empty tile is not in the n's row and the move is down
        x[z]=x[z+n]
        x[z+n]=0

# This is your HW
def hdistance0(s):                   # the heuristic value of s -- uniform cost
    return 0

def hdistance1(s):
    # Number of tiles out of place
    return sum(1 for i, tile in enumerate(s[0]) if tile != i and tile != 0)

def hdistance2(s):

    n = int(math.sqrt(len(s[0])))  

    return sum(abs(i // n - tile // n) + abs(i % n - tile % n) for i, tile in enumerate(s[0]) if tile != 0)


def hdistance3(s):

    puzzle = s[0]

    n = int(math.sqrt(len(puzzle)))  
    linear_conflicts = 0

    # first the rows 
    for row in range(n):
        row_tiles = puzzle[row*n:(row+1)*n:1]
        tiles_in_goal_row = sum(1 if tile // n == row  else 0 for tile in row_tiles)
        if tiles_in_goal_row < 2:
            continue

        conflict_per_tile = [0]*n
        for i in range(n):
            for j in range(i):
                if (row_tiles[i] // n == row and row_tiles[j] // n == row and row_tiles[i] < row_tiles[j]):
                    conflict_per_tile[i] += 1
                    conflict_per_tile[j] += 1
        max_conflict_per_tile = max(conflict_per_tile)
        linear_conflicts_in_row = 0
        while max_conflict_per_tile > 0:
            index = conflict_per_tile.index(max_conflict_per_tile)
            conflict_per_tile[index] = 0
            for j in range(n):
                if (row_tiles[j] // n == row and j != index and row_tiles[index] > row_tiles[j]):
                    conflict_per_tile[j] -= 1
            max_conflict_per_tile = max(conflict_per_tile)  
            linear_conflicts_in_row += 1
        
        linear_conflicts += linear_conflicts_in_row

    # then the cols  
    for col in range(n):
        col_tiles = puzzle[col:(n-1)*n+col+1:n]
        tiles_in_goal_col = sum(1 if tile % n == col else 0 for tile in col_tiles)
        if tiles_in_goal_col < 2:
            continue
        
        # goal_rows = [tile // n for tile in col_tiles]       
        conflict_per_tile = [0]*n
        for i in range(n):
            for j in range(i):
                if (col_tiles[i] % n == col and col_tiles[j] % n == col and col_tiles[i] < col_tiles[j]):
                    conflict_per_tile[i] += 1
                    conflict_per_tile[j] += 1

        max_conflict_per_tile = max(conflict_per_tile)

        linear_conflicts_in_col = 0
        while max_conflict_per_tile > 0:
            index = conflict_per_tile.index(max_conflict_per_tile)
            conflict_per_tile[index] = 0
            for j in range(n):
                if (col_tiles[j] % n == col and j != index and col_tiles[index] > col_tiles[j]):
                    conflict_per_tile[j] -= 1
            max_conflict_per_tile = max(conflict_per_tile)  
            linear_conflicts_in_col += 1
        linear_conflicts += linear_conflicts_in_col

    
    return hdistance2(s) + 2*linear_conflicts


