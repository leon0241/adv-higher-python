maze = [[0 for x in range(7)] for y in range(7)]
wallName = "H"
doorName = "d"

def setup_maze():
    walls = [2, 4, 6]
    floors = [1, 3, 5]
    mazeSize = 7

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
    mazeRunning = True
    wallCheck = [False] * 4
    while mazeRunning == True:
        coordV = ax[roomNumber][0] #X coord
        coordH = ax[roomNumber][1] #Y coord
        newRoomCoords = []

        directions = create_directions(coordV, coordH, 1)

        directionNames = ["North", "East", "South", "West"]
        doorVals = []

        for d in range(0, 4):
            direction = directions[d]
            if maze[direction[0]][direction[1]] == doorName:
                wallCheck[d] = True
                doorVals.append(directionNames[d])
            else:
                wallCheck[d] = False

        dirText = doorVals[0]
        for v in range(1, len(doorVals)):
            dirText += ", " + doorVals[v]

        print("You are in room " + str(roomNumber))
        print("You can move " + dirText)

        validMove = False
        while validMove == False:
            move = input("Choose a direction (N/E/S/W): ")
            if move == "N":
                val = 0
            elif move == "E":
                val = 1
            elif move == "S":
                val = 2
            elif move == "W":
                val = 3
            else:
                print("Invalid command. Please try again")
                val = 5

            if val < 5:
                if wallCheck[val] == False:
                    print("You have hit a wall. You are still in room " + str(roomNumber))
                else:
                    progressDirections = create_directions(coordV, coordH, 2)
                    newRoomCoords = progressDirections[val]
                    validMove = True

        roomNumber = ax.index(newRoomCoords)
        if roomNumber == 8:
            mazeRunning = False
    print("You have completed the maze!")


def create_directions(a, b, inc):
    directions = [
        [a - inc, b], #North
        [a, b + inc], #East
        [a + inc, b], #South
        [a, b - inc] #West
    ]
    return directions


floorArr, doorArr = setup_maze()
print(maze)
print_maze()
navigate_maze(floorArr, doorArr)
