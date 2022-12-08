rawFile = open("input", "r")
lines = [None] * 3
sum = 0

while True:
  for index in range(3):
    lines[index] = rawFile.readline().strip()
    if not lines[index]:
      print(sum)
      exit()
  common = set(lines[0]).intersection(lines[1]).intersection(lines[2]).pop()
  number = ord(common)
  if number >= 97 and number <= 122:
    number -= 96
  else:
    number -= 38
  sum += number
