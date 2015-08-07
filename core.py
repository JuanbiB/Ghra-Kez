import time
import random
import sentient


class Room(object):
    def __init__(self, x, y, description, description_2, container, container_type, content, monster, lock, valid_directions):
        self.x = x  # x position of room
        self.y = y  # y position of room
        # The grid is a normal one, that is, x increases to the right, and y increases upwards.
        self.container = container  # Is there a lootable container in the room, if so, what is it?
        self.container_type = container_type  # The command needed to open the container.
        self.content = content  # What is actually in the container, the command to equip it and the stats it gives.
        self.monster = monster  # Is there a monster in the room, if so, what is it?
        self.description = description  # The description of the room.
        self.description_2 = description_2  # The description you get once you've been there before (to avoid being repetitive)
        self.counter = 0  # Set to determine whether you've visited a room before or not.
        self.lock = lock  # Variable to see whether or not a room is locked.
        self.valid_directions = valid_directions


class Ghostroom(object):  # Class created for when the player tries to go to places that don't exist.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.valid_directions = "none"


def action(i, north, south, east, west):
    if i.lock == True:

        if user.key > 0:
            print()
            print("Using key to unlock door...")
            time.sleep(.5)
            print("You unlock the door using your key!")
            print("As you use it, it dissolves to dust...")
            print()

            i.lock = False
            user.key -= 1

            # The door simply opens, but the player doesn't go in.
            if north == 1:
                user.y -= 1

            elif east == 1:
                user.x -= 1

            elif south == 1:
                user.y += 1

            elif west == 1:
                user.x += 1

        else:
            print()
            print("That direction is locked.")
            print()

            if north == 1:
                user.y -= 1

            elif east == 1:
                user.x -= 1

            elif south == 1:
                user.y += 1

            elif west == 1:
                user.x += 1

    elif i.counter == 0:
        # These two variables below are set so that the player can skip the "survey" part if they want and go straight to "open chest".
        user.container = i.container_type
        user.content = i.content
        print(i.description)
       # Increasing the counter to keep track of whether the player has visited that room before or not. If he's already been there, the description will be different.
        i.counter += 1
        if i.monster != "nothing":
            print()
            time.sleep(3)
            print(i.monster[0])
            d = input("- ")
            if d == "yes" or d == "yeah" or d == "fight" or d == "kill":
                x = 0
                while x != 2:
                    user.kill(i.monster[1])
                    if user.dead == True:
                        print("It has overpowered you. You fall into darkness and blood.")
                        print()
                        print("###################")
                        print("//////////////////")
                        print("G A M E  O V E R")
                        print("###################")
                        print("//////////////////")
                        exit()
                    if i.monster[1].dead == True:
                        i.monster = "nothing"
                        x = 2
            else:
                print("You flee in terror back to where you were.")
                if north == 1:
                    user.y -= 1

                elif east == 1:
                    user.x -= 1
    
                elif south == 1:
                    user.y += 1
    
                elif west == 1:
                    user.x += 1
                
    else:
        print(i.description_2)
        user.container = i.container_type
        user.content = i.content
        if i.monster != "nothing":
            print()
            print(i.monster[0])
            d = input("- ")
            if d == "yes" or d == "yeah" or d == "fight" or d == "kill":
                x = 0
                
                while x != 2:
                    user.kill(i.monster[1])
                    if user.dead == True:
                        print()
                        print("You fall into darkness and blood.")
                        print("###################")
                        print("//////////////////")
                        print("G A M E  O V E R")
                        print("###################")
                        print("//////////////////")
                        exit()
                    if i.monster[1].dead == True:
                        i.monster = "nothing"
                        x = 2
            else:
                print("You flee in terror back to where you were.")
                if north == 1:
                    user.y -= 1

                elif east == 1:
                    user.x -= 1
    
                elif south == 1:
                    user.y += 1
    
                elif west == 1:
                    user.x += 1

# SENTIENT BEINGS
user = sentient.Player()
flesh_eater = sentient.Monster("Flesh Eater", 30, 10)
necromancer = sentient.Monster("Necromancer", 35, 20)
banshee = sentient.Monster("Banshee", 45, 15)
lizard_king = sentient.Monster("Lizard King", 100, 5)
mutant_earthworm = sentient.Monster("Mutant Earthworm", 60, 10)
statue = sentient.Monster("Ancient Statue", 10, 10)
hydra = sentient.Monster("Hydra", 60, 20)
gladiator = sentient.Monster("Gladiator", 60, 20)
hawk = sentient.Monster("Hawk", 65, 15)

# This is the actual output the player will read, which will guide him.
# first_room
r1_description = "You awaken in a dark, damp place. You are dressed in tattered rags.\nA meager ray of sunlight struggles through a crack on the vine covered wall.\nThere are appears to be a door to the north and the east. The one to the north is adorned by silver etchings."
r1_description_2 = "You're back the room you woke up in. The silver etched door is still there."
r1_container = "nothing"
r1_container_type = "nothing"
r1_monster = "nothing"
r1_content = ["na"]
r1_lock = False
r1_valid_directions = ["west", "east", "south"]

# second_room
r2_description = "You open the door to the east. It whines on its hinges and far away you hear a muffled scream.\nThere appears to be rotten flesh lying on the ground. The smell is putrid."
r2_description_2 = "You're in the putrid-smelling room. The mangled corpse of the monstrosity lays askew on the floor."
r2_container = "You find a small, wooden chest on the side of the room, hidden under cobwebs."
r2_container_type = "open chest"
r2_monster = "nothing"
r2_content = ["Inside, you find a rusty dagger, even though its aged, you can tell the grip and cross-guard are gold.", "take dagger", "You now have 10 base attack. It's not much... but you're going to need it.", "weapon", 10]
r2_lock = False
r2_valid_directions = ["west", "east"]

# third_room
r3_description = "You enter a room lit by a feeble torch. Vine and moss cover the walls.\nThe stones feel frigid under your bare feet."
r3_description_2 = "You're in the room lit by a torch. A feeble breeze escapes through the cracks of the stones."
r3_container = "nothing"
r3_container_type = "nothing"
r3_monster = ["Illuminated by the glow, you see a figure huddled over another, slurping and crunching sounds arising.\nYou feel sick to your stomach. The figure turns and two tendrils protrude from its mouth as is licks its lips,\nundoubtedly at the sight of your living flesh.\nWill you fight?", flesh_eater]
r3_content = ["nada"]
r3_lock = False
r3_valid_directions = ["south", "east", "west"]

# fourth_room
r4_description = "You step over the mangled corpse of your foe as you enter the room to the east.\nInside you see a wooden table with a single lit candle on top.\nA wooden bowl on the table holds animal entrails."
r4_description_2 = "You're in the room with the candle on the table."
r4_container = "You pat down the necromancer's emaciated body and find small ivory box in one his pockets."
r4_container_type = "open box"
r4_monster = ["Sitting on the table you see a man dressed in a black robe.\nHe smiles and his coal red eyes glimmer in the candlelight.\nThe entirety of his left cheek is missing and his jawbone clicks he begins to chuckle.\nWill you engage?", necromancer]
r4_content = ["Inside, lined with velvet, there gleams a silver key.", "take key", "You now have a key, it may grant you access to places otherwise locked.", "key", 1]
r4_lock = False
r4_valid_directions = ["east"]

# fifth_room
r5_description = "You take the door to the north and enter a very small room.\nThere's chain contraptions hanging over the ceiling some which gleam scarlet and appear recently used.\nYou almost trip over a severed limb laying on the floor. There appears to be a door only to the east."
r5_description_2 = "It's the room with metal contraptions and a severed limb."
r5_container = "You notice a rat scurrying by, holding a small linen bag in its teeth.\nYou pin it to the ground and take the bag from its teeth, it stares at you malevolently until you release it scampers away."
r5_container_type = "open bag"
r5_monster = "nothing"
r5_content = ["Inside the bag you find a rusty key!", "take key", "You now have a key to use.", "key", 1]
r5_lock = False
r5_valid_directions = ["north", "west"]

#sixth_room
r6_description = "Taking the door to the east you come upon a relatively bright room lit by four torches.\nThe heat provides relief for your sore fingers. There are no other doors besides the one you came in through."
r6_description_2 = "You're in the bright room with four torches."
r6_container = "On the far side of the room, you find a wooden coffin. It seems to lay halfway open..."
r6_container_type = "open coffin"
r6_monster = "nothing"
r6_content = ["Inside you find a corpse clutching a leather hide vest, this will probably serve as protection and warmth.", "take vest", "You take the vest from the poor soul. You now have armor, therefore, an increase in health.", "armor", 20]
r6_lock = True
r6_valid_directions = ["east"]

#seventh_room
r7_description = "The door with silver etchings unlocks with a loud clang, you open it and enter a long corridor.\nThe walls are adorned with decaying portraits of a family.\nA voice whispers 'This is not a game...'.\nThere seems to be doors on the east side of the hall and straight north."
r7_description_2 = "This is the long hall, a lengthy, crummy carpet covers its expanse."
r7_container = "nothing"
r7_container_type = "nothing"
r7_monster = "nothing"
r7_content = "nothing"
r7_lock = True
r7_valid_directions = ["north", "south", "west"]

#eighth_room
r8_description = "You open a pair of wooden, double doors and enter into what seems to be a common room.\nA tattered carpet covers the floor and a chandelier hangs slanted from the ceiling.\nThere's a fire going in the fireplace. It looks recently lit."
r8_description_2 = "Back in the room with the fire and chandelier."
r8_container = "You notice something something is on top of the chandelier. You throw a small rock at it, and a vial falls to the ground."
r8_container_type = "open vial"
r8_monster = "nothing"
r8_content = ["The liquid inside looks murky and thick. Try at your own risk...", "drink", "The liquid slimes down your throat and you almost choke on it. Surprisingly though, you feel reinvigorated! Health increased.","armor", 25]
r8_lock = False
r8_valid_directions = ["east"]

#ninth room
r9_description = "You open the door to the north and enter cautiously into a circular room; a bookshelf covers the entire wall around you.\nAll the book are organized perfectly, only an orange one seems to be sticking out.\nThere are doors to the east and west."
r9_description_2 = "This is the room with the circular bookshelf. A myriad of what appears to be ancient biology books age slowly."
r9_container = "nothing"
r9_container_type = "push orange book"
r9_content = ["As you push the book back in its place, the bookshelf trembles and slowly sinks into the ground by means of a mechanical contraption,\nthis reveals a broken glass case embedded into the wall. Inside, you find a gleaming sword with a silver hilt.\nThe words 'Lok'tar Ogar' are etched on the blade.", "take sword", "Attack increased by 20.", "weapon", 20]
r9_monster = "nothing"
r9_lock = False
r9_valid_directions = ["north", "west", "east"]

#tenth room
r10_description = "You open the door to the east and enter what seems to be a bedroom. There's a big victorian bed covered in dust."
r10_description_2 = "This is the room where the banshee lay, her diaphanous white gown painted scarlet."
r10_container = "nothing"
r10_container_type = "nothing"
r10_monster = ["You suddenly hear soft crying and from beneath the sheets a young girl sits up. Worried, you get closer.\nShe looks up. Her eyes are completely black and she lets out a subhuman scream - she tries to slash your face with her razor like nails.\nWill you fight?", banshee]
r10_content = "nothing"
r10_lock = False
r10_valid_directions = ["east", "west"]

# room 11
r11_description = "You continue to move cautiously unto the south-east part of the room, the figure to your left.\nThere are rows of tables here, undoubtedly used for feasts, your stomach grumbles."
r11_description_2 = "This is the south-east part of the room with the long tables."
r11_container = "You spot a throne at the end of the tables and you cautiously approach it. On the seat you find a tinted glass case."
r11_container_type = "open case"
r11_monster = "nothing"
r11_content = ["You slowly open the case, to find a crown adorned with a myriad of different colored gems. You can feel power emanating from it.", "take crown", "As you rest it upon your head you feel the very fingers of your hand vibrating with strength. You just gained 20 attack.", "weapon", 20]
r11_lock = False
r11_valid_directions = ["south", "east"]

#room 12
r12_description = "You move towards the north-east part of the room with caution. You notice a red-haired boy looking out from behind an enormous chair.\nAs you try to approach him, he disappears into the ground."
r12_description_2 = "This is the north-eastern part of the Great Hall."
r12_container = "nothing"
r12_container_type = "nothing"
r12_monster = "nothing"
r12_content = "nothing"
r12_lock = False
r12_valid_directions = ["east", "north"]

#room 13
r13_description = "You cleanse your weapon from the child's blood and move on, opening the door to the east.\nHere you find another bedroom, but bare except for a rickety chair. You think you see a young red haired boy sitting on it, but he's gone with the blink of an eye.\nThere appears to be a passage only to the east."
r13_description_2 = "This is the room with the rickety chair, a single red hair lays on the floor."
r13_container = "nothing"
r13_container_type = "nothing"
r13_monster = "nothing"
r13_content = "nothing"
r13_lock = False
r13_valid_directions = ["east", "west"]

#room 14
r14_description = "You walk through a passageway on the east go come upon a kitchen. It is with some caution that you notice the stove is lit."
r14_description_2 = "You're in the kitchen with the stove."
r14_container = "You search through ever pot and pan and open every cupboard but you find nothing. You're about to give up when the stove starts rattling and spewing fire.\nYou jump back through the passage to the west and you feel the stove explode. When you come back in the room is black with soot.\nLaying in the middle of it shines a silver metal box. You scratch your head and try not to think about it too much."
r14_container_type = "open box"
r14_monster = "nothing"
r14_content = ["Within the box there's a golden key.", "take key", "This one looks special.", "key", 1]
r14_lock = False
r14_valid_directions = ["east"]

#room 15
r15_description = "You open the door and a rotting, wooden staircase spirals into darkness. You descend to find yourself in a cellar lit by a lantern.\nThere are various jars of different sizes on shelves, each with body parts preserved in bile.\nThere seems to be a dirt tunnel to the north."
r15_description_2 = "This is the cellar with the jars of bile... and body parts."
r15_container = "nothing"
r15_container_type = "nothing"
r15_monster = "nothing"
r15_content = "nothing"
r15_lock = False
r15_valid_directions = ["west", "south"]

# room 16
r16_description = "You cross the dirt tunnel slowly, an insect drops at the nape of your neck and bites you.\nYou smack it with your palm and your neck dampens with blood.\nYou see a ladder at the end of the tunnel, climb it up and you emerge into a marble floored hall.\nThere's one pair of double doors to the south."
r16_description_2 = "This is the big marbled hall. There's silverware lying on the floor, it looks expensive."
r16_container = "nothing"
r16_container_type = "nothing"
r16_monster = "nothing"
r16_content = "nothing"
r16_lock = True
r16_valid_directions = ["south", "north"]

# room 17
r17_description = "You swing open the doors with might and to see an enormous hall, big as four rooms, with a huge arched ceiling.\nTo the South you see what an enormous figure bent over something. You would have to get closer to see better.\nIt might be better to look around first."
r17_description_2 = "This is the north-west part of the great hall."
r17_container = "nothing"
r17_container_type = "nothing"
r17_monster = "nothing"
r17_content = "nothing"
r17_lock = True
r17_valid_directions = ["north", "east", "south"]

# room 18
r18_description = "You come upon the south-west part of the room, to behold the figure clearly."
r18_description_2 = "This is the north-east part of the room."
r18_container = "nothing"
r18_container_type = "nothing"
r18_monster = ["It can only be described as reptile who has taken human qualities. It's skin is scaled and frigid, it's small eyes peer with hatred as you approach.\nBehind it, you can see a big archway with sunlight shining through it... the way out.\nIt suddenly speaks: 'You've done well, apprentice, it seems Ghra-Kez has not bested you. You have proved a fine specimen indeed. Now, you'll submit under my blade or die.'\nHe unsheathes a giant broadsword and readies himself. You have come a long way, freedom awaits if you can defeat this challenge.\nWill you fight?", lizard_king]
r18_content = "nothing"
r18_lock = False
r18_valid_directions = ["west", "south"]

r19_description = "You walk through the archway wearily and find yourself in an empty room with a wardrobe on the south wall.\nYou distrustfully shove the wardrobe aside only to find the entrance of a dirt tunnel."
r19_description_2 = "This is the room with the wardrobe and the tunnel. A book lies on the floor, the illustration on the cover: red hair."
r19_container = "nothing"
r19_container_type = "nothing"
r19_monster = "nothing"
r19_content = "nothing"
r19_lock = False
r19_valid_directions = ["south", "north"]

r20_description = "You walk through the tunnel and emerge unto a lush garden, unkempt but vibrantly green.\nThe midday sun hurts your eyes but you light warms your skin.\nThere's a stone path that goes down the middle and diverges to the north and east."
r20_description_2 = "This is the overgrown garden, a broken fountain sputters clear water."
r20_container = "The dead Earthworm starts convulsing and out of its squirmy body vomits a small leather pouch.\nIt's covered in slime."
r20_container_type = "open pouch"
r20_monster = ["As you enjoy the warmth you hear a rustling in the long grass. It intensifies and out of it arises a grotesque, bulging earth worm the size of a calf.\nIt opens it circular mouth to show putrid, but sharp teeth.\nWill you put this monstrosity down?", mutant_earthworm]
r20_content = ["Inside you find a bright small amethyst, you can barely take your eyes off of it.", "take amethyst", "You store it away and with its presence you feel bolder. Your health increases by 20!", "armor", 20]
r20_lock = False
r20_valid_directions = ["north", "south", "west"]

r21_description = "You follow the path to the east and enter a tall archway. On the other side there's a court full of real-sized statues of seemingly important men.\nEach have a different expression, ranging from lust to pride.\nOddly enough, their eyes seem to follow you as you walk warily across."
r21_description_2 = "You're back in the court with all the statues!"
r21_container = "Slightly disappointed at the ease of the fight (stone is heavy after all and does not move quickly) you search the body, and find a small locket around its neck.\nYou also notice paths to the north and east."
r21_container_type = "open locket"
r21_monster = ["Suddenly, a statue clad in armor and wielding a broadsword cracks to life, standing defiantly in you path.\nWill you engage in combat with this ancient warrior?", statue]
r21_content = ["Inside there's a minute key.", "take key", "Not sure what door this will open, but it might be of help.", "key", 1]
r21_lock = False
r21_valid_directions = ["east", "west", "south"]

r22_description = "As you leave the court through the east you come enter again into the shadows of a small storeroom.\nThe air is thick and the smell, metallic. You notice a wooden bench nearby caked with dry blood. A whispers flickers and then dies, ploughing your back with goosebumps.\nIt is with great scrutiny (and luck) that you notice a bump on a tattered carpet. Beneath it, to the east, lies a small trapdoor."
r22_description_2 = "This is the dusty storeroom, rotten benches and chairs littered about. Carpet lies aside to reveal the trapdoor."
r22_container = "You search every cupboard and find a small, rotten case with a lock. You place it on the floor and step on, and the lock gives way."
r22_container_type = "open case"
r22_monster = "nothing"
r22_content = ["Inside there's a unadorned key.", "take key", "Go forth and unlock.", "key", 1]
r22_lock = False
r22_valid_directions = ["east", "west"]

r23_description = "You descend the rotting stairs for what seems like hours, each step getting darker and darker, into nothingness.\nYou finally come upon a small, rectangular room, with one single made bed. It looks clean and recently used. A single torch illuminates all."
r23_description_2 = "You're down the trapdoor and in the room with the bed again. "
r23_container = "As you snoop around you feel eyes watching you, but can see no one in the small confines of this space.\nYou find a book by the beside, it appears to emanate a blue glow."
r23_container_type = "open book"
r23_monster = "nothing"
r23_content = ["As soon as you open it the pages flash a violent blue and burn your hands in excruciating pain.\nYou immediately drop it to the floor, recognizing this as an item of immense power. You may not be able to read, but wielding it might infuse you with strength.", "take book", "As you take it you hear the cackle of the dead necromancer... Nonetheless you feel stronger, you have gained 10 attack!\nThere are no exits other than the way you come in through (east).", "weapon", 10]
r23_lock = False
r23_valid_directions = ["east"]

r24_description = "You exit the room through a small door and climb up a long, rusty ladder.\nYou climb for what seems like forever, when you finally reach the top you're atop a sentry tower in a big circular room, overseeing a shimmering, red dusk.\nStrangely enough, you can see nothing below the tower. A strange darkness overtakes your eyes."
r24_description_2 = "You're atop the sentry tower once again, the scarlet dusk is gone but the darkness remains - you can see nothing below you and only a moon lit horizon. "
r24_container = "The hawk's belly glows with a strange light, so you slice it open, throw the guts aside and find inside a silver case."
r24_container_type = "open case"
r24_monster = ["As you look out the distance you hear a strange cry and turn around to see a massive hawk flying towards you, it's talons aimed at your throat.\nYou throw yourself aside and the hawk lands in the room, it's eyes glow red. Fight or flee?", hawk]
r24_content = ["Inside there's a silver key.", "take key", "Be wise with what you open.", "key", 1]
r24_lock = False
r24_valid_directions = ["south"]

r25_description = "You enter an underground tunnel which turns sharply south, only to emerge unto stone battlements.\nTo either side you can see nature reclaiming civilization. A big archway southwards upon a rock wall."
r25_description_2 = "This is the stone battlements, remains of flags lay scattered upon the ground, some being take up by the wind."
r25_container = "nothing"
r25_container_type = "what you have to type to get it to open"
r25_monster = "nothing"
r25_content = "nothing"
r25_lock = False
r25_valid_directions = ["west", "north"]

r26_description = "You swing open a big iron gate to come upon another small garden, slightly flooded from the other room\nYou wonder where the water even came from. There are hibiscus flowers growing wildly, making the place look deceitfully amiable."
r26_description_2 = "This is the partly flooded room. The hibiscus flowers seem to have all disappeared."
r26_container = "You aimlessly glance over the grass, not expecting to find anything, when a glint catches your eye: a small coffer."
r26_container_type = "open coffer"
r26_monster = "nothing"
r26_content = ["Inside you simply find a small note that reads: It now daWns on me that Sufficiency iS not of my SurE qualities Surrounding the neWts. ", "take note", "You do not feel anything extraordinary - perhaps the magic is within the words.", "armor", 0]
r26_lock = False
r26_valid_directions = ["west", "east"]

r27_description = "You unlock the vine covered door with the minute key, squeezing yourself through and entering muddy, flooded room.\nFlotsam and jetsam bob up and down at waist level, mingling with the dirt and leaves. Sunlight breaks in through broken tiles.\nThere appears to be exits to the east and west."
r27_description_2 = "You're back in the flooded room. The hydra's blood tinting the the water red; one of the heads is floating by."
r27_container = "nothing"
r27_container_type = "nothing"
r27_monster = ["As you start wading across, the water across the room becomes turbulent. A great shadow passes near you under the water.\nOut of it arises a three-headed hydra, its silver scales glimmering. Will you fight?", hydra]
r27_content = "nothing"
r27_lock = True
r27_valid_directions = ["north", "east", "west"]

r28_description = "You enter an open hallway made of stone, lined with torches stone bowls full of water. For some reason, the moment you step in all sound is extinguishes.\nAs you walk all you can hear is your own breath and heartbeat. The path leads straight east."
r28_description_2 = "This is the soundless hall. This time you can hear your the impact of your bone on your muscles."
r28_container = "nothing"
r28_container_type = "nothing"
r28_monster = "nothing"
r28_content = "nothing"
r28_lock = False
r28_valid_directions = ["east", "west"]

r29_description = "The stone hallway descends into a stone archway, this leads to a circular pit.\nAll around and above there are stands, as if for a public to watch. This does not feel right. There are exits to the east and west."
r29_description_2 = "The gladiator pit, the severed head of the fighter lies on the dusty floor."
r29_container = "nothing"
r29_container_type = "nothing"
r29_monster = ["As you grip your weapon tighter an iron gate open to the north and out of it emerges an enormous man, veins bulging from the arms that wield two sharp axes.\nHe stands ready to kill. Will you fight?", gladiator]
r29_content = "nothing"
r29_lock = False
r29_valid_directions = ["west", "east"]

r30_description = "As you leave the pit you enter what could only be the fighters' preparation room.\nThere are bloody pieces of bandages on the floor, as well as a tooth, broken weapons, flasks of wine, crushed helmets & shields and small wooden benches. The stench of sweat still lingers.\nThere's an exit only to the south."
r30_description_2 = "This is the gladiator preparation room. Tokens of blood lay scattered across the room."
r30_container = "You look around for anything that you might be able to use, but it all blades seem broken or dull, the shields bashed and the helmets cracked.\nYou wonder over to a wardrobe and when you open it the body of a young boy crumples. He's clutching a rectangular case."
r30_container_type = "open case"
r30_monster = "nothing"
r30_content = ["You wrench the case from the corpse, open it and within find an exquisite looking sword, its hilt delineated by gems. The blade is so sharp it cuts you at the touch.", "take sword", "You've gained 15 attack!", "weapon", 15]
r30_lock = False
r30_valid_directions = ["east", "north"]

# Ghost rooms are basically the boundaries of the map. They're what holds the dungeon, Ghra-kez, where it is.

# Lower side ghost rooms
ghost_room1 = Ghostroom(0, -1)
ghost_room2 = Ghostroom(1, -1)
ghost_room3 = Ghostroom(2, -1)
ghost_room4 = Ghostroom(3, -1)
ghost_room5 = Ghostroom(4, -1)
ghost_room6 = Ghostroom(5, -1)

#Left side ghost room
ghost_rooml2 = Ghostroom(-1, 1)
ghost_rooml3 = Ghostroom(-1, 2)
ghost_rooml4 = Ghostroom(-1, 3)
ghost_rooml5 = Ghostroom(-1, 4)

#Right side ghost room
ghost_roomr1 = Ghostroom(6, 0)
ghost_roomr2 = Ghostroom(6, 1)
ghost_roomr3 = Ghostroom(6, 2)
ghost_roomr4 = Ghostroom(6, 3)
ghost_roomr5 = Ghostroom(6, 4)

#top side ghost rooms
ghost_roomtop1 = Ghostroom(0, 5)
ghost_roomtop2 = Ghostroom(1, 5)
ghost_roomtop3 = Ghostroom(2, 5)
ghost_roomtop4 = Ghostroom(3, 5)
ghost_roomtop5 = Ghostroom(4, 5)
ghost_roomtop6 = Ghostroom(5, 5)

# Here's the magic happens, where the rooms and the player are actually created.
first_room = Room(2, 0, r1_description, r1_description_2, r1_container, r1_container_type, r1_content, r1_monster, r1_lock, r1_valid_directions)
second_room = Room(3, 0, r2_description, r2_description_2, r2_container, r2_container_type, r2_content, r2_monster, r2_lock, r2_valid_directions)
third_room = Room(4, 0, r3_description, r3_description_2, r3_container, r3_container_type, r3_content, r3_monster, r3_lock, r3_valid_directions)
fourth_room = Room(5, 0, r4_description, r4_description_2, r4_container, r4_container_type, r4_content, r4_monster, r4_lock, r4_valid_directions)
fifth_room = Room(4, 1, r5_description, r5_description_2, r5_container, r5_container_type, r5_content, r5_monster, r5_lock, r5_valid_directions)
sixth_room = Room(5, 1, r6_description, r6_description_2, r6_container, r6_container_type, r6_content, r6_monster, r6_lock, r6_valid_directions)
seventh_room = Room(2, 1, r7_description, r7_description_2, r7_container, r7_container_type, r7_content, r7_monster, r7_lock, r7_valid_directions)
eighth_room = Room(3, 1, r8_description, r8_description_2, r8_container, r8_container_type, r8_content, r8_monster, r8_lock, r8_valid_directions)
ninth_room = Room(2, 2, r9_description, r9_description_2, r9_container, r9_container_type, r9_content, r9_monster, r9_lock, r9_valid_directions)
tenth_room = Room(3, 2, r10_description, r10_description_2, r10_container, r10_container_type, r10_content, r10_monster, r10_lock, r10_valid_directions)
room_11 = Room(1, 0, r11_description, r11_description_2, r11_container, r11_container_type, r11_content, r11_monster, r11_lock, r11_valid_directions)
room_12 = Room(1, 1, r12_description, r12_description_2, r12_container, r12_container_type, r12_content, r12_monster, r12_lock, r12_valid_directions)
room_13 = Room(4, 2, r13_description, r13_description_2, r13_container, r13_container_type, r13_content, r13_monster, r13_lock, r13_valid_directions)
room_14 = Room(5, 2, r14_description, r14_description_2, r14_container, r14_container_type, r14_content, r14_monster, r14_lock, r14_valid_directions)
room_15 = Room(1, 2, r15_description, r15_description_2, r15_container, r15_container_type, r15_content, r15_monster, r15_lock, r15_valid_directions)
room_16 = Room(0, 2, r16_description, r16_description_2, r16_container, r16_container_type, r16_content, r16_monster, r16_lock, r16_valid_directions)
room_17 = Room(0, 1, r17_description, r17_description_2, r17_container, r17_container_type, r17_content, r17_monster, r17_lock, r17_valid_directions)
room_18 = Room(0, 0, r18_description, r18_description_2, r18_container, r18_container_type, r18_content, r18_monster, r18_lock, r18_valid_directions)
room_19 = Room(0, 3, r19_description, r19_description_2, r19_container, r19_container_type, r19_content, r19_monster, r19_lock, r19_valid_directions)
room_20 = Room(1, 3, r20_description, r20_description_2, r20_container, r20_container_type, r20_content, r20_monster, r20_lock, r20_valid_directions)
room_21 = Room(2, 3, r21_description, r21_description_2, r21_container, r21_container_type, r21_content, r21_monster, r21_lock, r21_valid_directions)
room_22 = Room(3, 3, r22_description, r22_description_2, r22_container, r22_container_type, r22_content, r22_monster, r22_lock, r22_valid_directions)
room_23 = Room(4, 3, r23_description, r23_description_2, r23_container, r23_container_type, r23_content, r23_monster, r23_lock, r23_valid_directions)
room_24 = Room(5, 3, r24_description, r24_description_2, r24_container, r24_container_type, r24_content, r24_monster, r24_lock, r24_valid_directions)
room_25 = Room(0, 4, r25_description, r25_description_2, r25_container, r25_container_type, r25_content, r25_monster, r25_lock, r25_valid_directions)
room_26 = Room(1, 4, r26_description, r26_description_2, r26_container, r26_container_type, r26_content, r26_monster, r26_lock, r26_valid_directions)
room_27 = Room(2, 4, r27_description, r27_description_2, r27_container, r27_container_type, r27_content, r27_monster, r27_lock, r27_valid_directions)
room_28 = Room(3, 4, r28_description, r28_description_2, r28_container, r28_container_type, r28_content, r28_monster, r28_lock, r28_valid_directions)
room_29 = Room(4, 4, r29_description, r29_description_2, r29_container, r29_container_type, r29_content, r29_monster, r29_lock, r29_valid_directions)
room_30 = Room(5, 4, r30_description, r30_description_2, r30_container, r30_container_type, r30_content, r30_monster, r30_lock, r30_valid_directions)


List = [first_room, second_room, third_room, fourth_room, fifth_room, sixth_room, seventh_room, eighth_room, ninth_room, tenth_room, room_11, room_12, room_13, room_14, room_15, room_16, room_17, room_18, room_19, room_20, room_21, room_22, room_23, room_24, room_25, room_26, room_27, room_28, room_29, room_30, ghost_room1, ghost_room2, ghost_room3, ghost_room4, ghost_room5, ghost_room6, ghost_rooml2, ghost_rooml3, ghost_rooml4, ghost_roomr1, ghost_roomr2, ghost_roomr3, ghost_roomr4, ghost_roomtop1, ghost_roomtop2, ghost_roomtop3, ghost_roomtop4, ghost_roomtop5, ghost_roomtop6, ghost_roomr5, ghost_rooml5]


def move():
    # The variable won will change once you finish the game.
    print("One day you're strolling aimlessly around the woods because, well, you feel like it.")
    print("The air is fresh and sunlight pierces the green foliage, giving everything a serene, green glow.")
    print("You're life's been quite easy, and you know little of hardship, yet, you fancy yourself a strong and knowledgeable human being.")
    print("Suddenly, from behind a bush appears a little red-haired boy who opens his mouth and says with an adult voice: ")
    print("'You have grown lax your entire life, and have not taken time to appreciate adversity - for that you'll face Ghra-Kez.'")
    print("He then wriggles his fingers at you and you stifle a laugh, only for it to become a scream of agony as you lose consciousness... ")
    #time.sleep(5)
    won = False
    print()
    while not won:
        z = 0
        container = None
        content = None
        gtg = False
        # Looping through all the rooms to match the player's position with a room, and thus figure out where the player is.

        if user.x == -1 and user.y == 0:
                    print("You lay on top of the Lizard King's corpse, enervated and shuddering.")
                    print("You wipe the blood of your face and look into freedom, the green forest awaits you and you rejoice.")
                    print("Despite this, hatred poisons your heart, and as you enter the light you know you'll be back.")
                    print("A child's laugh is the last thing you hear as the passage you just went through disappears....")
                    if user.attack > 70:
                        print()
                        print("You finished with a gold medal! Fuck yeah, well done!")
                        print()
                    elif user.attack > 50:
                        print()
                        print("You've finished with a silver medal! Good job on that.")
                        print()
                    else:
                        print()
                        print("You got a bronze medal... Hm.")
                        print()
                    exit()

        for i in List:

            if user.x == i.x and user.y == i.y:

                if user.startup > 0:
                    if north == 1:
                        if "north" in i.valid_directions:  # If the room can be accessed from that certain location then the function "action" executes, and the playere advances rooms.
                            action(i, north, south, east, west)
                        
                        elif i.valid_directions == "none":  # If they're attempting to go  into a ghost room (off the grid) then this will tell them.
                            print("Just a wall there.")
                            user.y -= 1
                        else:
                            print("Can't access room through there.")  # They may try to access a room that cannot be accessed from their certain location so then this happpens.
                            user.y -= 1
                            north = 0

                    elif south == 1:
                        if "south" in i.valid_directions:
                            action(i, north, south, east, west)

                        elif i.valid_directions == "none":
                            print("Just a wall there.")
                            user.y += 1

                        else:
                            print("Can't access room through there.")
                            user.y += 1
                            south = 0

                    elif east == 1:
                        if "east" in i.valid_directions:
                            action(i, north, south, east, west)
                        
                        elif i.valid_directions == "none":
                            print("Just a wall there.")
                            user.x -= 1
                        else:
                            print("Can't access room through there.")
                            user.x -= 1
                            east = 0

                    elif west == 1:
                        if "west" in i.valid_directions:
                            action(i, north, south, east, west)
                        
                        elif i.valid_directions == "none":
                            print("Just a wall there.")
                            user.x += 1

                        else:
                            print("Can't access room through there.")
                            user.x += 1
                            west = 0
                    else:
                        pass

                else:
                    print(i.description)
                    i.counter += 1

        north = 0
        south = 0
        east = 0
        west = 0

        z = 0

        user.startup += 1
        time.sleep(.2)
        d = input("- ")

        # These are all the direction options. The player's position gets updated with every turn.
        if d == "east" or d == "e":
            user.x += 1
            east += 1  # Every time the player moves I need to keep track of what direction he went so I can retract his progress if he stumbled on a locked door room.
                      # The issue here is that the player first moves to an x, y, location, and THEN I look at the info for that room.
                      # This enables the player to technically move his x,y coordinate to rooms he might not have access to, which is why I have to reverse it.

        elif d == "north" or d == "n":
            user.y += 1
            north += 1

        elif d == "west" or d == "w":
            user.x -= 1
            west += 1

        elif d == "south" or d == "s":
            user.y -= 1
            south += 1

        elif d == "survey":
            for i in List:
                if user.x == i.x and user.y == i.y:
                    z = i.container
                    if i.container != "nothing":
                        print(i.container)

                        d = input("- ")
                        if d == str(i.container_type):
                            print(i.content[0])
                            d = input("- ")
                            if d == i.content[1]:
                                print()
                                if i.content[3] == "key":
                                    user.key += i.content[4]
                                    print(i.content[2])
                                    i.container = "nothing"
                                elif i.content[3] == "weapon":
                                    user.attack += i.content[4]
                                    print(i.content[2])
                                    i.container = "nothing"
                                elif i.content[3] == "armor":
                                    user.health += i.content[4]
                                    print(i.content[2])
                                    i.container = "nothing"
                            
                                print()
                            else:
                                print()
                                print("Try something different.")
                                print()
                        else:
                            print()
                            print("Try again. I may have misunderstood.")
                            print()
                    else:
                        print()
                        print("There's nothing to be found.")
                        print()

        elif d == str(user.container):  # Variable set during action function
            print(user.content[0])
            d = input("- ")
            if d == user.content[1]:
                print()
                if user.content[3] == "key":
                    user.key += user.content[4]
                    print(user.content[2])
                    z = "nothing"
                elif user.content[3] == "weapon":
                    user.attack += user.content[4]
                    print(user.content[2])
                    z = "nothing"
                elif user.content[3] == "armor":
                    user.health += user.content[4]
                    print(user.content[2])
                    z = "nothing"
                print()
            else:
                print("Try different syntax.")
        elif d == "stats":
            print()
            print("Health:", user.health)
            print("Attack:", user.attack)
            print("Keys:", user.key)
            print()

        elif d == "help":
            print()
            print("-Navigate with cardinal directions (north, south, east, west; can be abbreviated to their first letter)")
            print("-Obtain keys in order to unlock certain rooms.")
            print("-In order to obtain items follow this procedure: survey, open x, take x.")
            print("-You can skip directly to 'open x' if you know the container that lies in the room.")
            print()
            print("-Input 'stats' if to see your health, attack and amount of keys!")
            print("-Try your hand at your own commands for special rewards! ;)")
            print()
        else:
            print()
            print("That is not understandable.")
            print()
move()

