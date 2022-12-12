
def part1():
    file = open("input.txt")
    lines = file.readlines()
    rows = len(lines)
    cols = len(lines[0])-1
    heights = [[-1 for y in range(cols)] for x in range(rows)]
    for x in range(cols):
        for y in range(rows):
            heights[x][y] = int(lines[y][x])

    visible = [[False for y in range(cols)] for x in range(rows)]
    maxHeightL = [-1 for y in range(rows)]
    maxHeightR = [-1 for y in range(rows)]
    maxHeightU = [-1 for x in range(cols)]
    maxHeightD = [-1 for x in range(cols)]

    for depth in range(cols):
        for y in range(rows):
            if heights[depth][y] > maxHeightL[y]:
                maxHeightL[y] = heights[depth][y]
                visible[depth][y] = True
            if heights[cols - depth - 1][y] > maxHeightR[y]:
                maxHeightR[y] = heights[cols - depth - 1][y]
                visible[cols - depth - 1][y] = True
    for depth in range(rows):
        for x in range(cols):
            if heights[x][depth] > maxHeightU[x]:
                maxHeightU[x] = heights[x][depth]
                visible[x][depth] = True
            if heights[x][rows - depth - 1] > maxHeightD[x]:
                maxHeightD[x] = heights[x][rows - depth - 1]
                visible[x][rows - depth - 1] = True

    count = 0
    for x in range(cols):
        for y in range(rows):
            if visible[x][y]:
                count += 1

    print(count)
    
def findScenic(myX, myY, heights, rows, cols):
    if myX == 0 or myX == cols-1 or myY == 0 or myY == rows -1: 
        return(0)
    treesRight = 0
    for depth in range(1, cols - myX):
            treesRight += 1
            if heights[myX + depth][myY] >= heights[myX][myY]:
                break
    treesLeft = 0
    for depth in range(1,myX+1):
            treesLeft += 1
            if heights[myX-depth][myY] >= heights[myX][myY]:
                break
    treesDown = 0
    for depth in range(1,rows - myY):
            treesDown += 1
            if heights[myX][myY+depth] >= heights[myX][myY]:
                break
    treesUp = 0
    for depth in range(1,myY+1):
            treesUp += 1
            if heights[myX][myY- depth] >= heights[myX][myY]:
                break
    #print("up " + str(treesUp) + " down " + str(treesDown) + " left " + str(treesLeft) + " right " + str(treesRight))
    return(treesUp*treesDown*treesLeft*treesRight)
    
    
file = open("input.txt")
lines = file.readlines()
rows = len(lines)
cols = len(lines[0])-1
heights = [[-1 for y in range(cols)] for x in range(rows)]
for x in range(cols):
    for y in range(rows):
        heights[x][y] = int(lines[y][x])

maxScenic = 0
for x in range(cols):
    for y in range(rows):
        z=1
        maxScenic = max(maxScenic, findScenic(x, y, heights, rows, cols))
        #print("x= " + str(x) + " y=" + str(y) + " scenic=" + str(findScenic(x,y,heights, rows,cols)))
print(maxScenic)