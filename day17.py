def printCave(grid):
    string = ""
    for y in range(10, -1,-1):
        for x in range(0, len(grid)):
            if grid[x][y] == '#':
                string += "#"
            elif grid[x][y] == ".":
                string += "."
        string += "\n"
    print(string)
    
def collision(pushx, pushy):
    if rockPos[1] < 0:
        return True
    for x in range(rock[1]):
        for y in range(rock[2]):
            if rock[0][3-y][x]==1 and (rockPos[1]+y+pushy < 0 or grid[rockPos[0]+x+pushx][rockPos[1]+y+pushy]=="#"):
                return True
    return False


file = open("practice.txt")
lines = file.readlines()

pushes = lines[0]

rocks = []
rocks.append( ([ [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [1,1,1,1]
            ], 4, 1))    #Rocks are in the format: Array, Width, Height
rocks.append( ([ [0,0,0,0],
                [0,1,0,0],
                [1,1,1,0],
                [0,1,0,0]
            ], 3, 3))
rocks.append(( [ [0,0,0,0],
                [0,0,1,0],
                [0,0,1,0],
                [1,1,1,0]
            ], 3, 3))
rocks.append(( [ [1,0,0,0],
                [1,0,0,0],
                [1,0,0,0],
                [1,0,0,0]
            ], 1, 4))
rocks.append( ([ [0,0,0,0],
                [0,0,0,0],
                [1,1,0,0],
                [1,1,0,0]
            ], 2, 2))
topHeight = [0,0,0,0,0,0,0]
grid = [["." for y in range(4*2022)] for x in range(7)]
push = 0
for i in range(2022):
    rock = rocks[i%5]
    rockPos = (2, max(topHeight)+3)
    rockFalling = True
    while rockFalling:
        #Get direction of push
        pushx = 1
        if pushes[push%len(pushes)] == '<':
            pushx = -1
            
        if ((rockPos[0] + (rock[1]-1) + pushx < 7 and pushx > 0 ) or (rockPos[0] + pushx >= 0 and pushx < 0)) and (not collision(pushx,0)):
            rockPos = (rockPos[0]+pushx,rockPos[1])
            
        safeToFall = True
        if max(topHeight) >= rockPos[1]-1:
            if collision(0,-1):
                rockFalling = False
                safeToFall = False
                break
        if safeToFall:
            rockPos = (rockPos[0],rockPos[1]-1)
        push += 1
                
    for x in range(rock[1]):
        height = 3
        for y in range(4):
            if rock[0][3-y][x] == 1:
                break
            height -= 1
        topHeight[rockPos[0]+x] = max(topHeight[rockPos[0]+x],rockPos[1]+height)
    for x in range(4):
        for y in range(4):
            if rock[0][3-y][x]==1:
                grid[rockPos[0]+x][rockPos[1]+y] = "#"
    a=""
    input(a)
    printCave(grid)

print(max(topHeight))