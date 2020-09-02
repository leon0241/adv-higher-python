maze = [[0 for x in range(7)] for y in range(7)]

def setup_maze():
    walls = [2, 4, 6]
    floors = [1, 3, 5]
    mazeSize = 7
    wallName = "□"
    doorName = "d"

    #Walls (x)
    for x in range(0, mazeSize):
        maze[x][0] = wallName
        maze[x][6] = wallName
        for i in walls:
            maze[x][i] = wallName

    #Walls (y)
    for y in range(0, mazeSize):
        maze[0][y] = wallName
        maze[6][y] = wallName
        for i in walls:
            maze[i][y] = wallName

    #Floors
    room = 0
    floorArr = [[0 for x in range(2)] for y in range(9)]
    for i in floors:
        for j in floors:
            maze[i][j] = room
            floorArr[room][0] = i
            floorArr[room][1] = j
            room += 1

    #Doors
    doorArr = [[1, 2], [1, 4], [2, 3], [2, 5], [3, 2], [4, 1], [5, 2], [5, 4]]
    for i in range(len(doorArr)):
        doorx = doorArr[i][0]
        doory = doorArr[i][1]
        maze[doorx][doory] = doorName

    return floorArr, doorArr

def print_maze():
    line = ""
    for x in range(0, 7):
        for y in range(0, 7):
            line = line + " " + str(maze[x][y])
        print(line)
        line = ""

def navigate_maze(ax, ay):
    roomNumber = 0
    for i in range(0, 3):
        coordX = ax[roomNumber][0]
        coordY = ax[roomNumber][1]
        print(coordX)
        print(coordY)
        roomNumber += 1

floorArr, doorArr = setup_maze()
print_maze()
print(floorArr)
navigate_maze(floorArr, doorArr)
