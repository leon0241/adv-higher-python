# Maze Program

maze = [[0 for x in range (4)] for y in range(9)]

for x in range(0,9):
    for y in range(0,4):
        maze[x][y] = -1



def Valid_Moves(maze):
    maze[0][1] = 1
    maze[1][1] = 2
    maze[1][2] = 4
    maze[2][2] = 5
    maze[2][3] = 1
    maze[3][1] = 4
    maze[3][2] = 6
    maze[4][0] = 1
    maze[4][3] = 3
    maze[5][0] = 2
    maze[6][0] = 3
    maze[6][1] = 7
    maze[7][1] = 8
    maze[7][3] = 6
    maze[8][3] = 7

    return maze

def change_Room(maze, room, direction):
    newRoom = 0

        
    if (maze[room][direction]) == -1:
        print("You have hit a wall")
    else:
        newRoom = maze[room][direction]
        print("you are now in room " , newRoom)
    return newRoom 

def Get_user_move():
    User_move = input("which move would you like to make?")

    return User_move




#main program

print("You are currently in room 0")

#set inital values for vars 
room = 0
direction = 0

#set valid room moves 
maze = Valid_Moves(maze)


#get next move from user
while room != 8:
    direction = int(Get_user_move())

    #change room 
    room = int(change_Room(maze, room, direction))
    



