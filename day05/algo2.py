rawFile = open("input.txt", "r")

def printStack(stacks):
  for stack in stacks:
    print(stack)
    
def readStack(rawFile):
  while True:
    line = rawFile.readline().rstrip()
    if not line:
      break
    yield line
  
def parseBottom(stacks, lines):
  row = [letter[1] for letter in lines.pop().split()]
  for item in row:
    stacks.append([item])
  
def parseTheRest(stacks, lines):
  letterCount = 0
  for index, char in enumerate(lines.pop()):
    if index == 1 + 4 * letterCount:
      if char != ' ':
        stacks[letterCount].append(char)
      letterCount += 1

def parseStackLines(rawFile):
  stacks = []
  lines = [line for line in readStack(rawFile)]
  lines.pop()
  parseBottom(stacks, lines)
  while lines:
    parseTheRest(stacks, lines)
  return stacks

def getNextMove(rawFile):
  line = rawFile.readline().strip().split()
  if not line:
    return False
  move = [int(line[1]), int(line[3]) - 1, int(line[5]) - 1]
  return move

def executeMove(rawFile, stacks):
  move = getNextMove(rawFile)
  if not move:
    return False
  numOfCrates = move[0]
  fromStack = move[1]
  toStack = move[2]
  splitIndex = len(stacks[fromStack]) - numOfCrates
  stacks[toStack] += stacks[fromStack][splitIndex:]
  stacks[fromStack] = stacks[fromStack][:splitIndex]
  return True

def rearrange(rawFile, stacks):
  while executeMove(rawFile, stacks):
    pass

def collectTop(stacks):
  result = []
  for stack in stacks:
    result.append(stack.pop())
  return result

stacks = parseStackLines(rawFile)
print("before:")
printStack(stacks)
rearrange(rawFile, stacks)
print("after:")
printStack(stacks)
print("result:")
print(''.join(collectTop(stacks)))

