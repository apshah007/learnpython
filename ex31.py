print (""" you enter a dark room with two doors.
Do you go through door # 1,  door # 2, or door #3?""")

door = input("> ")

if door == "1":
    print("there is a giant bear here eatng cheese cake.")
    print("What do you do?")
    print("1. take the cake.")
    print("2. scream at the bear.")

    bear = input (">")

    if bear == "1":
        print("The bear eats your face off.  good job!")
    elif bear == "2":
        print("the bear eats your legs off. good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away")

elif door == "2":
    print("you stare into the endless abyss at Chthulu's retina.")
    print("1 blueberries")
    print("2 yellow jacket clothespins")
    print("3 understanding revolvers yelling melodies")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("good job")
    else:
        print("the insanity rots your eyes into a pool of muck.")
        print("good job")

elif door == "3":
    print("you enter the medical school morgue")
    print("all the lights go out and the electronic door cant be opened")
    print("you are consumed by zombies")
    
else:
    print("you stumble around and fall on a knife and die good job!")
