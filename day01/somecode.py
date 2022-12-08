rawFile = open("input", "r")
calories = 0
caloryList = []
largestCalories = -1
theElf = 0

while True:
  # Read the next line
  line = rawFile.readline()
  # Summarise elf calories and increment elves
  if len(line) <= 1:
    caloryList.append(calories)
    if largestCalories == -1 or calories > largestCalories:
      largestCalories = calories
    calories = 0
  # end of file
  if not line:
    break
  stripped = line.strip()
  # New elf
  if not stripped:
    continue
  # Counting calories for current elf
  calory = int(stripped)
  calories += calory

print(caloryList)
print("The Elf:", theElf, "has", largestCalories, "calories")

# Assignment
left = 1
boxes = ["box", "box"]

# Comparison (logical comparision)
## Is x equal to y?
if x == y:
<
>
<=
>=

# increment
x = 1
x = x + 1
x += 1
x = x - 1
x -= 1