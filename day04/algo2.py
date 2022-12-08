rawFile = open("input", "r")
sum = 0

while True:
  line = rawFile.readline().strip()
  overlap = 0
  if not line:
    break
  array = line.split(',')
  partners = [[int(i) for i in array[0].split('-')]]
  partners.append([int(i) for i in array[1].split('-')])
  if partners[0][0] > partners[1][0]:
    partners[0], partners[1] = partners[1], partners[0]
  elif partners[0][0] == partners[1][0] and partners[0][1] < partners[1][1]:
    partners[0], partners[1] = partners[1], partners[0]
  if partners[1][0] == partners[0][0] or partners[1][0] <= partners[0][1]:
    overlap = 1
  sum += overlap
  print(partners, overlap)

print(sum)
