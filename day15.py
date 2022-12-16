def printCave(grid):
    string = ""
    for x in range(0, len(grid)):
        if grid[x][y] == 0:
            string += "."
        elif grid[x][y] == 1:
           string += "S"
        elif grid[x][y] == 2:
            string += "B"
        elif grid[x][y] == 3:
            string += "#"
        elif grid[x][y] == 4:
            string += "O"
    string += "\n"
    print(string)
        
file = open("input.txt")
lines = file.readlines()
maxSize = 4000000
beacons = []
sensors = []
minX = 999999999999999
maxX = -999999999999
minY = 9999999999999
maxY  = -999999999
for line in lines:
    sensorX = line.split(' ')[2]
    sensorX = int(sensorX[2:len(sensorX)-1])
    sensorY = line.split(' ')[3]
    sensorY = int(sensorY[2:len(sensorY)-1])
    sensors.append((sensorX, sensorY))
    beaconX = line.split(' ')[8]
    beaconX = int(beaconX[2:len(beaconX)-1])
    beaconY = line.split(' ')[9]
    beaconY = int(beaconY[2:len(beaconY)])
    beacons.append((beaconX, beaconY))
    minX = min(minX, sensorX, beaconX)
    maxX = max(maxX, sensorX, beaconX)
    minY = min(minY, sensorY, beaconY)
    maxY = max(maxY, beaconY, sensorY)


#0 is free, 1 is Sensor, 2 is Beacon, 3 is can't be a beacon
#grid = [[0 for x in range(maxSize+1)] for y in range(maxSize+1)]
print("grid made")

# for i in range(len(beacons)):
#     beacon = beacons[i]
#     sensor = sensors[i]
#     if sensor[0] >= 0 and sensor[0] <= maxSize and sensor[1] >= 0 and sensor[1] <= maxSize:
#         grid[sensor[0]][sensor[1]] = 1
#     if beacon[0] >= 0 and beacon[0] <= maxSize and beacon[1] >= 0 and beacon[1] <= maxSize:
#         grid[beacon[0]][beacon[1]] = 2
#     manHattanDist = abs(beacon[0] - sensor[0]) + abs(sensor[1] - beacon[1])
#     for x in range(0, maxSize):
#         for y in range(0, maxSize):
#             if abs(sensor[0] - x) + abs(sensor[1] - y) <= manHattanDist and grid[x][y] == 0:
#                 grid[x][y] = 3
#     print("one down, more to go")

manHattDists = []
for i in range(len(beacons)):
    beacon = beacons[i]
    sensor = sensors[i]
    manHattanDist = abs(beacon[0] - sensor[0]) + abs(sensor[1] - beacon[1])  
    manHattDists.append(manHattanDist)

tuning = 0
x=0
y=0
while y < maxSize + 1:
    x=0
    while  x < maxSize + 1:
        validPos = True
        for i in range(len(beacons)):
            sensor = sensors[i]
            manHattanDist = manHattDists[i]
            if abs(sensor[0] - x) + abs(sensor[1] - y) <= manHattanDist:
                validPos = False
                if not i == 0:
                    manHattDists.pop(i)
                    sensors.pop(i)
                    manHattDists.insert(0,manHattanDist)
                    sensors.insert(0,sensor)
                rem = manHattanDist - (abs(sensor[0] - x) + abs(sensor[1] - y) )
                x += max(0,rem)
                break
        if validPos:
            tuning = 4000000*x + y
            print("tuning = " + str(tuning))
        x += 1
    y += 1
        
print(tuning)
