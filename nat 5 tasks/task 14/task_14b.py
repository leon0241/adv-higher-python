name = [""]*5
score = [""]*5
passed = [""]*5

for i in range(5):
    name[i] = input("enter your name")
    score[i] = int(input("enter your score out of 150"))
    if score[i] / 150 > 0.7:
        passed[i] = name[i]

for i in range(5):
    print(passed[i])
