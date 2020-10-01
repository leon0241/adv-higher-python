import os
a = False
print("Leon's python CMD loophole")
print("Commands: cd change")
while a == False:
    print(":)", end=" ")
    x = input()
    if x == "cd change":
        y = input("Enter the directory to change to: ")
        os.chdir(y)
        os.system("cd")
    else:
        os.system(x)
