import operator
import math

LCM = 0

class item:
    def __init__(self, value):
        self.val = value
        self.monkes = []
    def setval(self, val):
        self.val = val

def printMonkeys(monkeys):
    string = ""
    count = 0
    for monke in monkeys:
        string += "Monkey " + str(count) + ": "
        for item in monke.items:
            string += str(item) + ", "
        string += "\n"
        count += 1
    print(string)


class Monkey:
    def __init__(self, items, operation, amount, test, trueMonke, falseMonke):
        if amount == "old":
                self.operation = lambda x: x.setval(x.val**2)
        else:
            if operation == "*":
                self.operation = lambda x: x.setval(x.val * int(amount))
            elif operation == "+":
               self.operation = lambda x: x.setval(x.val + int(amount))
            elif operation == "-":
                self.operation = lambda x: x.setval(x.val - int(amount))
            elif operation == "/":
               self.operation = lambda x: x.setval(x.val / int(amount))
        self.items = items
        self.test = lambda x: x.val%test==0
        self.trueMonke = trueMonke
        self.falseMonke = falseMonke
        self.tally = 0
        
    def throw(self, monkeys):
        listLen = len(self.items)
        self.tally += listLen
        for i in range(listLen):
            item = self.items[i]
            self.operation(item)
            #item.setval(int(item.val/3))
            item.setval(item.val%LCM)
            if self.test(item):
                monkeys[self.trueMonke].items.append(item)
        #        item.monkes.append(self.trueMonke)
            else:
                monkeys[self.falseMonke].items.append(item)
        #        item.monkes.append(self.falseMonke)
        self.items = []

file = open("input.txt")
lines = file.readlines()
lineNumber = 0
monkeys = []
divisors = set()
while lineNumber < len(lines):
    lineNumber += 1
    #Get items
    items = []
    itemLine = lines[lineNumber]
    for i in range(len(itemLine.split(' '))-4):
        items.append(item(int(itemLine.split(' ')[i+4].replace(',','').strip())))
    lineNumber += 1
    #Get operation
    lambdaLine = lines[lineNumber]
    operation = lambdaLine.split(' ')[6]
    amount = lambdaLine.split(' ')[7].strip()

    lineNumber += 1
    #Get test
    testLine = lines[lineNumber]
    test = int(testLine.split(' ')[5].strip())
    divisors.add(test)
    lineNumber += 1
    #Monkey if true
    trueMonke = int(lines[lineNumber].split(' ')[9].strip())
    lineNumber += 1
    #Monkey if false
    falseMonke = int(lines[lineNumber].split(' ')[9].strip())
    monke = Monkey(items, operation, amount, test, trueMonke, falseMonke)
    monkeys.append(monke)
    lineNumber += 2
    
LCM = 1
for num in divisors:
    LCM = math.lcm(LCM, num)

for i in range(10000):
    for monke in monkeys:
        monke.throw(monkeys)
    print(i)
    

        
monkeys.sort(key=lambda x: -x.tally)
print(monkeys[0].tally)
print(monkeys[1].tally)
print(monkeys[0].tally*monkeys[1].tally)