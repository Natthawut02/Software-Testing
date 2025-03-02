def gridChallenge(grid):
    # Sort each row alphabetically
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))
    
    # Check if columns are sorted
    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"
    return "YES"