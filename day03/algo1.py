rawFile = open("input", "r")
sum = 0

while True:
  line = rawFile.readline().strip()
  if not line:
    break
  length = len(line)
  first = line[0:length//2]
  second = line[length//2:length]
  common = set(first).intersection(second).pop()
  number = ord(common)
  if number >= 97 and number <= 122:
    number -= 96
  else:
    number -= 38
  sum += number
  print(first, second, common, number)

print(sum)