
def moveHead(head, dir):
    if(dir == "U"): 
        return(head[0], head[1] + 1)
    elif dir == "R":
        return(head[0] + 1, head[1])
    elif dir == "L":
        return(head[0] - 1, head[1])
    elif dir == "D":
        return(head[0], head[1] - 1)

def moveTail(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1 :
        return(tail)
    toReturn = tail
    if head[0] > tail[0]:
        toReturn = (tail[0] + 1, toReturn[1])
    if head[0] < tail[0]:
        toReturn = (tail[0] - 1, toReturn[1])
    if head[1] > tail[1]:
        toReturn = (toReturn[0], tail[1] + 1)
    if head[1] < tail[1]:
        toReturn = (toReturn[0], tail[1] - 1)
    return toReturn

def printgrid(grid, knots):
    string = ""
    for y in range(len(grid[0])-1, -1, -1):
        for x in range(len(grid)):
            matchFound = False
            for i in range(10):
                if (x,y) == knots[i]:
                    if i == 0:
                        string += "H"
                    else:
                        string += str(i)
                    matchFound = True
                    break
            if not matchFound:
                if (x,y) == (0,0):
                    string += "s"
                else:
                    string += "."
        string += "\n"
    print(string)
    print()


file = open("input.txt")
lines = file.readlines()
grid = [[False for x in range(500)] for y in range(500)]
knots = [(0,0) for x in range(10)]
grid[0][0] = True
for line in lines:
    dir = line[0]
    amount = line.split(' ')[1].strip()
    for i in range(int(amount)):
        knots[0] = moveHead(knots[0], dir)
        for j in range(9):
            knots[j+1] = moveTail(knots[j], knots[j+1])
            grid[knots[9][0]][knots[9][1]] = True
        #printgrid(grid,knots)

count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == True:
            count += 1
str = ""
for y in range(len(grid[0])-1, -1, -1):
    for x in range(len(grid)):
        if grid[x][y] == True:
            str += "#"
        else:
            str += "."
    str += "\n"
print(str)
print()
print(count)