class Valve:
    def __init__(self, name, flowRate, neighbours):
        self.name = name
        self.flowRate = flowRate
        self.neighbours = neighbours

file = open("practice.txt")
lines = file.readlines()

dictionary = { }
for line in lines:
    name = line.split(' ')[1]
    flowRate = line.split(' ')[4][5:len(line.split(' ')[4]) - 1]
    neighbours = []
    for i in range(9, len(line.split(' '))):
        neighbours.append(line.split(' ')[i][0:2])
    valve = Valve(name, flowRate, neighbours)
    dictionary[name]= valve

minutesLeft = 30