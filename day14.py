def printCave(grid):
    string = ""
    for y in range(0, maxY+1):
        for x in range(minX, maxX+1):
            if x==500 and y==0:
                string += "+"
            elif grid[x][y] == 0:
                string += "."
            elif grid[x][y] == 1:
                string += "#"
            elif grid[x][y] == 2:
                string += "o"
        string += "\n"
    print(string)
        

file = open("input.txt")
lines = file.readlines()

#0 is empty, 1 is rock, 2 is sand
grid = [[0 for x in range(1000)] for y in range(1000)]

minX = 1000
maxX = -1000
maxY = 0
for line in lines:
    firstPos = (0,0)
    secondPos = (int(line.split(' ')[0].split(',')[0]), int(line.split(' ')[0].split(',')[1]))
    minX = min(minX, secondPos[0])
    maxX = max(maxX, secondPos[0])
    maxY = max(maxY, secondPos[1])
    i = 0
    while i < len(line.split(' ')):
        firstPos = secondPos
        secondPos = (int(line.split(' ')[i].split(',')[0]), int(line.split(' ')[i].split(',')[1]))
        if secondPos[0] < minX:
            minX = secondPos[0]
        if secondPos[0] > maxX:
            maxX = secondPos[0]
        if secondPos[1] > maxY:
            maxY = secondPos[1]
        xStep = 1
        if firstPos[0] > secondPos[0]:
            xStep = -1
        elif firstPos[0] == secondPos[0]:
            xStep = 0
        yStep = 1
        if firstPos[1] > secondPos[1]:
            yStep = -1
        elif firstPos[1] == secondPos[1]:
            yStep = 0
        currPos = (firstPos[0], firstPos[1])
        while currPos != secondPos:
            grid[currPos[0]][currPos[1]] = 1
            currPos = (currPos[0] + xStep, currPos[1] + yStep)
        grid[secondPos[0]][secondPos[1]] = 1
        i += 2
    
maxY = maxY + 2
for x in range(1000):
    grid[x][maxY] = 1

sandCount = 0
while grid[500][0] == 0:
    sandCount += 1
    grid[500][0] = 2
    sandPos = (500,0)
    #printCave(grid)
    while True:
        if grid[sandPos[0]][sandPos[1]+1] == 0:
            grid[sandPos[0]][sandPos[1]]=0
            grid[sandPos[0]][sandPos[1]+1] = 2
            sandPos = (sandPos[0], sandPos[1]+1)
        elif grid[sandPos[0]-1][sandPos[1]+1] == 0:
            grid[sandPos[0]][sandPos[1]]=0
            grid[sandPos[0]-1][sandPos[1]+1] = 2
            sandPos = (sandPos[0]-1, sandPos[1]+1)
        elif grid[sandPos[0]+1][sandPos[1]+1] == 0:
            grid[sandPos[0]][sandPos[1]]=0
            grid[sandPos[0]+1][sandPos[1]+1] = 2
            sandPos = (sandPos[0]+1, sandPos[1]+1)
        else:
            break
print(sandCount)