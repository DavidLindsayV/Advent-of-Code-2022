def makeList(line):
    list = []
    strings = []
    currentStr = ""
    bracketsDeep = 0
    for c in line:
        if bracketsDeep >= 1:
            currentStr += c
        if c == '[':
            bracketsDeep += 1
        elif c == ']':
            bracketsDeep -= 1
        elif c == ',' and bracketsDeep == 1:
            strings.append(currentStr[0:len(currentStr)-1])
            currentStr = ""
    strings.append(str(currentStr)[0:len(str(currentStr))-1])
    for string in strings:
        if string == '':
          return []  
        elif not '[' in string:
            list.append(int(string))
        else:
            list.append(makeList(string))
    return list
        
def compareLists(list1, list2):
    for i in range(len(list1)):
        item1 = list1[i]
        if i >= len(list2):
            return False
        item2 = list2[i]
        if isinstance(item1, int) ^ isinstance(item2, int):
            if isinstance(item1,int):
                item1 = [item1]
            else:
                item2 = [item2]
        if isinstance(item1, int):
            if item1 < item2:
                return True
            elif item1 > item2:
                return False
        else:
            result = compareLists(item1,item2)
            if result == True:
                return True
            elif result == False:
                return False
    if len(list2) > len(list1):
        return True
    else:
        return None

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if not compareLists(list[j],list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
        

def part1():
    file = open("input.txt")
    lines = file.readlines()
    print(compareLists([2,3,4],[4]))
    index = 1
    sumIndexes = 0
    for i in range(0,len(lines),3):
        list1 = makeList(lines[i].strip())
        list2 = makeList(lines[i+1].strip())
        inOrder = compareLists(list1,list2)
        if inOrder:
            sumIndexes += index
            print(index)
        index += 1
    print(sumIndexes)
    
file = open("input.txt")
lines = file.readlines()
metaList = []
for line in lines:
    if line.strip() != '':
        list = makeList(line.strip())
        metaList.append(list)

divider1 = makeList("[[2]]")
divider2 = makeList("[[6]]")
index1 = 1
index2 = 1
for i in range(len(metaList)):
    if compareLists(metaList[i],divider1):
        index1 += 1
    if compareLists(metaList[i],divider2):
        index2 += 1
index2 += 1
print(len(metaList))
print(str(index1) + " " + str(index2))
print(index1*index2)