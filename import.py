#import subprocess
#subprocess.call('pip install functools --target=D:\UserData\130679900\Downloads\python modules', shell=True)

import os
a = False
print("Leon's python CMD loophole")
while a == False:
    print(":)", end=" ")
    x = input()
    if x == "cd change":
        y = input("Enter the directory to change to: ")
        os.chdir(y)
        os.system("cd")
    else:
        os.system(x)
