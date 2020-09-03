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
        coordX = ax[roomNumber][1]
        coordY = ax[roomNumber][0]

        print("coords: " + str(coordX) + str(coordY))

        directions = [ #room = 1 - 1
            [coordX, (coordY - 1)], #this is north 1 - 0
            [(coordX + 1), coordY], #this is east 2 - 1
            [coordX, (coordY + 1)], #this is south 1 - 2
            [(coordX - 1), coordY]  #this is west 0 - 1
        ]

        print("X" + str(directions[0][0]) + "Y" + str(directions[0][1]))
        print("X" + str(directions[1][0]) + "Y" + str(directions[1][1]))
        print("X" + str(directions[2][0]) + "Y" + str(directions[2][1]))
        print("X" + str(directions[3][0]) + "Y" + str(directions[3][1]))

        #for i in range(0, 3):
        if maze[directions[0][0]][directions[0][1]] == wallName:
            wallCheck[0] = False
        else:
            wallCheck[0] = True
        print("X:" + str(directions[0][0]) + "Y:" + str(directions[0][1]) + maze[directions[0][0]][directions[0][1]] )

        if maze[directions[1][0]][directions[1][1]] == wallName:
            wallCheck[1] = False
        else:
            wallCheck[1] = True
        print("X:" + str(directions[1][0]) + "Y:" + str(directions[1][1]) + maze[directions[1][0]][directions[1][1]])

        if maze[directions[2][0]][directions[2][1]] == wallName:
            wallCheck[2] = False
        else:
            wallCheck[2] = True
        print("X:" + str(directions[2][0]) + "Y:" + str(directions[2][1]) + maze[directions[2][0]][directions[2][1]])

        if maze[directions[3][0]][directions[3][1]] == wallName:
            wallCheck[3] = False
        else:
            wallCheck[3] = True
        print("X:" + str(directions[3][0]) + "Y:" + str(directions[3][1]) + maze[directions[3][0]][directions[3][1]])

        print(wallCheck)

        roomNumber += 1

floorArr, doorArr = setup_maze()
print_maze()
print(floorArr)
navigate_maze(floorArr, doorArr)
