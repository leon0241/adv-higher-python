maze = [[0 for x in range(7)] for y in range(7)] #Initialise maze
wallName = "H" #Notation for the wall symbol
doorName = "d" #Notation for the door symbol

def setup_maze(): #Set ups the values in the maze
    walls = [2, 4, 6] #Even numbers for walls
    floors = [1, 3, 5] #Odd numbers for rooms
    mazeSize = 7 #Size of the map (arranged like W0W1W2W)

    #Walls (x)
    for x in range(0, mazeSize):
        maze[x][0] = wallName #Outer Wall(Top)
        maze[x][6] = wallName #Outer Wall(Bottom)
        for i in walls:
            maze[x][i] = wallName #Inner Wall(Wall array)

    #Walls (y)
    for y in range(0, mazeSize):
        maze[0][y] = wallName #Outer Wall(Left)
        maze[6][y] = wallName #Outer Wall(Right)
        for i in walls:
            maze[i][y] = wallName #Inner Wall(Wall array)

    #Floors
    room = 0
    floorArr = [[0 for x in range(2)] for y in range(9)] #2d array (roomNumber * [x, y])
    for i in floors:
        for j in floors:
            maze[i][j] = room
            floorArr[room][0] = i #X-coord of room
            floorArr[room][1] = j #Y-coord of room
            room += 1

    #Doors
    doorArr = [[1, 2], [1, 4], [2, 3], [2, 5], [3, 2], [4, 1], [5, 2], [5, 4]] #Array of arrays(position of doors)
    for i in range(len(doorArr)):
        doorx = doorArr[i][0] #X-coord of door
        doory = doorArr[i][1] #Y-coord of door
        maze[doorx][doory] = doorName #replaces wall at xy with door
    return floorArr #Returns array of floors coordinates

def print_maze(): #Prints the maze on screen as a visual
    line = "" #Empty Line
    for x in range(0, 7): # Repeats per Line
        for y in range(0, 7): #Per Row
            line += " " + str(maze[x][y]) #Adds next maze value
        print(line) #Prints a full line (H0H1H2H3H)
        line = ""

def navigate_maze(ax): #Direction logic checking and user input
    #ax = floorArr
    roomNumber = 0 #Initialise room number
    mazeRunning = True #Set while condition
    while mazeRunning == True:
        #Set up variables
        coordV = ax[roomNumber][0] #X coord
        coordH = ax[roomNumber][1] #Y coord
        wallCheck = [False] * 4 #array(BOOL) - whether there is a wall or not
        newRoomCoords = [] #array(ARRAY) - the coordinates of the next room
        directionNames = ["North", "East", "South", "West"] #array(STR) - Names of each direction
        doorVals = [] #array(STR) - Directions that have doors

        directions = create_directions(coordV, coordH, 1) #Creates array(ARRAY) of 4 "directions" (e.g north is coordV - 1)

        #Finds the possible directions to take and stores it in wallCheck[] and doorVals[]
        for d in range(0, 4): #Repeats 4 times for 4 directions
            direction = directions[d] #var(ARRAY) - direction to check(North, East, South, West)
            if maze[direction[0]][direction[1]] == doorName: #If Maze[] values of directions[x, y] is equal to the character for a door then:
                wallCheck[d] = True #Set wallCheck[index] to true
                doorVals.append(directionNames[d]) #Append direction to doorVals(string from directionNames)
            else: #Else - #If Maze[] values of directions[x, y] is equal to the character for a wall
                wallCheck[d] = False #Set wallCheck[index] to false

        #Sets up text telling the directions to take
        dirText = doorVals[0] #Sets first value of doorVals (So first value doesn't end up with ", ")
        for s in range(1, len(doorVals)): #Repeats from 1 to doorVals length
            dirText += ", " + doorVals[s] #Adds doorVals[index] to a string

        #Prints information to the user about the room they are in
        print("You are in room " + str(roomNumber)) #Print text saying what room you are in
        print("You can move " + dirText) #Print text saying directions you can take(Taken from dirText)

        validMove = False #Set while condition
        while validMove == False:
            #Gets user input for which direction to take
            move = input("Choose a direction (N/E/S/W): ") #Choose from "N", "E", "S", "W"
            #Sets value of move to val (Corresponds to arrays like directionNames or wallCheck)
            if move == "N":
                val = 0 #North - 0
            elif move == "E":
                val = 1 #East - 1
            elif move == "S":
                val = 2 #South - 2
            elif move == "W":
                val = 3 #West - 3
            else:
                print("Invalid command. Please try again") #Error - input that isn't N/E/S/W
                val = 5 #Val = 5 (Highest value)

            if val < 5: #Skip wall check if invalid command
                if wallCheck[val] == False: #Check if value of wallCheck[val] is False (Wall)
                    print("You have hit a wall. You are still in room " + str(roomNumber)) #Prints error message
                else: #Value of wallCheck[val] is True (Door)
                    progressDirections = create_directions(coordV, coordH, 2) #Creates array(ARRAY) of 4 room directions (e.g 0 -> 1 is coordH + 2))
                    newRoomCoords = progressDirections[val] #Set value of newRoomCoords to the coords in the direction set
                    validMove = True #Fulfills while condition

        roomNumber = ax.index(newRoomCoords) #Checks ax for value that matches with newRoomCoords
        if roomNumber == 8: #Checks if roomNumber is 8 (Last room)
            mazeRunning = False #Fulfills while condition
    print("You have completed the maze!") #Print congratulation message


def create_directions(a, b, inc): #Creates a 4 value array containing moves in each direction
    #Vertical, horizontal, increment number (Door/Wall check or Room move)
    directions = [
        [a - inc, b], #North
        [a, b + inc], #East
        [a + inc, b], #South
        [a, b - inc] #West
    ]
    return directions


floorArr = setup_maze() #array of coordinates for each floor
print_maze() #Print Maze
navigate_maze(floorArr)
