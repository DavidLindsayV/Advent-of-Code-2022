

class TreeNode:
    def __init__(self):
        self.parent = None
        self.children = []
        self.name = ""
        self.size = -1
        
    def initParent(self):
        self.parent = TreeNode()
        
    def calcSize(self):
        if self.size == -1:
            totalSize = 0
            for child in self.children:
                totalSize += child.calcSize()
            self.size = totalSize
        return(self.size)
    
    def getLargeDirSizes(self, dirSize):
        if len(self.children) != 0 and self.size < 100000:
            dirSize += self.size
        for child in self.children:
            dirSize = child.getLargeDirSizes(dirSize)
        return(dirSize)
    
    def minDirSize(self, minSizeNeeded, minSizeSoFar):
        if len(self.children) != 0 and self.size >= minSizeNeeded and self.size < minSizeSoFar:
            minSizeSoFar = self.size
        for child in self.children:
            minSizeSoFar = child.minDirSize(minSizeNeeded, minSizeSoFar)
        return(minSizeSoFar)

def part1():
    file = open("input.txt")
    lines = file.readlines()
    currNode = TreeNode()
    currNode.initParent()


    currNode.name = "/"
    rootNode = currNode
    readingOutput = False
    for line in lines:
        readingOutput = line.split(" ")[0] != "$"
        if readingOutput:
            newNode = TreeNode()
            newNode.initParent()
            newNode.name = line.split(" ")[1].strip()
            newNode.parent = currNode
            if line.split(" ")[0] != "dir":
                newNode.size = int(line.split(" ")[0])
            currNode.children.append(newNode)
        else:
            command = line.split(" ")[1]
            if command != "ls\n":
                #its cd
                if line.split(" ")[2] == "..\n":
                    currNode = currNode.parent
                elif line.split(" ")[2] == "/\n":
                    currNode = rootNode
                else:
                    for child in currNode.children:
                        if child.name == line.split(" ")[2].strip():
                            currNode = child
    rootNode.calcSize()
    print(rootNode.getLargeDirSizes(0))


file = open("input.txt")
lines = file.readlines()
currNode = TreeNode()
currNode.initParent()


currNode.name = "/"
rootNode = currNode
readingOutput = False
for line in lines:
    readingOutput = line.split(" ")[0] != "$"
    if readingOutput:
        newNode = TreeNode()
        newNode.initParent()
        newNode.name = line.split(" ")[1].strip()
        newNode.parent = currNode
        if line.split(" ")[0] != "dir":
            newNode.size = int(line.split(" ")[0])
        currNode.children.append(newNode)
    else:
        command = line.split(" ")[1]
        if command != "ls\n":
            #its cd
            if line.split(" ")[2] == "..\n":
                currNode = currNode.parent
            elif line.split(" ")[2] == "/\n":
                currNode = rootNode
            else:
                for child in currNode.children:
                    if child.name == line.split(" ")[2].strip():
                        currNode = child
rootNode.calcSize()
totalSize = 70000000 - rootNode.size
print(rootNode.minDirSize(30000000 - totalSize, 999999999999))