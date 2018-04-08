pine = int(input("Please tell me a number greater than 3  "))
additive = int(input("Please input a number: 1, 2, or 3 "))
numbers = []
def fence(count, additive):
    i = 0
    numbers = []
    while i < pine:
        print(f"At the top i is {i}")
        numbers.append(i)
        print(i)
        i =  i + additive
        print(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        print("The numbers: ")
        for num in numbers:
            print(num)
count = pine
fence(count, additive)
