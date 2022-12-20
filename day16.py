import itertools


class Valve:
    def __init__(self, name, flowRate, neighbours):
        self.name = name
        self.flowRate = int(flowRate)
        self.neighbours = neighbours
        self.released = False
        self.valveDistances = {}

def solve(minute, currValve):
    if minute == 0:
        return 0
    maxRelease = 0
    if (not currValve.flowRate == 0) and (not currValve.released):
        currValve.released = True
        maxRelease = max(maxRelease, int(solve(minute-1,currValve)) + int((minute-1))*currValve.flowRate)
        currValve.released = False
    for i in range(len(currValve.neighbours)):
        maxRelease = max(maxRelease, solve(minute-1, valves[currValve.neighbours[i]]))
    return maxRelease

def release(list):
    release = 0
    minutesLeft = 29 - list[0].valveDistances[list[1].name]
    for i in range(1, len(list)):
        valve = list[i]
        release += valve.flowRate * minutesLeft
        if i == len(list)-1:
            return release
        minutesLeft -= valve.valveDistances[list[i+1].name] + 1
        if minutesLeft <= 0:
            return release

file = open("input.txt")
lines = file.readlines()

valves = { }
nonZeroValves = []
for line in lines:
    name = line.split(' ')[1]
    flowRate = line.split(' ')[4][5:len(line.split(' ')[4]) - 1]
    neighbours = []
    for i in range(9, len(line.split(' '))):
        neighbours.append(line.split(' ')[i][0:2])
    valve = Valve(name, flowRate, neighbours)
    valves[name]= valve
    if not flowRate == 0:
        nonZeroValves.append(valve)

for valve in nonZeroValves:
    for valve2 in nonZeroValves:
        if valve == valve2: 
            valve.valveDistances[valve2.name] = 0
        elif not valve.neighbours.count(valve2.name) == 0:
            valve.valveDistances[valve2.name] = 1
        else:
            paths = []
            for neighbour in valve.neighbours:
                paths.append((neighbour, int(1)))
                valves[neighbour].released = True
            linkFound = False
            while not linkFound:
                path = paths.pop()
                for neighbour in valves[path[0]].neighbours:
                    if valves[neighbour].released == False:
                        valves[neighbour].released = True
                        if neighbour == valve2.name:
                            linkFound = True
                            valve.valveDistances[valve2.name] = path[1] + 1
                        paths.append((neighbour, path[1]+1))
            for v in valves.values():
                v.released = False

print('ooga')
startValve = valves["AA"]
print(len(nonZeroValves))
superList = list(itertools.permutations(nonZeroValves, 10))
print(len(superList))
maxRelease = 0

for list in superList:
    if list[0] == startValve:
        maxRelease = max(maxRelease, release(list))

print(maxRelease)

list = [valves["DD"], valves["BB"], valves["JJ"], valves["HH"], valves["EE"], valves["CC"]]
print(release(list))
#Manually trying all paths didn't work
#Next attempt: listing all the valves with non-zero flowrate, and trying every order of these