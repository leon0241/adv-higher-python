values = int(input("how many values are there? "))
total = 0

for counter in range(0, values):
    userinput = int(input("enter a value"))
    total = userinput + total
print(total)
