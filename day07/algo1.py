
class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.contents = {}
    self.parent = parent
  
  def goTo(self, dest):
    if dest == "/":
      return self
    if dest == "..":
      return self.parent
    return self.contents[dest]
  
  def __str__(self):
    return f"dir: {self.name}, parent: {self.parent}, contents: {self.contents}"
  
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
    workingDirectory = workingDirectory.goTo(words[1])
  return workingDirectory

def getNextLine(rawFile, workingDirectory):
  line = rawFile.readline().strip()
  if not line:
    return 0
  words = line.split()
  if words[0] == '$':
    return runCommand(workingDirectory)
  if words[0] == 'dir':
    return Directory(words[1], workingDirectory)
  return File(words[1], words[0])

print(workingDirectory)
getNextLine(rawFile, workingDirectory)
print(workingDirectory)