def path_finder(maze, x=0, y=0, last_positions=[(0, 0)]):
    # split maze first time it is run
    if type(maze) == str:
        maze = maze.split('\n')
    
    # catch if the last_positions stay after test case finishes, (code wars problem)
    if len(last_positions) > 1 and x == 0 and y == 0:
        last_positions = [(0, 0)]
    
    # if position is bottom right completed, and exit exists.
    if x == len(maze) - 1 and y == len(maze[len(maze) - 1]) - 1:
        return True
    
    # checks if going up is possible
    if x - 1 > - 1 and maze[x-1][y] == '.' and (x - 1, y) not in last_positions:
        last_positions.append((x - 1, y))

        # this check allows us to come back to this point for all the different paths, 
        # incase we find a deadend
        if path_finder(maze, x - 1, y, last_positions):
            return True

    # check if can go right
    if y + 1 < len(maze) and maze[x][y + 1] == '.' and (x, y+1) not in last_positions:
        last_positions.append((x, y+1))
        # same idea as other check.
        if path_finder(maze, x, y + 1, last_positions):
            return True
    
    # check if you can go down
    if x + 1 < len(maze) and maze[x+1][y] == '.' and (x + 1, y) not in last_positions:
        last_positions.append((x + 1, y))
        # same check
        if path_finder(maze, x + 1, y, last_positions):
            return True

    # check if you can go left
    if y - 1 > - 1 and maze[x][y - 1] == '.' and (x, y-1) not in last_positions:
        last_positions.append((x, y-1))
        # same check
        if path_finder(maze, x, y - 1, last_positions):
            return True
    
    # dead end or maze is impossible
    return False