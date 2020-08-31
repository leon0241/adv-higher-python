number = 69
guess = 0

while guess != number:
    guess = int(input("guess a number: "))
    if guess > number:
        print("too high")
    if guess < number:
        print("too low")
print("nice.")
