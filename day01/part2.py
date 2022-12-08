rawFile = open("input", "r")
calories = 0
caloryList = []

while True:
  line = rawFile.readline()
  # Summarise elf calories and increment elves
  if len(line) <= 1:
    caloryList.append(calories)
    calories = 0
  # end of file
  if not line:
    break
  stripped = line.strip()
  if not stripped:
    continue
  # Counting calories for current elf
  calory = int(stripped)
  calories += calory

caloryList.sort(reverse=True)
topthree = caloryList[0] + caloryList[1] + caloryList[2]
print(caloryList)
print(topthree)