#General var

UNDERLINE = '\033[4m'
END = '\033[0m'
ROJO = '\033[31m'

#Adventure game
print('')
print("CREATE YOUR OWN STORY")
print('')
print('The Dungeon of Camelot')
#Introduction scenario
print('')
principal_weapon_election = input("You wake up in a strange dungeon and start to walk. You are walking through this dark dungeon and find two items: a DRAGON COMBAT "+ROJO+"GLOVES"+END+" with the ability to create light when they move through the gems that are in them on the shape of dragon eyes  and a "+ROJO+"STAFF"+END+" OF FIRE with the ability to launch small fireballs. Which one do you want to pick up? ")

#Principal weapon election

    #DRAGON COMBAT GLOVES ELECTION
if principal_weapon_election.upper() == "GLOVES":
    print('')
    road_split = input("You choose to pick up the DRAGON COMBAT "+ROJO+"GLOVES "+END+"You realize that for it to show a light for 15 seconds you must make a sudden and dry movement, that implies that someone or something can hear you, so you try to only make these movements in case you need it. Suddenly, you hear footsteps similar to those of an orc approaching your positions. It's necesary to project some light in order to find a way out, so you do, but unfortunately the orc was looking at your position and starts running towards you. You run for a few meters until you get a place where the path splits. Should you choose to go, "+ROJO+"RIGHT "+END+"or "+ROJO+"LEFT"+END+"? ")



        #ROAD SPLIT SELECTION

            #Choose: "Left"
    if road_split.upper() == "LEFT":
        print('')
        print("You choose to go to the "+ROJO+"LEFT"+END+".You continue down that path until reach a dead end and decide to fight with the orc. The orc hit your arm with his axe and start to lose blood, but you don't give up.the fight was intense, but you were able to win.your wound got worse, so you start looking for a bandage. You found something similar and try to use it. You search for the exit for a while longer, but without achieving success, you decide to live here devoting your life to improving your hunting skills and fighting with stronger and stronger monsters and finally become the master of the dungeon.") 
        print('')
        print('The end!')
        print('')

            #Choose: "Right"      
    elif road_split.upper() == "RIGHT":
        print('')
        print("You choose to go to the "+ROJO+"RIGHT"+END+".You continue down that path until you start to see until you start to see a light on the horizon, your eyes start to shine and you think that this nightmare was about to end. Accelerate your career even more and go out for a little hole. The orc can't follow you, so you walk through the forest and find a village. You decide to become a warrior and live in this place for a long time to protect them.") 
        print('')
        print('The end!')
        print('') 
            #Not decide to choose one path
    else:
        print("You choose to not pick up "+ROJO+"LEFT "+END+"or "+ROJO+"RIGHT"+END+".You look at the road for a long time and the orc catches you when you get distracted. The orc crushes you and you die right now.")
        print('')
        print('The end!')
        print('')



    #STAFF OF FIRE ELECTION
           
elif principal_weapon_election.upper() == "STAFF":
    print('')
    mistery_mission = input("You choose to pick up the "+ROJO+"STAFF"+END+" OF FIRE. In the same moment you pick it with your left hand you begin to see that your right arm and the right part of your face begins to metamorphize and the anatomy of your arm becomes volcanic, like a golem of lava. And as if that were not enough, you begin to hear the ancestral voice of a mythological magician who And as if that were not enough, you begin to hear the ancestral voice of a mythological wizard who asks you to break a crystal that Thram guards, one of the highest-ranking orcs in the dungeon. Do you choose "+ROJO+"ACCEPT "+END+"this mission or "+ROJO+"NO"+END+"? ")
     #Choose: "ACCEPT"

    if mistery_mission.upper() == "ACCEPT":
        print('')
        print("You choose "+ROJO+"ACCEPT"+END+" the mission.You start to follow the instructions of that voice and you find the orc Thram while he was sleeping. Very cautiously, you approach her neck and remove the crystal. The voice tells you 'break your fast and I promise you that you won't have to suffer anymore in this dungeon' and you decide to listen to it even though you still did not fully trust this voice. At this time the rest of your body metamorphose and you become a lava man. You think this is good at some point, but the voice says 'never trust strangers', the lava starts to dull and solidify more and you petrify forever. At that moment, the crystal rejoins and returns to the neck of that orc until the next person who trusts the cursed fire staff.") 
        print('')
        print('The end!')
        print('')

         #Choose: "NO"   
                 
    else: 
        print('')
        share_knowledge = input("You choose to "+ROJO+"NO"+END+" accept this strange mission.You continue down that path until you start to see until you start to see a light on the horizon, your eyes start to shine and you think that this nightmare was about to end. Accelerate your career even more and go out for a little hole. so you walk through the forest and find a village. the people there are very kind and accept you despite your metamorphosis, in gratitude you become a wizard to protect them forever, you also discover the way to pass this magical power. Do you choose to "+ROJO+"SHARE "+END+"your magical power with the people of the village or do you choose "+ROJO+"NOT SHARE "+END+"? ")  
        print('')
        if share_knowledge.capitalize() == "Share":
            print("You choose "+ROJO+"SHARE "+END+"your knowledge. So, you decide to create a magic school to share how to get this magical power and help the people of this village to be able to control it. you manage to create an army of wizards to defend this place by threats.") 
            print('')
            print('The end!')
            print('') 
        elif share_knowledge.capitalize() == "Not share":
            print("You choose "+ROJO+"NOT SHARE "+END+"this power.So, You live to serve in this city with your magical powers, but when you get older this secret dies with you.")
            print('')
            print('The end!')
            print('') 
        else:
            print("You don't choose any of this options. You aren't sure sharing this power so You live to serve in this city with your magical powers, but when you get older this secret dies with you.")
            print('')
            print('The end!')
            print('') 
        

    

    #NOT DECIDE TO GRAB ANY OBJECT
else: 
    print('')
    print("You choose to not pick up "+ROJO+"GLOVES "+END+"or "+ROJO+"STAFF"+END+". You can't see nothing arround you and finally you're lost forever.")
    print('')
    print('The end!')
    print('')