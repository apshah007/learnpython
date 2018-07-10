"""choose your own adventure game"""

    
"""Functions for the first door"""

def hot_door():
    print("When walking through the hot door you notice as soon as you get into \
the vestibule the door slams shut behind you and locks with a click.  You enter \
further into the space able stand tall because the room is large.  Suddenly, \
fluorescent lights flip on and you are not alone.  Three men dressed in police \
officer uniforms sit in rolling chairs in the room.  Each has turned lazily to \
stare at you with guns in their hands.   One says. 'Lay down, face down on the \
floor'  You are captured!")
    endgame()
   

def double_door():
    print("The double door is heavy and large. As you push your way through it, \
you catch your foot against one of the heavy doors.  Your foot is injured severely. \
You are able to walk with a limp but you are very tired,  You see the door has led \
to a quiet dark passage unfinished like a dirty tunnel.   It is perhaps an old subway \
you begin limping towards a distant light at the end of the tunnel.  Your ears are\
perked up and listening to all the sounds around.  You hear the scurry of animals \
and you know you are surrounded by rats.  The rats sense your frailty and see you \
limping so slowly.  They attack and you rush towards the light to no avail.  You \
are eaten alive by the rats. ")
    endgame()


def small_door():
    print("The small door you enter leads to a group of 3 doors in a small hallway. \
Each door has a rubik's cube attached to the door handle by a thick wire.  You are \
a modest genius so you spend the next hours deciphering each cube.  You are able to \
open all the doors. But the sign above the doors says you must choose only one \
to walk through  For if you open one door, the other two will lock back up.  The \
doors are identical. ")
    second_choice = int(input("So you choose...  1, 2, 3?"))
    small_door_choices(second_choice)


"""Conditional statement for the the second door"""

def small_door_choices(second_choice):
    if second_choice == 1:
        print("Being of extraordinary physical stamina and beauty, you happen to see \
your reflection in the first door and you decide 'What the hell? You choose that door \
and walk through.  A velvet curtain draws open.  Suddenly there is a crowd of people \
sitting in bleachers and you are out in the open.  The blue sky is filled with golden \
light.  And a fuchsia light is placed on your and you realize you are in a theatre. \
The crowd screams.  'Dance! Dance! Dance!'  In your home country you had access to two \
music videos: Beyonce's Single Ladies and the final dance scene from Napoleon Dynamite.\
You dance with the panache of both and receive a standing ovation. ")
        red_carpet()

    elif second_choice == 2:
        print("Having experience working at a nuclear power plant and enjoying doughnuts \
    You are a native of Simpsonland.  But are willing to learn more about a new land \
    provided there is beer.  After exiting through the second door, you use your hand gestures \
    to find the nearest bar and you make money and friends belching the national anthem of \
    your new country for the crowd")
        beer_cave()

    elif second_choice == 3:
        print("You have chosen the third door and exit to a street where suddenly someone \
takes a picture of you and runs away. A black car drives up beside you as you walk down the \
street and insists of following you slowly. You stop and turn and a woman with a gray suit \
comes out of the car.  She has traditional Slavic features with a pleasing affect.  You know \
her well.  And you get into the car unafraid.")
        land_o_milk_honey()
    else:
        print("You did not choose a door.")

    
"""Functions for the End results"""

def beer_cave():
    print("You are enjoying beer and bar food in a dive bar.")

def land_o_milk_honey():
    print("You made it to the land of milk and honey")

def red_carpet():
    print("Since you have a remarkable talent, you have been asked to walk the\
red carpet.  If you play your cards right you will gain citizenship")

def endgame():
    print("Unfortunately your bid to enter this country is over. Rise another day.")


""" main program """

if __name__ == "__main__":

    print("You have traveled to a foreign country as a refugee.  You have only \
belongings enough to carry in a plastic bag. You have traveled 20 miles today \
foot through a desert and you are in poor shape.  In front of you is a wall\
seeming so tall you cannot see the top of it.  There are three doors in front \
of you.  They may lead to an uncertain fate, but you dont think you can \
climb the wall.  The first door is made of wood and its metal handle is hot to the\
touch.  The second door is double wide and gray in color.  The third door is \
small and you would have to squeeze through")

    choice = int(input("Which door will be your choice?  1, 2 or 3  "))

    if choice == 1:
        print("You take the plastic bag and cover your hand with it as your turn the \
handle of the door.  It is so hot you draw your hand away. But the door is opened \
and its ajar.  You are in pain but you kick the door open the rest of the way. \
And walk through...")
        hot_door()
    elif choice == 2:
        print("You touch the surface of the door and notice the door is strangely \
cold.  You press your hand against of the handle and it bites you because of its \
icy touch.  Nevertheless you are able to push it open. ")
        double_door()
    elif choice == 3:
        print("This door is locked, but you are able to use a piece of wire to jimmy \
the lock open.  The door is small but you are able to crawl through.  ")
        small_door()
    else:
        print("You did not choose one of the three doors.") 
