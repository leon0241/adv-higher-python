print("the equation program")

print("please select an option from the following menu")
print("  1. calculate the speed")
print("  2. calculate the distance")
print("  3. calculate the time")
print("  4. calculate the area of a rectangular room")
print("  5. exit program")

selection = input()

if selection == "1":
    time = input("what's the time? ")
    distance = input("what's the distance? ")
    speed = round((int(distance) / int(time)), 2)
    print("speed is: " + str(speed) + "m/s")
elif selection == "2":
    time = input("what's the time? ")
    speed = input("what's the speed? ")
    distance = time * speed
    print("distance is: " + str(distance) + "m")
elif selection == "3":
    distance = input("what's the distance? ")
    speed = input("what's the speed? ")
    time = round((int(distance) / int(speed)), 2)
    print("time is: " + str(time) + "s")
elif selection == "4":
    length = int(input("what's the length of the room"))
    breadth = int(input("what's the breadth of the room"))
    height = int(input("what's the height of the room"))

    area = length * breadth * height
    print(area)
else:
    exit()
