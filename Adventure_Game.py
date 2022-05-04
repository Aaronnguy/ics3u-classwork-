# Gallo
import os 

 
# Aidan
current_location = "basement"
# Gallo
front_door_locked = True 
# Aaron
timer = 0 
locked = False
lock_code = 2009
open = True
inspect = ["mirror", "sink", "drawer", "shower"]
#Aidan
inventory = []
#Aidan
dead_people=["Matther","Ader","Dhani","HaHa","Ngu","Aaron","Wayne","Xiao"]
#Matthew
sPoOkY_nOtE = ["T̷̤͊͛͜Ḣ̸̼͝E̴̥̼͂ ̴̭̣̽̃E̸͕͇͋̈́Ǹ̷̺͝D̴͚̽ ̷̬̭͐Ì̸̟S̴̘̺̚ ̸͖̀N̶̡̋E̶͈̼͋͑A̶̲͋͐R̵̬̮̃. R̵͚͔̄U̸̠͙͘N̴̺͎̒̂ ̶͖̌̎I̴͉͑N̸͕̹̎̋ ̸͖̜͗͝F̷̭͑̚E̷͇͖̐̚Ȃ̶͎̕R̵͇̍"]
# Gallo
while True:
        os.system("clear")
# Aidan        
        print(
          "You wake up from a deep sleep and realize you are in an unusual place.") 
        print(
          "You also realize this a place you don't want to be and you want to get out.")
  
        print()
        if current_location == "basement":
            print(
              "Looking around you see no clear way out.")
            
            print(
              "You then see one door. But it's locked! You have to find a key")
            search2 = input ("Are you wanting to search the room? Type yes or no: ")
            if search2.lower() == "yes":
                search2 = input("Where do you want to search? closet, stool, or couch: ")
            if search2.lower() == "no":
                print ("That is not an option!")
                search2 = input("Where do you want to search? closet, stool, or couch: ")
            if search2 == "closet":
                print ("Damn Unlucky. It looks like the key is not in the closet.")
            elif search2 == "couch":
                print ("Well it looks like I have to move on and look for somewhere else.")
            
            elif search2 == "stool":
                print (
                    "You've found the key. Now get out of the basement")
                print (
                    "Before leaving you take a quick second look around the room and find this")
            
                print (dead_people)
            
                print (
                    "It appears that is a list of victims of some sort")
                inventory.append ("basement key")                   
                print("Options:")
                print("- go to the [k]itchen")
                print("- go to the [w]ashroom")
                print("- go to the [m]aster bedroom")
                print("- go to the [a]ttic") 
                                        
                choice = input("choice: ").lower()
                if choice == "k":
                    current_location = "kitchen"
                elif choice == "a":
                    current_location = "attic"
                elif choice == "m":
                    current_location = "Master_Bedroom"
                elif choice == "w":
                    current_location = "washroom"
                    inventory.remove ("basement key")
  
                while search2 == "couch":
                    search2 = input("Where do you want to search? closet, stool, or couch: ")
          
              
                while search2 == "closet":
                    search2 = input("Where do you want to search? closet, stool, or couch: ")
  
         
# Matthew      
        if current_location == "kitchen":
            print(
              "your current location is the kitchen")
            print(
              "this place has an eerie atmosphere.")
            print(
              "there is something burning in the oven.")
            print(
              "you start to get a little scared")
            print(
              "Options:")
            print(
              " -Go to the [b]asement")
            print(
              " - Go to the [w]ashroom")
            print(
              " - Go to the [m]aster bedroom")
            print(
              " - Go to the [a]ttic")
            search = input("Do you want to search the [oven] or the [drawers] of the kitchen?").lower()
            if search.lower() == "oven":
              print(
                "you walk up to the oven...you open it...you see a burning head")
              print(
                "in fear you quickly shut oven")
              print(
                "Options: ")
              print(
                " - Go to the [w]ashroom")
              print(
                " - Go to the [m]aster bedroom")
              print(
                " - Go to the [a]ttic")
              print(
                "- Type 'drawers' to search the drawers in the kitchen")
              search = input("Do you want to search the [oven] or the [drawers] of the kitchen?").lower()
            if search.lower() == "drawers":
              print(
                "you search the drawers...there is no key in any of them...")
              print(
                "you do see a haunted note tho.")
              print(
                "it says...")
              print(sPoOkY_nOtE)
              print(
                "Options: ")
              print(
                " - Go to the [w]ashroom")
              print(
                " - Go to the [m]aster bedroom")
              print(
                " - Go to the [a]ttic")
              search = input("Do you want to search the [oven] or the [drawers] of the kitchen?").lower()
              inventory.append ("sPoOkY_nOtE")
              print(inventory)

        
  # Aaron
       elif current_location == "washroom":
            print(
                "You did not find the key to escape downstairs") 
            print(
                "so you walk upstairs to check the washroom.")
            print(
                "Inside the guest washroom") 
            print(
                "you see a sink, a USEABLE shower, a washroom mirror")
            print(
                "you felt dirty")
            print(
                "what do you do?")
            while True:
                choice = input(f'go to {inspect}: ')
                inspect.remove(choice)
            
                if choice == "mirror":
                    print(
                        "you looked at the mirror")
                    print(
                        "it was oddly cleaner than everything else in the room")
            
                elif choice == "sink":
                    print(
                        "this sink is rusted")
                    print(
                        "seems unusable")
                # used ian's idea for the lock 
                elif choice == "drawer":
                    print("theres a lock")
                    locked = input("unlock it? [no] [yes] ")        
                if locked == "no":
                    inspect.append("drawer")
                if locked == "yes":
                    while open is True:
                        number = int(input("Enter Lock Code: "))
                        if number == lock_code: 
                            print(
                                "the lock was unlocked")
                            print(
                                "you have recieved the key to the front door")
                            inventory.append("front door key")
                            print(
                                "go to the front door?")
                           
                            decision = input(
                                "are you ready to leave [yes] [no]: ")
                            if decision == "yes":
                                current_location = "front-door"
                            elif decision == "no":
                                current_location = "basement"
                                print(
                                    "you should've left")
                            open = False 
                        else: 
                            print("wrong code")
                            inspect.append("drawer")
                                      
                elif choice == "shower":
                    print(
                        "the shower head is rusty")
                    shower = input("take a shower? [yes] [no]")
                    if shower == "no":
                        inspect.append("shower")
                    elif shower == "yes":
                        timer = int(input("[15] or [30] minutes: "))
                    
                    if timer == 15:
                        print(
                            "that was the weirdest shower you taken")
                        print(
                            "you notice something wrong with the mirror")
                        print(
                            "with the mist from the hot water")
                        print(
                            "the mirror printed 2009")
                      
                    elif timer == 30: 
                        print(
                            "now why would you take that long")
                        print(
                            "you notice something wrong with the mirror")
                        print(
                            "with the mist from the hot water")
                        print(
                            "the mirror printed 2009") 
                          
            
# Ian        
        elif current_location == "Master_Bedroom":
        
            print("You did not find the key to escape downstairs and you walk upstairs to check the master bedroom.")
            print("You look around and see a bed, bedside table, closet, tv and rug.")
            search1 = input("What do you search? The [Bed], bedside [Table], [TV], [Closet] or [Rug] :").lower()
            
            if search1 == "bed":
                    print("You uncover the blanket and you find a pool of dried blood and an axe.")
                    option = input("Do you pick up the axe? Type yes or no.")
                    if option == "yes":
                        inventory.append("axe")
                        print(inventory)
                    else:
                        print("What do you search next:")
                        
                

            elif search1 == "table":
                    print("You try to open the bedside table, but it is locked. You see a number lock on the side with four digits")
                    code = int(input("What is the four digit code?"))
                    if code == 4920:
                        print("The lock is unlocked and you find a key that leads to the attic")
                        inventory.append ("attic key") 
                    else:
                        print("Try again")
                        
            elif search1 == "rug":
                    print("You look under the rug and dont find anything")
                
            elif search1 == "tv":
                    print("You turn on the TV and see the numbers 4920")
                
            elif  search1 == "closet":
                    print("You need to break open the wooden closet.")
                    opencloset = input("Do you [punch] the closet open or use the [axe]")
                    if opencloset == "punch":
                        print("you can't open it and you hurt your fist")
                    elif opencloset == "axe": 
                        inventory.remove("axe")
                        print("You break the closet open and a wave of dust hits your face. You see a dusty wedding dress and an old letter.")
                    read = input("Do you read the letter? Type yes or no.")
                    if read == "yes":
                        print("You open the letter and it reads... Hi to whoever may be reading this. Today is my wedding day and I will be happily married to my husband. Although I am very excited for this day, I have a feeling something bad will happen. There is this spine chilling feeling that I am being watched from afar by an ominous pair of eyes...")
                    else:
                        print("Go search something else.")                     
           
