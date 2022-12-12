def printgrid(heights):
    string = ""
    for y in range(len(heights[0])):
        for x in range(len(heights)):
            string += chr(heights[x][y]+96)
        string += "\n"
    print(string)

file = open("input.txt")
lines = file.readlines()
start = []
end = (0,0)
heights = [[-1 for x in range(len(lines))] for y in range(len(lines[0]))]
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "\n":
            continue
        elif(lines[y][x] == "E"):
            end = (x,y)
            heights[x][y] = 26
        elif lines[y][x] == "S":
            start.append((x,y))
            heights[x][y] = 1
        else:
            heights[x][y] = ord(lines[y][x]) - 96
            if heights[x][y]==1:
                start.append((x,y))

printgrid(heights)
minDist = 9999999999
for beginning in start:
    distances =  [[-1 for x in range(len(lines))] for y in range(len(lines[0]))]
    toVisit = [(beginning[0],beginning[1],0)]
    distances[beginning[0]][beginning[1]] = 0
    stop= False
    while len(toVisit) != 0 and not stop:
        pos = toVisit.pop()
        for a in range(-1, 2):
            for b in range(-1,2):
                if (a==0 or b==0) and pos[0]+a < len(lines[0]) and pos[0]+a > -1 and (pos[1]+b < len(lines)) and pos[1]+b > -1 and not heights[pos[0]+a][pos[1]+b] == -1 and distances[pos[0]+a][pos[1]+b] == -1 and heights[pos[0]+a][pos[1]+b] <= heights[pos[0]][pos[1]] + 1:
                    toVisit.append((pos[0]+a,pos[1]+b,distances[pos[0]][pos[1]]+1))
                    distances[pos[0]+a][pos[1]+b] = distances[pos[0]][pos[1]]+1
                    if (pos[0]+a,pos[1]+b) == end:
                        stop=True
        toVisit.sort(key=lambda x:-x[2])
    if not distances[end[0]][end[1]] == -1:
        minDist = min(minDist, distances[end[0]][end[1]])
    print(minDist)
 