def region(grid,row,col):
    count=0
    if grid[row][col]==1:
        count+=1
        grid[row][col]=0
        for i in xrange(row-1,row+2):
            for j in xrange(col-1,col+2):
                if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]):
                    count+=region(grid,i,j)
    return count
    
def get_biggest_region(grid):
    maxSize=0
    for row in xrange(len(grid)):
        for col in xrange(len(grid[0])):
            currentRegionSize=region(grid,row,col)
            if maxSize<currentRegionSize:
                maxSize=currentRegionSize
    return maxSize

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
