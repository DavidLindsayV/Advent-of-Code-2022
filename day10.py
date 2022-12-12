def part1():
    file = open("input.txt")
    lines = file.readlines()

    X = 1
    lineNumber = 0
    adding = False
    myAnswer = 0
    for cycle in range(1, 221):
        if (cycle-20)%40 == 0:
            print("cycle =" + str(cycle) + " x=" + str(X) + " sum=" + str(cycle*X))
            myAnswer += cycle*X
            
        if adding == True:
            adding = False
            X += int(lines[lineNumber].split(' ')[1].strip())
            lineNumber += 1
        elif lines[lineNumber].strip() == "noop":
            lineNumber += 1
        elif lines[lineNumber].strip().split(' ')[0] == "addx":
            adding = True

    print(myAnswer)
    
file = open("input.txt")
lines = file.readlines()

X = 1
lineNumber = 0
adding = False
myAnswer = 0
grid = [ [False for x in range(6)] for y in range(40)]
for cycle in range(1, 241):
    drawingPosRow = int((cycle-1)/40)
    drawingPosCol = (cycle-1)%40
    if abs(X - drawingPosCol) <= 1:
        grid[drawingPosCol][drawingPosRow] = True
        
    if adding == True:
        adding = False
        X += int(lines[lineNumber].split(' ')[1].strip())
        lineNumber += 1
    elif lines[lineNumber].strip() == "noop":
        lineNumber += 1
    elif lines[lineNumber].strip().split(' ')[0] == "addx":
        adding = True
    a = ""
    #print("cycle " + str(cycle) + " x " + str(X))
    #input(a)

str = ""
for y in range(len(grid[0])):
    for x in range(len(grid)):
        if grid[x][y] == True:
            str += "#"
        else:
            str += "."
    str += "\n"
print(str)