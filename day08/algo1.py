class LineOfSight:
    def __init__(self, rows, cols):
        self.map = [[0] * cols for i in range(rows)]
        self.rows = rows
        self.cols = cols
        self.map[0] = [1] * cols
        self.map[rows - 1] = [1] * cols
        for i in range(1, rows - 1):
            self.map[i][0] = 1
            self.map[i][cols - 1] = 1

    def traceLeft(self, snapshot):
        for rId, row in enumerate(snapshot[1:-1]):
            highest = row[0]
            for cId, tree in enumerate(row[1:-1]):
                if tree > highest:
                    self.map[rId + 1][cId + 1] = 1
                    highest = tree
    
    def traceRight(self, snapshot):
        for rId, row in enumerate(snapshot[1:-1]):
            highest = row[-1]
            for cId, tree in reversed(list(enumerate(row[1:-1]))):
                if tree > highest:
                    self.map[rId + 1][cId + 1] = 1
                    highest = tree
    
    def traceTop(self, snapshot):
        for col in range(1, self.cols - 1):
            highest = snapshot[0][col]
            for row in range(1, self.rows - 1):
                tree = snapshot[row][col]
                if tree > highest:
                    self.map[row][col] = 1
                    highest = tree

    def traceBottom(self, snapshot):
        for col in range(1, self.cols - 1):
            highest = snapshot[0][col]
            for row in range(self.rows - 1, 1, -1):
                tree = snapshot[row][col]
                if tree > highest:
                    self.map[row][col] = 1
                    highest = tree

    def traceMap(self, snapshot):
        self.traceLeft(snapshot)
        self.traceRight(snapshot)
        self.traceTop(snapshot)
        self.traceBottom(snapshot)

    def getVisible(self):
        return sum(sum(self.map, []))

    def __str__(self):
        return f"{self.map}"

def constructMap(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    rows = len(lines)
    cols = len(lines[0])
    snapshot = []
    for line in lines:
        snapshot.append([int(value) for value in line])
    return rows, cols, snapshot;

rows, cols, snapshot = constructMap("input.txt")
lineOfSight = LineOfSight(rows,cols)

lineOfSight.traceMap(snapshot)
print(snapshot)
print(rows,cols)
print(lineOfSight.getVisible())
