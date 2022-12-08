rawFile = open("input", "r")



def getMarker(line):
  chars = ""
  for index, nextChar in enumerate(line):
    location = chars.find(nextChar)
    if location == -1:
      chars += nextChar
      if len(chars) >= 14:
        return index + 1, chars
      continue
    chars = chars[location+1:] + nextChar

while True:
  line = rawFile.readline().strip()
  if not line:
    break
  index, chars = getMarker(line)
  print(index)
  print(chars)
