
#import mystuff
#mystuff.apple()
#print(mystuff.tangerine)

#mystuff['apple'] #get apple from dict
#mystuff.apple() #get apple from the module
#mystuff.tangerine #same thing, its just a variable

#class MyStuff(object):
#    def __init__(self):
#        self.tangerine = "and now a thousand years between"

#    def apple(self):
#        print("I AM CLASSY APPLES!")

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#happy_bday = Song(["Happy birthday to you",
#                    "I dont want to get sued",
#                    "So I'll stop right there"])

#bulls_on_parade = Song(["They rally around tha family",
#                       "With pockets full of shells"])

heartless = Song(["In the night, I hear 'em talk",
"The coldest story ever told",
"Somewhere far along this road, he lost his soul to a woman so heartless",
"How could you be so heartless?",
"Oh, how could you be so heartless?",
"How could you be so, cold as the winter wind when it breeze, yo",
"Just remember that you talkin' to me though",
"You know need to watch the way you talkin' to me, yo",
"I mean after all the things that we've been through",
"I mean after all the things we got into",
"Hey yo, I know of some things that you ain't told me",
"Hey yo, I did some things but that's the old me",
"And now you wanna get me back and you goin' show me",
"So you walk around like you don't know me",
"You got a new friend, well I got homies",
"But in the end it's still so lonely",
"In the night, I hear 'em talk",
"The coldest story ever told",
"Somewhere far along this road, he lost his soul to a woman so heartless",
"How could you be so heartless?",
"Oh, how could you be so heartless?",
"How could be so Dr. Evil, you bringin' out a side of me that I don't know",
"I decided we weren't goin' speak so",
"Why we up three A.M. on the phone",
"Why does she be so mad at me for",
"Homie I don't know, she's hot and cold",
"I won't stop, I won't mess my groove up",
"Cause I already know how this thing go",
"You run and tell your friends that you're leaving me",
"They say that they don't see what you see in me",
"You wait a couple months then you gon' see",
"You'll never find nobody better than me",
"In the night, I hear 'em talk",
"The coldest story ever told",
"Somewhere far along this road, he lost his soul to a woman so heartless",
"How could you be so heartless?",
"Oh, how could you be so heartless?",
"Talkin', talkin', talkin', talk",
"Baby let's just knock it off",
"They don't know what we been through",
"They don't know 'bout me and you",
"So I got something new to see",
"And you just goin' keep hatin' me",
"And we just goin' be enemies",
"I know you can't believe",
"I could just leave it wrong",
"I'm goin' take off tonight",
"Into the night",
"In the night, I hear 'em talk",
"The coldest story ever told",
"Somewhere far along this road, he lost his soul to a woman so heartless",
"How could you be so heartless?",
"Oh, how could you be so heartless?"])

#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()


print("\n\n\n\n\n")
heartless.sing_me_a_song()
print("\n\n\n\n\n")
