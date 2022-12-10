class Directory:
  def __init__(self, name, parent=None):
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
    return self

  def __str__(self):
    if not self.parent:
      parent = "None"
    else:
      parent = self.parent.name
    return f"dir: {self.name}, parent: {parent}, contents: {self.contents}"
  
class File:
  def __init__(self, name, size):
    self.name = name
    self.size = int(size)
  
  def __str__(self):
    return f"file: {self.name}, size: {self.size}"

rawFile = open("test.txt", "r")
root = Directory('/')
workingDirectory = root

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

print(workingDirectory)
while True:
   workingDirectory = getNextLine(rawFile, workingDirectory)
   if not workingDirectory:
     break
print(root.get('a'))
