#RPG Nested Dictionaries - Jenil Patel
#Dec. 4, 2023
#This code will create 3 different dictionaries and print statements with
#each item in the dictionary


characters = {'Peter':{'Full Name':'Peter Benjamin Parker',
                       'Health Points':'20'},
              'Miles':{'Full Name':'Miles Gonzalo Morales',
                       'Health Points':'10'},
              'Gwen':{'Full Name':'Gwendolyne Maxine Stacy',
                      'Health Points':'10'},
              'Miguel':{'Full Name':'Miguel O’Hara',
                        'Health Points':'15'}
              }
#The dictionary above is for each character and has individual dictionaries
#for each character

places = {'Front Yard':{'Description':
                        'In front of the haunted house, there is a broken tree to the right and a close to broken tree on the left.'},
          'School':{'Description':
                    'You and your friends go to high school here.'},
          'Back Yard':{'Description':
                       'In the back of the haunted house, there is a lot of tall grass.'},
          'Haunted House':{'Description':
                           'It is said that there are countless spirits in the house and no one has come back from the haunted house.'},
          'Living Room':{'Description':
                         'There is cloth over all the furniture and there are family photos on the wall.'},
          'Bedroom':{'Description':
                     'This was the old room of the youngest daughter of the family and she had many toys.'},
          'Basement':{'Description':
                      'The door is locked to the basement but there seems to be something suspicious coming from the basement.'}
          }
#The dictionary above is for each location and has an individual dictionary
#for each locatio

items = {'Phone':{'Damage':'1',
                  'Description':'Can be used to call for help and as a flashlight'},
         'Flash Light':{'Damage':'2',
                        'Description':'One of your lights sorces'},
         'Baseball Bat':{'Damage':'5',
                        'Description':'Main sorce of protection'},
         'Key':{'Damage':'2',
                'Description':'Used to open a locked door'}
         }
#The dictionary above is for each item and has an individual dictionary
#for each item

#the next line loops through each character and its info
for character, character_info in characters.items(): 
    print(f"\n{character}:")
    full_name = character_info['Full Name'] #stores thire full name 
    print(f"{character}'s full name is {full_name}.")
    hp = character_info['Health Points']    #store thire health points
    print(f"{character} has {hp} health points.")

#the next line loops through each place and its info
for place, place_info in places.items():
    print(f'\n{place}:')
    print(place_info['Description'])    #print the discription of place

#the next line loops through each item and its info
for item , item_info in items.items():
    print(f'\n{item}:')
    print(item_info['Description'])	#prints item description
    damage = item_info['Damage']	#store damage of item
    print(f'{item} does {damage} amount of damage.')