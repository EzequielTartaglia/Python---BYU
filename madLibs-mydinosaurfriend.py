#Others vars

UNDERLINE = '\033[4m'
END = '\033[0m'
YELLOW = '\033[33m'

print ("Please enter the following: ")
print('')

#Input to the user

name = input("Name: ")
nameCapitalize = name.capitalize() ##Convert name to capitalize
nameUPPER = name.upper() ##Convert name to upper
animal = input("Animal: ")
animalLower = animal.lower() ##Convert animal to lower
adjetive = input ("Adjetive: ")
adjetiveLower = adjetive.lower() ##Convert adjetive to lower
timeAgo = input("Number and Time(Example: 2 hours): ")
verb = input("Verb: ")
verbLower = verb.lower() ##Convert verb to lower
weight = input("Number (Example: 20): ")
housing = input("Type of Housing(Examples: Apartment|House|Hut): ")
housingLower = housing.lower() ##Convert housing to lower

print('')
print("Your Story is: ")
print('')

#Start of the Mad libs (text)

print(f"{UNDERLINE}FINEDING ONE HOME TO MY DINOSAUR:{YELLOW+UNDERLINE+nameUPPER+END}")
print('')
print('')
print( YELLOW+UNDERLINE+nameCapitalize+END+ ' is a dinosaur very similar like a ' +YELLOW+
UNDERLINE+animal +END+ ' and incredibly ' +YELLOW+UNDERLINE+adjetive+END + '! I found it ' +YELLOW+UNDERLINE+timeAgo+END+ ' ago. Something i love about my new friend is when it ' 
+YELLOW+UNDERLINE+verb+END+ ' with me, I will could to see it doing this for hours, but for other part i have a little problem ' +YELLOW+UNDERLINE+nameCapitalize 
+END+ ' weighs ' +YELLOW+UNDERLINE+weight+END+ ' tons! So its dangerous for ' +YELLOW+UNDERLINE+name+END+ ' to live in my ' +YELLOW+UNDERLINE+housing+END+
".I think I'll never see another dinosaur again if something happens to it. Could you take care of it for me? " )
print('')
print('')

        #Answer(The final of the story)
answer = input(f"Will do adopt {YELLOW+UNDERLINE+nameCapitalize+END}?  - Choose(Yes | No): - ")
answerUPPER = answer.upper() ##Convert name to upper
print('')
print(f"You choose {YELLOW+UNDERLINE+answerUPPER+END} .If I have to tell you a secret. it was really a great idea, but this is not the last time you will hear about the story from {YELLOW+UNDERLINE+nameCapitalize+END}")
print('')
print('Will be continue...')
print('THE END!')
