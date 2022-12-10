class Directory:
  def __init__(self, name, parent=None):
    self.type = 'directory'
    self.name = name
    self.contents = {}
    self.parent = parent
    self.size = 0
  
  def get(self, dest):
    if dest == "/":
      return self
    if dest == "..":
      return self.parent
    return self.contents[dest]

  def add(self, src):
    self.contents[src.name] = src
    self.size += src.size
    self.accumulateSize(src.size)
    return self

  def accumulateSize(self, size):
    if self.parent == None:
      return
    self.parent.size += size
    self.parent.accumulateSize(size)

  def __str__(self):
    if not self.parent:
      parent = "None"
    else:
      parent = self.parent.name
    return f"dir: {self.name}, parent: {parent}, size: {self.size}"
  
class File:
  def __init__(self, name, size):
    self.type = 'file'
    self.name = name
    self.size = int(size)
  
  def __str__(self):
    return f"file: {self.name}, size: {self.size}"


def runCommand(words, workingDirectory):
  if words[0] == "cd":
    workingDirectory = workingDirectory.get(words[1])
  return workingDirectory

def getNextLine(rawFile, workingDirectory):
  line = rawFile.readline().strip()
  if not line:
    return 0
  words = line.split()
  if words[0] == '$':
    return runCommand(words[1:],workingDirectory)
  if words[0] == 'dir':
    return workingDirectory.add(Directory(words[1], workingDirectory))
  return workingDirectory.add(File(words[1], words[0]))

def constructTree(directory):
  while True:
    directory = getNextLine(rawFile, directory)
    if not directory:
      break

def traverseTree(directory, toFree):
  optimal = directory.size
  queue = [directory]
  for element in queue:
    queue += [value for value in element.contents.values() if value.type == 'directory']
    if element.size >= toFree and element.size < optimal:
      optimal = element.size
  return optimal

rawFile = open("input.txt", "r")

capacity = 70000000
required = 30000000

root = Directory('/')
constructTree(root)
unused = capacity - root.size
toFree = required - unused
print(traverseTree(root, toFree))
