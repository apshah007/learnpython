# 3 of seven deadly sins game
# sequel seven cirlces of hell game
from sys import exit

chapel = False
cave = False
tax = False
state = False

def beer_cave():
    print("This room is full of alcoholic beverages and scantily clad models. You are married do you leave or stay?")
    global cave
    cave = True
    choice = input("> ")
    if choice == "leave":
        dead("You go to heaven, but you are not an angel and have no wings")
    elif choice == "stay":
        dead("You contract the super antibiotic resistant form of gonorrhea that's going around")
    else:
        print("You become a digital character stuck in the movie Fear because you did not choose. Try again.")

def tax_auditor_office():
    print("You have lied on your taxes.  And the tax auditor is easily bribed.  How much will you give them?")
    global tax
    tax = True
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Tax man dont play that shit.")
    if how_much == 1000:
        dead("Nice you got the bribe correct.  You win this year!")
    else:
        dead("Wrong answer, man.  Tax man cometh. Try again.")

def chapel_of_heartbreak():
    print("Since your baby left you, you have no place to go.  But you found yourself in the Chapel of Heartbreak with an ogre.  Do you stay or do you leave?")
    global chapel
    chapel = True
    choice = input("> ")
    if choice == "stay":
        dead("Wedding bells for you and Ogre dahling.",)
    elif choice == "leave":
        dead("No one leaves Ogre at the altar, nobody.  You are dead meat.  And scrumptious!")
    else:
        print("Sometimes you have got to choose.  Leave or Stay, try again!")

def dead(why):
    print(why, "Give a little, get a little. Good job!")
    if (tax and chapel and cave == True):
        global state
        state = True
        exit(0)
    elif (tax or chapel or cave == False):
        start()

def start():
    while (state == False):
        print("\n\n\n\n")
        print("You are committing the seven deadly sins in no particular order and for no particular reason")
        print("You are in dark room")
        print("There are 3 doors: 1, 2, 3")
        print("Choose a door")

        choice = input(">  ")

        if choice == "1":
            chapel_of_heartbreak()
        elif choice == "2":
            tax_auditor_office()
        elif choice == "3":
            beer_cave()
        else:
            print("You enter purgatory and wait for there for a really long time")







start()
