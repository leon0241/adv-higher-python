for i in range(10):
    result = int(input("what percentage did you get? "))

    if result >= 90:
        print("you got an A")
    elif result >= 80:
        print("you got an B")
    elif result >= 50:
        print("you got an C")
    elif result >= 40:
        print("you got an D")
    else:
        print("you fail")
