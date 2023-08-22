import tkinter as tk
import random

def art1(typ):
        
    if typ == 1:

        option01 = input("Would you like the character to be described or \
based on a randomised animal or object? 1 or 2: ")
        
        if option01 == "1":

            form = 'Species: {}\nBuild: {}\nGender: {}\nGenre: {}\nOccupation: {}'

            occuplist01 = ['Mechanic', 'Soldier', 'Mercenary', 'Maintenance', \
                       'Labourer', 'Engineer', 'Civilian', 'Hacker', 'Pilot', \
                        ]
            occuplist02 = ['Blacksmith', 'Soldier', 'Mercenary', 'Civilian', \
                       'Hunter', 'Labourer']
            occuplist03 = ['Blacksmith', 'Soldier', 'Civilian', 'Mercenary', \
                       'Hunter', 'Labourer', 'Healer', 'Magic-User']
            occuplist04 = ['Civilian', 'Labourer', 'Doctor', 'Engineer', \
                       'Hacker', 'Soldier', 'Pilot', ]
            scifiocc = random.choice(occuplist01)
            medievalocc = random.choice(occuplist02)
            fantasyocc = random.choice(occuplist03)
            modernocc = random.choice(occuplist04)

            themelist01 = ['Cyberpunk', 'Solarpunk', 'Dystopian', 'Utopian']
            themelist02 = ['Golden Ages', 'Dark Ages', 'Roman', 'Viking']
            themelist03 = ['Dark Fantasy', 'Fairytale', 'Classic Fantasy']
            themelist04 = ['Modern', 'Retro-Modern', 'Early Space Age']
            scifi = random.choice(themelist01)
            medieval = random.choice(themelist02)
            fantasy = random.choice(themelist03)
            modern = random.choice(themelist04)
        
            speclist = ['Humanoid', 'Non-Humanoid']
            buildlist = ['Thin', 'Well-built', 'Chunky', 'Lightweight', \
                     'REFRIGERATOR']
            genderlist = ['Male', 'Female', 'Unspecified', 'Androgynous', \
                      'You Decide!']
            genrelist = [scifi, medieval, fantasy, modern]
        
            spec = random.choice(speclist)
            build = random.choice(buildlist)
            gender = random.choice(genderlist)
            genre = random.choice(genrelist)
        
            if genre == scifi:
                occupation = scifiocc
                print (form .format(spec, build, gender, genre, occupation))
        
            if genre == medieval:
                occupation = medievalocc
                print (form .format(spec, build, gender, genre, occupation))
        
            if genre == fantasy:
                occupation = fantasyocc
                print (form .format(spec, build, gender, genre, occupation))

            if genre == modern:
                occupation = modernocc
                print (form .format(spec, build, gender, genre, occupation))
    
        if option01 == "2":
        
            option02 = input("Animal or Object?: ")

            if option02 == 'animal' or option02 == 'Animal':

                birdlist = ['Bird of Paradise', 'Hawk', 'Falcon', 'Eagle', \
                            'Songbird', 'Peacock', 'Penguin', 'Owl', \
                            'Cassowary', 'Emu', 'Ostrich', 'Kiwi', 'Parrot', \
                            'Crow', 'Jay', 'Swift', 'Pelican', 'Stork', \
                            'Heron', 'Waterfowl', 'Seagull', 'Albatross', \
                            'Petrel']
                reptilelist = ['Monitor Lizard', 'Gecko', 'Skink', 'Snake', \
                           'Turtle', 'Komodo Dragon', 'Iguana', 'Anole', \
                           'Draco Lizard', 'Crocodile', 'Caiman', 'Gharial']
                amphlist = ['Frog', 'Bullfrog', 'Toad', 'Salamander', \
                            'Tree Frog', 'Caecillian', 'Axolotl']
                mammallist = ['Cat', 'Dog', 'Big Cat', 'Wolf', 'Fox', 'Bear', \
                              'Seal', 'Sea Lion', 'Dolphin', 'Orca', 'Whale', \
                              'Deer', 'Moose', 'Musk Deer', 'Ox', 'Antelope', \
                              'Bear', ]
            
                bird = random.choice(birdlist)
                reptile = random.choice(reptilelist)
                amphib = random.choice(amphlist)
                mammal = random.choice(mammallist)

                animallist = [bird, reptile, amphib, mammal]

                animal = random.choice(animallist)

                print (animal)

            if option02 == 'Object' or option02 == 'object':

                devicelist = ['Phone', 'Computer', 'TV', 'Gaming Console', \
                              'Toaster', 'Microwave', 'Oven', 'Air Fryer', \
                              'Watch', 'Clock', 'Blender', 'Striplights', \
                              'LEDs', 'Lamp', 'Lava Lamp', 'Camera', ]
                naturlist = ['Conch Shell', 'Clam Shell', 'Crystals', \
                              'Ore', 'Water', 'Coral', ]
                florlist = ['Grass', 'Wheat', 'Cotton', 'Ferns', 'Vines', \
                            'Tree', 'Flowers', 'Algae', 'Kelp', 'Flytrap', \
                            'Pitcher Plant', 'Sundew', ]
                
                device = random.choice(devicelist)
                natural = random.choice(naturlist)
                flora = random.choice(florlist)

                objectlist = [device, natural, flora]

                obj = random.choice(objectlist)

                print(obj)

            
    if typ == 2:

        option01 = input("Do you want a hybrid, fantasy creature, alien,\
 or a descendant of an existing animal? 1, 2, 3 or 4: ")
        
        if option01 == "1":

            specamnt = ['2', '3', '4']

            specnum = random.choice(specamnt)

            animlist = ['Bird of Paradise', 'Hawk', 'Falcon', 'Eagle', \
                            'Songbird', 'Peacock', 'Penguin', 'Owl', \
                            'Cassowary', 'Emu', 'Ostrich', 'Kiwi', 'Parrot', \
                            'Crow', 'Jay', 'Swift', 'Pelican', 'Stork', \
                            'Heron', 'Waterfowl', 'Seagull', 'Albatross', \
                            'Petrel'
                            'Monitor Lizard', 'Gecko', 'Skink', 'Snake', \
                            'Turtle', 'Komodo Dragon', 'Iguana', 'Anole', \
                            'Draco Lizard', 'Crocodile', 'Caiman', 'Gharial'
                            'Frog', 'Bullfrog', 'Toad', 'Salamander', \
                            'Tree Frog', 'Caecillian', 'Axolotl'
                            'Cat', 'Dog', 'Big Cat', 'Wolf', 'Fox', 'Bear', \
                            'Seal', 'Sea Lion', 'Dolphin', 'Orca', 'Whale', \
                            'Deer', 'Moose', 'Musk Deer', 'Ox', 'Antelope', \
                            'Bear', ]

            if specnum == '2':
                species01 = random.choice(animlist)
                species02 = random.choice(animlist)
                print('A Hybrid of {} and {}.' .format(species01, species02))
            
            if specnum == '3':
                species01 = random.choice(animlist)
                species02 = random.choice(animlist)
                species03 = random.choice(animlist)
                print('A Hybrid of {}, {} and {}' .format(species01, species02\
                                                          , species03))
            
            if specnum == '4':
                species01 = random.choice(animlist)
                species02 = random.choice(animlist)
                species03 = random.choice(animlist)
                species04 = random.choice(animlist)
                print('A Hybrid of {}, {}, {} and {}.' .format(species01, \
                                                               species02, \
                                                               species03, \
                                                               species04))

        if option01 == "2":

            hab = ['Urban', 'Polar', 'Coastal', 'Savannah', 'Mountain', \
                   'Marine', 'Desert', 'Jungle', 'Forest', 'Rainforest', ]

            monst = ['Amphithere', 'Basilisk', 'Dragon', 'Wyvern', 'Wyrm', \
                     'Lindwurm', 'Drake', 'Hydra', 'Sea Serpent', 'Griffin', \
                     'Dire Wolf', 'Mimic', 'Owlbear', 'Phoenix', 'Hippogriff',\
                     'Unicorn', 'Pegasus',]
            
            habitat = random.choice(hab)
            monster = random.choice(monst)

            print('{} {}.' .format(habitat, monster))

        if option01 == "3":

            realm = ['Aerial', 'Terrstrial', 'Aquatic']
            life = ['Ambush Predator', 'Pack Predator', 'Endurance Predator', \
                    'Pursuit Predator', 'Opportunistic Omnivore']

env = 0
char = 1
crea = 2
vehicle = 3
archi = 4

choice = input("What option would you like to pick? Whole numbers, 0 - 6: ")

if choice == '1':
    art1(char)

if choice == '2':
    art1(crea)
