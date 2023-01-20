'''
-------------------------------------------------------------------------------
Name:  TheQuestforthe3%JuniorYear.py
Purpose: A text based adventure game

Author:   Erins Bozhori

Created:  20/10/2022
------------------------------------------------------------------------------
'''

new_game = 0
place = 1
inventory = ["Metal Water Bottle - A Metal Water Bottle given to you by Davis (DMG:10)", ]
# Player Inventory

shop_inventory = ["ERIC'S PREMO PRIME!",
                  "1. Green Prime - Instant 20 health healed, no skill check needed (2 Medical Supplies)",
                  "2. Red Prime - Instant 20 damage to enemy (1 medical supply)",
                  "3. Blue Prime - 50/50 chance to instantly end combat when used (5 Medical supplies)"]
# The Inventory For The Shop In the gym

consumable = "(consumable)"
sold_out = "Sold Out"
dmg_10 = "(DMG:10)"
dmg_20 = "(DMG:20)"
dmg_30 = "(DMG:30)"
dmg_40 = "(DMG:40)"
dmg_50 = "(DMG:50)"
# Identifiers used for both inventory systems to update variables

action = 0
# Stores the player's action
explored_list = [0, 0, 0, 0, 0, 0]
# List that gets updated to track if a location has been explored, each index value represents a different location
weapon_equiped = inventory[0]
# A variable that defines the item in the first positon of the player's inventory as the currently equipped one
medical_supply = 0
# counter for medical supplies
damage = 10
# player damage counter
gym_entered = False
playerhealth = 100
# player health counter

try:
    import os
    import time
    import sys
    import random
    import colorama
# This tries to import all the libraries that are required to run the games. All but one are pre installed with python

except ModuleNotFoundError:
    print("You seem to be missing a dependency for the game, we will auto-install it for you now.")
    os.system("pip install colorama")
    os.system("py -m install colorama")
    print("The dependency is now installed and we must restart the game")
    input("press enter to restart: ")
    quit()
from colorama import init

init()


# This initalizes colorama

def wipe():
    os.system('cls')


# A kinda cheating way for me to clear the screen after moving to a new location


def slowprint(text, speed=50):
    delay = speed / 1000
    for char in text:
        print(char, end='')
        time.sleep(delay)
    print("\n", end='')


# A function that allows me to have the text print one charater at a time
def tutorial():
    wipe()
    print("TUTORIAL")
    slowprint("Welcome to The Quest for The 3%: Junior Year", 50)
    print()
    slowprint("Selections are listed at the end of a input statement in brackets", 50)
    slowprint("Capitalization and spacing will not matter, so long as the selection is spelt correctly", 50)
    slowprint("If you enter a invalid selection, you will be given a chance to re-enter the selection. ", 50)
    input("Press enter to continue: ")
    print()
    print("EXPLORING")
    slowprint(
        "In all locations, with the exception of the gym, you have a 25% chance of being ambushed, this chance resets every time you explore a location",
        50)
    slowprint("Once a location is explored properly (I.E without being ambushed), there will be nothing else to find",
              50)
    input("Press enter to continue: ")
    print()
    print("COMBAT AND AMBUSHES")
    slowprint(
        "Combat is decided on turn-based skill check system, attacking, healing, checking inventory and checking enemy health will all use up one turn, regardless if you are successful",
        50)
    slowprint("If you are victorious, you will be rewarded with Medical supplies", 50)
    input("Press enter to continue: ")
    print()
    print("MEDICAL SUPPLIES")
    slowprint("Medical supplies can be found in certain locations and gained from winning combat encounters", 50)
    slowprint("Medical supplies can be used to trade from items in the Gym or used to heal yourself in combat", 50)
    slowprint("Without Medical supplies, you will be unable to heal, so please budget accordingly.", 50)
    input("Press enter to end the tutorial: ")
    intro()


# Tutorial section, simple text based tutorial
def quick_time_event(situation):
    if situation == 1:
        start_time = time.time()
        input("You have 3 seconds, Press Enter To Dodge!: ")
        end = time.time
        elapsed = end - start_time
        if elapsed < 3:
            user_reaction = False
        else:
            user_reaction = True
        # tracks the amount of time it took for a user to press enter, and decides if they passed the skill check based on time elapsed
    if situation == 2:
        start_time = time.time()
        input("You have 3 seconds, Press Enter To Perform The Takedown!: ")
        end = time.time
        elapsed = end - start_time
        if elapsed < 3:
            user_reaction = False
        else:
            user_reaction = True
        # tracks the amount of time it took for a user to press enter, and decides if they passed the skill check based on time elapsed
    if situation == 3:
        start_time = time.time()
        input("You have 3 seconds, Press Enter To Jump!: ")
        end = time.time
        elapsed = end - start_time
        if elapsed < 3:
            user_reaction = False
        else:
            user_reaction = True
        # tracks the amount of time it took for a user to press enter, and decides if they passed the skill check based on time elapsed
    return user_reaction


# A function that allows for quicktime events, different situations can be selected via the situation parameter
def skillcheck():
    slowprint("Skillcheck Time!")
    input("Press enter when you are ready: ")
    start_time = time.time()
    num_1 = random.randint(1, 101)
    num_2 = random.randint(1, 101)
    anwser = str(num_1 + num_2)
    user_anwser = input("What is " + str(num_1) + " + " + str(num_2) + ": ")
    end_time = time.time()
    time_elapsed = end_time - start_time
    if user_anwser == anwser and time_elapsed <= 10:
        slowprint("CORRECT!")
        user_correct = True
    elif user_anwser != anwser:
        slowprint("INCORRECT")
        user_correct = False
    elif time_elapsed > 10:
        slowprint("YOU TOOK TOO LONG!")
        user_correct = False
    return user_correct


# A Skillcheck system, asks the user an addition question, and if they get it correct under a certain time limit, it will return true, else it will return false


def combat():
    wipe()
    global enemyhealth
    global enemydamage
    global medical_supply
    enemyhealth = random.randrange(80, 100)
    enemydamage = random.randrange(10, 30)
    global playerhealth
    while enemyhealth > 0 or playerhealth > 0:
        if enemyhealth > 100:
            enemyhealth = 100
        if playerhealth > 100:
            playerhealth = 100
        attackhit = None
        enemyattackhit = random.randrange(0, 20)
        enemymissorhit = random.randrange(0, 20)
        enemyaction = random.randrange(1, 2)
        slowprint("Your HP: " + str(playerhealth), 50)
        playeraction = input("What would you like to do (Heal, Attack, Size Up, Inventory):")
        print("")
        if playeraction.lower() == "inventory":
            print("Equipped: " + inventory[0])
            print()
            print(inventory[1:9], sep="\n")
            print("Medical Supplies:", medical_supply)
            while True:
                try:
                    item_chosen = int(input("Enter The Number of The Item You wish to Use: "))
                except ValueError:
                    input("You have entered a invalid value. Press Enter to Continue: ")
                    continue
                try:
                    if consumable not in inventory[item_chosen]:
                        slowprint("You Cannot Consume a Weapon.")
                    if consumable in inventory[item_chosen]:
                        if "Red" in inventory[item_chosen]:
                            slowprint("You Open The Red Prime, It Instantly Deals Damage To Your Enemy!")
                            enemyhealth -= 20
                            inventory.pop(item_chosen)
                            break
                        if "Green" in inventory[item_chosen]:
                            slowprint("You Drink The Green Prime, You Feel Rejuvenated!")
                            playerhealth += 20
                            inventory.pop(item_chosen)
                            break
                        if "Blue" in inventory[item_chosen]:
                            slowprint("You Open the Blue Prime! The Scent alone makes the enemy not want to fight!")
                            inventory.pop(item_chosen)
                            return
                except IndexError:
                    input("You Have entered a invalid value. Press enter to continue: ")
                    continue
        # Combat inventory logic, this is mainly allows the user to use the bottles of prime they can buy from the gym
        if playeraction.lower() == "heal" and medical_supply > 0:
            medical_supply -= 1
            if medical_supply < 0:
                medical_supply = 0
            playerhealth = playerhealth + 10
            slowprint("You healed! Your health is: " + str(playerhealth), 50)
            print("")
        if playeraction.lower() == "heal" and medical_supply <= 0:
            medical_supply = 0
            slowprint("You Lack The Supplies to Heal Right Now")
        if playeraction.lower() == "size up":
            slowprint("You size up the enemy...", 50)
            print("")
            time.sleep(2)
            if enemyhealth >= 80:
                slowprint("The enemy looks unscathed! Their health is:" + str(enemyhealth), 50)
                print("")
            elif enemyhealth >= 40 and enemyhealth < 80:
                slowprint("The enemy looks minorly damaged! Their health is:" + str(enemyhealth), 50)
                print("")
            elif enemyhealth < 50:
                slowprint("The enemy looks like they are about to faint! Their health is:" + str(enemyhealth), 50)
                print("")
        if playeraction.lower() == "attack":
            slowprint("You ready to attack!")
            print("")
            attackhit = skillcheck()
            if attackhit:
                slowprint("You Hit The Enemy!")
                enemyhealth -= damage
            if not attackhit:
                slowprint("You swung, but you missed")
        if playeraction.lower() != "attack" and playeraction.lower() != "heal" and playeraction.lower() != "size up":
            slowprint("INVALID INPUT", 50)
            continue

        if enemyhealth <= 0:
            slowprint("The enemy falls to the ground... YOU WIN!", 50)
            slowprint("You search the fallen enemy's pockets, and find some medical supplies!")
            medical_found = random.randint(1, 6)
            slowprint("You Found " + str(medical_found) + " Medical Supplies!")
            medical_supply += medical_found
            break
        if enemyaction == 1 and enemyattackhit >= enemymissorhit:
            slowprint("The enemy winds up for an attack!", 50)
            time.sleep(2)
            slowprint("The enemy hits you! The attack stings badly...")
            playerhealth = playerhealth - enemydamage
        if enemyaction == 1 and enemyattackhit <= enemymissorhit:
            slowprint("The enemy winds up for an attack!", 50)
            time.sleep(2)
            print("")
            slowprint("You narrowly dodge the enemy's attack!")
        if enemyaction == 2:
            slowprint("The enemy begins to heal itself!")
            enemyhealth = enemyhealth + random.randrange(10, 20)
        if playerhealth <= 0:
            slowprint("You fall to the ground and faint...")
            loser = input("You Have Lost, Would You Like To Quit, Or Return To The Main Menu? (Menu, Quit): ")
            if loser.lower() == "quit":
                quit()
            if loser.lower() == "menu":
                menu()


# Combat system, The Same as my previous game, but with added skillcheck and inventory functionality

def map():
    wipe()
    global place
    global key1
    place = "test"
    print()
    while place.lower() != "gym" or place.lower() != "commons" or place.lower() != "arts hall" or place.lower() == "floor 1" or place.lower() == "floor1" or place.lower() == "floor 2" or place.lower() == "floor2" or place.lower() == "floor 3" or place.lower() == "floor3" or place.lower() == "machine shop" or place.lower == (
    "machineshop"):
        place = input(
            "Where would you like to go? (Commons, Arts Hall, Gym, Machine Shop, Floor 1, Floor 2, Floor 3):  ")
        if place.lower() == "commons":
            commons()
        if place.lower() == "gym":
            gym()
        if place.lower() == "arts hall" or place.lower() == "artshall":
            arts()
        if place.lower() == "floor 1" or place.lower() == "floor1":
            floor_1()
        if place.lower() == "floor 2" or place.lower() == "floor2":
            floor_2()
        if place.lower() == "floor 3" or place.lower() == "floor3":
            floor_3()
        if place.lower() == "machine shop" or place.lower() == "machineshop":
            machine_shop()
        if place == "problems":
            combat()


# Long story short, if the place variable matches the location, then it calls the location function


def combat_christian():
    wipe()
    global enemyhealth
    global enemydamage
    global medical_supply
    enemyhealth = random.randrange(80, 100)
    enemydamage = random.randrange(10, 30)
    global playerhealth
    while enemyhealth > 0 or playerhealth > 0:
        if enemyhealth > 100:
            enemyhealth = 100
        if playerhealth > 100:
            playerhealth = 100
        attackhit = None
        enemyattackhit = random.randrange(0, 20)
        enemymissorhit = random.randrange(0, 20)
        enemyaction = random.randrange(1, 2)
        slowprint("Your HP: " + str(playerhealth), 50)
        playeraction = input("What would you like to do (Heal, Attack, Size Up, Inventory):")
        print("")
        if playeraction.lower() == "inventory":
            print("Equipped: " + inventory[0])
            print()
            print(inventory[1:9], sep="\n")
            print("Medical Supplies:", medical_supply)
            while True:
                try:
                    item_chosen = int(input("Enter The Number of The Item You wish to Use: "))
                except ValueError:
                    input("You have entered a invalid value. Press Enter to Continue: ")
                    continue
                try:
                    if consumable not in inventory[item_chosen]:
                        slowprint("You Cannot Consume a Weapon.")
                    if consumable in inventory[item_chosen]:
                        if "Red" in inventory[item_chosen]:
                            slowprint("You Open The Red Prime, It Instantly Deals Damage To Christian!")
                            enemyhealth -= 20
                            break
                        if "Green" in inventory[item_chosen]:
                            slowprint("You Drink The Green Prime, You Feel Rejuvenated!")
                            playerhealth += 20
                            break
                        if "Blue" in inventory[item_chosen]:
                            slowprint("Christian Doesn't React To The Blue Prime!")
                            break
                except IndexError:
                    input("You Have entered a invalid value. Press enter to continue: ")
                    continue
        if playeraction.lower() == "heal" and medical_supply > 0:
            medical_supply -= 1
            if medical_supply < 0:
                medical_supply = 0
            playerhealth = playerhealth + 10
            slowprint("You healed! Your health is: " + str(playerhealth), 50)
            print("")
        if playeraction.lower() == "heal" and medical_supply <= 0:
            medical_supply = 0
            slowprint("You Lack The Supplies to Heal Right Now")
        if playeraction.lower() == "size up":
            slowprint("You size up the enemy...", 50)
            print("")
            time.sleep(2)
            if enemyhealth >= 80:
                slowprint("Christian looks unscathed! Their health is:" + str(enemyhealth), 50)
                print("")
            elif enemyhealth >= 40 and enemyhealth < 80:
                slowprint("Christian looks minorly damaged! Their health is:" + str(enemyhealth), 50)
                print("")
            elif enemyhealth < 50:
                slowprint("The enemy looks like they are about to faint! Their health is:" + str(enemyhealth), 50)
                print("")
        if playeraction.lower() == "attack":
            slowprint("You ready to attack!")
            print("")
            attackhit = skillcheck()
            if attackhit:
                slowprint("You Hit Christian!")
                enemyhealth -= damage
            if not attackhit:
                slowprint("You swung, but you missed")
        if playeraction == "win":
            enemyhealth = 0
        if playeraction == "lose":
            playerhealth = 0
        if playeraction.lower() != "attack" and playeraction.lower() != "heal" and playeraction.lower() != "size up":
            slowprint("INVALID INPUT", 50)
            continue

        if enemyhealth <= 0:
            slowprint("Christian falls to the ground... YOU WIN!", 50)
            christian_fight = 1
            return christian_fight
        if enemyaction == 1 and enemyattackhit >= enemymissorhit:
            slowprint("Christian winds up for an attack!", 50)
            time.sleep(2)
            slowprint("Christian hits you! The attack stings badly...")
            playerhealth = playerhealth - enemydamage
        if enemyaction == 1 and enemyattackhit <= enemymissorhit:
            slowprint("Christian winds up for an attack!", 50)
            time.sleep(2)
            print("")
            slowprint("You narrowly dodge the Christian's attack!")
        if enemyaction == 2:
            slowprint("Christian begins to heal himself!")
            enemyhealth = enemyhealth + random.randrange(10, 20)
        if playerhealth <= 0:
            slowprint("You fall to the ground and faint...")
            christian_fight = 0
            return christian_fight


# special combat function for the christian fight

def finalbossfight():
    pass


# Special combat function for the final boss, also contains most of the endings

def machine_shop():
    wipe()
    global explored_list
    global action
    global medical_supply
    global inventory
    global damage
    while place.lower() == "machine shop" or place.lower() == "machineshop":
        wipe()
        slowprint("You enter the machine shop")
        if explored_list[2] == 1:
            slowprint("You see Christian once again, still dribbling that basketball. He invites you to play him again")
        else:
            slowprint("As you walk into the machine shop, you see Christian dribbling a basketball.")
            slowprint(
                "Christian - Hey! You looking for a way into the first floor? Well I've got a cutting torch, if you beat me in a fight I'll give it to you! ")
        player_choice = input("What Would You like to do? (Move/Fight/Inventory): ")
        if player_choice.lower() == "fight":
            torch_fight = combat_christian()
            if torch_fight == 1:
                wipe()
                slowprint("Christian - That Was A Good Fight Man!, Here's The Torch")
                inventory.append(
                    "Cutting Torch - A Butane Cutting Torch, Looks like I Could Use This To Cut Through Some Strong Welds.  (DMG:30)")
                slowprint("CUTTING TORCH OBTAINED! CHECK YOUR INVENTORY TO EQUIP IT!")
                input("Press Enter to Continue: ")
                explored_list[2] = 1
            if torch_fight == 0:
                wipe()
                slowprint("Christian - That Was A Good Try Man... Here's The Torch for your troubles.")
                inventory.append(
                    "Cutting Torch - A Butane Cutting Torch, Looks like I Could Use This To Cut Through Some Strong Welds.  (DMG:30)")
                slowprint("CUTTING TORCH OBTAINED! CHECK YOUR INVENTORY TO EQUIP IT!")
                input("Press Enter to Continue: ")
                explored_list[2] == 1
        # All the code above is the location logic
        if player_choice.lower() == "move":
            map()
        if player_choice.lower() == "inventory":
            wipe()
            print("Equipped: " + inventory[0])
            print()
            print(inventory[1:9], sep="\n")
            print("Medical Supplies:", medical_supply)
            inv_action = input("Would you like to Equip a new weapon? (Y/N): ")
            if inv_action.lower() == "y":
                inv_index = int(input("Please enter the number of the weapon you want to equip: "))
                try:
                    if consumable in inventory[inv_index]:
                        input("You cannot equip a consumable")
                    if consumable not in inventory[inv_index]:
                        inventory.insert(0, inventory.pop(inv_index))
                        if dmg_10 in inventory[0]:
                            damage = 10
                        if dmg_20 in inventory[0]:
                            damage = 20
                        if dmg_30 in inventory[0]:
                            damage = 30
                        if dmg_40 in inventory[0]:
                            damage = 40
                        if dmg_50 in inventory[0]:
                            damage = 50
                            input("NOW EQUIPPED: " + inventory[0] + "! Press enter to return to game: ")
                except IndexError:
                    input("Invalid selection! Please press enter to return to the game: ")


# inventory system, this is baked into every location, this allows a user to switch between weapons and will not allow them to equip consumable items


def floor_3():
    wipe()
    global explored_list
    global action
    global medical_supply
    global inventory
    global damage
    while place.lower() == "floor 3" or place.lower() == "floor3":
        if explored_list[5] != 1:
            slowprint("You can't go to the third floor. The first floor doors are still welded shut")
            input("Press enter to return the map: ")
            map()
        wipe()
        final_decision = input(
            "This is a point of no return. Are you certain you are ready for the final Boss Fight?: (Y/N): ")
        if final_decision.lower() == "n" or final_decision.lower() == "no":
            input("Press Enter to return to the map: ")
            map()
        if final_decision.lower() == "y" or final_decision.lower() == "yes":
            slowprint("You Climb to the third floor...")
            slowprint("It looks like a warzone, SMK students are strewn about, drifting in and out of consciousness")
            slowprint("You look down the hallway. The windows have been broken, and a ladder hangs outside.")
            slowprint(
                "You notice a heavily armored Cardinal Carter student guarding the window. You approach stealthily")
            slowprint(
                "You throw a piece of debris to distract the armored guard, as soon as he turns around you rush to take them down! ")
            takedown = quick_time_event(2)
            if takedown:
                slowprint(
                    "You quickly knock them out, only to hear a classroom door opening further down the hall, and a Cardinal Carter student yell at you to freeze")
                slowprint(
                    "A large amount of Cardinal Carter Students begin to flood the hallway in force. You stand no chance against them. You proceed to make a jump to the ladder!")
                jump = quick_time_event(3)
                if jump:
                    slowprint("You quickly latch onto and climb the ladder, kicking it away once you reach the top...")
                    slowprint(
                        "It is then you see it. A giant blob of Cardinal Carter students, acting as a single entity, as a hivemind.")
                    slowprint("You steel yourself. This seems like it's going to be the final battle...")
                    finalbossfight()
                if not jump:
                    slowprint("You can't work up the nerve to take the leap. You are surrounded and captured By Cardinal Carter Students... It's Over...")
                    slowprint("CAPTURED ENDING: 1/4")
                    input("Press Enter to Quit: ")
                    quit()
            if not takedown:
                slowprint(
                    "The armored student turns around and pushes you away. They then proceed to knock you out with a single punch. When you come too, you realize you have been tied up...")
                slowprint("CAPTURED ENDING: 1/4")
                input("Press Enter to Quit: ")
                quit()


# Floor 3 logic


def floor_2():
    wipe()
    global explored_list
    global action
    global medical_supply
    global inventory
    global damage
    while place.lower() == "floor 2" or place.lower() == "floor2":
        if explored_list[5] != 1:
            slowprint("You can't go to the second floor. The first floor doors are still welded shut")
            input("Press enter to return the map: ")
            map()
        wipe()
        slowprint(
            "You climb Up the stairs to the second floor. This place gives you a uneasy feeling. Almost like it's the final room before a boss fight...",
            50)
        print()
        action = input("What would you like to do (Move,Explore,Inventory): ")
        # GLOBAL VARIABLES AAAAAAAAH
        # And this lets the player to make their choices
        if action.lower == "move":
            map()
            # If the player wants to move then call the map
        if action.lower() == "explore" and explored_list[4] == 1:
            slowprint("You have checked the second floor halls over again, there is nothing left")
            input("Press enter to continue:")
        if action.lower() == "explore" and explored_list[4] == 0:
            ambush = random.randrange(1, 5)
            print()
            slowprint("You look around the second floor hallways...", 50)
            if ambush == 4:
                slowprint("You Have Been Ambushed! Prepare for battle!", 50)
                input("Press enter to start combat:")
                combat()
            else:
                slowprint(
                    "There is a giant table, filled to the brim with medical supplies. There is also a RPG sitting on the table.",
                    50)
                slowprint("There is a note strapped to the RPG: \"Desperate Times May Require Desperate Measures\"")
                medical_supply += 10
                inventory.append("RPG - Desperate Times, Require Desperate Measures... (consumable)")
                input("RPG OBTAINED. IT IS A SINGLE USE CONSUMABLE. USE IT IN THE BOSS FIGHT TO GET THE RPG ENDING")
                explored_list[4] = 1
                input("Press Enter To Continue:")
        if action.lower() == "inventory":
            wipe()
            print("Equipped: " + inventory[0])
            print()
            print(*inventory[1:9], sep="\n")
            print("Medical Supplies:", medical_supply)
            inv_action = input("Would you like to Equip a new weapon? (Y/N): ")
            if inv_action.lower() == "y":
                try:
                    inv_index = int(input("Please enter the number of the weapon you want to equip: "))
                except ValueError:
                    input("You have entered a invalid input. Press enter to continue: ")
                    continue
                try:
                    if consumable in inventory[inv_index]:
                        input("You cannot equip a consumable")
                    if consumable not in inventory[inv_index]:
                        inventory.insert(0, inventory.pop(inv_index))
                        if dmg_10 in inventory[0]:
                            damage = 10
                        if dmg_20 in inventory[0]:
                            damage = 20
                        if dmg_30 in inventory[0]:
                            damage = 30
                        if dmg_40 in inventory[0]:
                            damage = 40
                        if dmg_50 in inventory[0]:
                            damage = 50
                        input("NOW EQUIPPED: " + inventory[0] + "! Press enter to return to game: ")
                except IndexError:
                    input("Invalid selection! Please press enter to return to the game: ")
# Floor 2 Logic

def floor_1():
    wipe()
    global explored_list
    global action
    global medical_supply
    global inventory
    global damage
    while place.lower() == "floor 1" or place.lower() == "floor1":
        wipe()
        if inventory[
            0] != "Cutting Torch - A Butane Cutting Torch, Looks like I Could Use This To Cut Through Some Strong Welds.  (DMG:30)" and \
                explored_list[5] != 1:
            slowprint(
                "The doors to the first floor hallways have been welded shut. I should Equip a Cutting Torch To Get through here. There Should be one in the machine shop.")
            input("Press enter to return to the map: ")
            map()
        if inventory[
            0] == "Cutting Torch - A Butane Cutting Torch, Looks like I Could Use This To Cut Through Some Strong Welds.  (DMG:30)" and \
                explored_list[5] != 1:
            slowprint("After cracking open the first floor doors, something causes the school to shake violently.")
            explored_list[5] = 1
        if explored_list[5] == 1:
            slowprint("you step into the first floor hallway ", 50)
            slowprint(
                "You see two SMK students standing back to back, holding broadswords. Surrounded by Unconsious Cardinal Carter Kids.")
            print()
            action = input("What would you like to do (Move,talk,Inventory): ")
            # GLOBAL VARIABLES AAAAAAAAH
            # And this lets the player to make their choices
            if action == "move" or action == "Move":
                map()
            # If the player wants to move then call the map
            if action.lower() == "talk" and explored_list[3] == 1:
                slowprint("You go to talk to the 2 SMK students again.")
                slowprint("You: Anything new?")
                slowprint("Student 1: Naw, nothing new.")
                input("Press enter to continue:")
            if action.lower() == "talk" and explored_list[3] == 0:
                ambush = random.randrange(1, 5)
                print()
                slowprint("You talk two the two SMK students...", 50)
                slowprint("Student 1: Oh thank God, Someone finally got those doors open!")
                slowprint("Student 2: I Thought we would be stuck here for a while.")
                slowprint("You: No worries. You guys have any idea why this is happening?")
                slowprint(
                    "Student 1: No Clue. I think that these kids are trying to make up for losing the last basketball match against us.")
                slowprint(
                    "Student 2: Yeah, we think their leader is on the third floor. Hopefully beating them up is enough to end this whole thing.")
                slowprint(
                    "Student 1: We were trying to get up there ourselves, but we got ambused by about 2 dozen guys.")
                slowprint("You: I'm Surprised you guys are still standing.")
                slowprint(
                    "Student 2: Same here. Hey, why don't you try and take down their leader? We would, but you know, we are kinda tired.")
                if ambush == 4:
                    slowprint(
                        "You are about to say something, when 3 Cardinal Carter Kids suddenly attack the 3 of you!", 50)
                    input("Press enter to start combat:")
                    combat()
                    slowprint("Upon winning the battle. One of the students throws you a spare Broadsword he has ")
                    inventory.append("Broadsword - A Sword, Imbued with warrior spirit. (DMG:30)")
                    slowprint("BROADSWORD OBTAINED! CHECK YOUR INVENTORY TO EQUIP IT!")
                    input("Press enter to continue: ")
                    explored_list[3] = 1
                else:
                    slowprint("You: Sure, Got anything that would help me?", 50)
                    slowprint(
                        "Student 2: Yeah, Here is a spare sword. Take some of our medical supplies too, we have way too many.",
                        50)
                    inventory.append("Broadsword - A Sword, Imbued with warrior spirit. (DMG:40)")
                    slowprint("BROADSWORD OBTAINED! CHECK YOUR INVENTORY TO EQUIP IT!")
                    slowprint("+ 10 MEDICAL SUPPLIES!")
                    input("Press enter to continue: ")
                    medical_supply = 10
                    explored_list[3] = 1
            if action.lower() == "inventory":
                wipe()
                print("Equipped: " + inventory[0])
                print()
                print(*inventory[1:9], sep="\n")
                print("Medical Supplies:", medical_supply)
                inv_action = input("Would you like to Equip a new weapon? (Y/N): ")
                if inv_action.lower() == "y":
                    try:
                        inv_index = int(input("Please enter the number of the weapon you want to equip: "))
                    except ValueError:
                        input("You have entered a invalid input. Press enter to continue: ")
                        continue
                    try:
                        if consumable in inventory[inv_index]:
                            input("You cannot equip a consumable")
                        if consumable not in inventory[inv_index]:
                            inventory.insert(0, inventory.pop(inv_index))
                        if dmg_10 in inventory[0]:
                            damage = 10
                        if dmg_20 in inventory[0]:
                            damage = 20
                        if dmg_30 in inventory[0]:
                            damage = 30
                        if dmg_40 in inventory[0]:
                            damage = 40
                        if dmg_50 in inventory[0]:
                            damage = 50
                        input("NOW EQUIPPED: " + inventory[0] + "! Press enter to return to game: ")
                    except IndexError:
                        input("Invalid selection! Please press enter to return to the game: ")
#Floor 1 logic

def arts():
    global explored_list
    global action
    global medical_supply
    global inventory
    global damage
    while place.lower() == "art hall" or place.lower() == "arthall":
        wipe()
        slowprint("There is nothing much to see in the commons area", 50)
        print()
        action = input("What would you like to do (Move,Explore,Inventory): ")
        # GLOBAL VARIABLES AAAAAAAAH
        # And this lets the player to make their choices
        if action.lower() == "move":
            map()
            # If the player wants to move then call the map
        if action.lower() == "explore" and explored_list[1] == 1:
            print("You have checked the arts hall over again, there is nothing left")
            input("Press Enter To Continue")
        if action.lower() == "explore" and explored_list[1] == 0:
            print()
            slowprint("You look around the Arts Hall...", 50)
            slowprint(
                "The Hall itself is messy. There is obvious signs of a struggle and dirt tracks leading to the stage")
            slowprint(
                "Upon opening the door to the stage, you hear the sound of something cutting through the air near you")
            if quick_time_event(1):
                slowprint(
                    "You turn around quickly to see a girl in a SMK Uniform swinging a lightsaber down on your head. ")
                slowprint("You quickly dodge out of the way and knock the weapon out of the girl's hand.")
                slowprint(
                    "She apologizes profusely, and lets you keep the lightsaber as you escort her out of the school")
                inventory.append(
                    "Lightsaber - A Lightsaber. It's a prop, but it has some decent weight to it.  (DMG:20)")
                input("LIGHTSABER ADDED TO INVENTORY. Press Enter To Continue:")
                explored_list[1] = 1
            else:
                slowprint("You aren't able to dodge the attack and pass out...", 50)
                slowprint(
                    "When you come to, you see a Cardinal Carter student going through your pockets. He readies to fight you as you stand up.",
                    50)
                combat()
                slowprint(
                    "After Looting The Cardinal Carter Student, you look around the area. Finding A prop lightsaber left behind by someone")
                inventory.append(
                    "Lightsaber - A Lightsaber. It's a prop, but it has some decent weight to it.  (DMG:20)")
                input("LIGHTSABER ADDED TO INVENTORY. Press Enter To Continue:")
                explored_list[1] = 1
        if action.lower() == "inventory":
            wipe()
            print("Equipped: " + inventory[0])
            print()
            print(*inventory[1:9], sep="\n")
            print("Medical Supplies:", medical_supply)
            inv_action = input("Would you like to Equip a new weapon? (Y/N): ")
            if inv_action.lower() == "y":
                try:
                    inv_index = int(input("Please enter the number of the weapon you want to equip: "))
                except ValueError:
                    input("You have entered a invalid input. Press enter to continue: ")
                    continue
                try:
                    if consumable in inventory[inv_index]:
                        input("You cannot equip a consumable")
                    if consumable not in inventory[inv_index]:
                        inventory.insert(0, inventory.pop(inv_index))
                        if dmg_10 in inventory[0]:
                            damage = 10
                        if dmg_20 in inventory[0]:
                            damage = 20
                        if dmg_30 in inventory[0]:
                            damage = 30
                        if dmg_40 in inventory[0]:
                            damage = 40
                        if dmg_50 in inventory[0]:
                            damage = 50
                        input("NOW EQUIPPED: " + inventory[0] + "! Press enter to return to game: ")
                except IndexError:
                    input("Invalid selection! Please press enter to return to the game: ")
#Arts hall logic

def gym():
    global gym_entered
    global action
    global medical_supply
    global inventory
    global damage
    global shop_inventory
    global sold_out
    while place.lower() == "gym":
        if not gym_entered:
            wipe()
            slowprint("As you approach the gym, Robert is standing outside. He's holding a meter stick ", 50)
            print()
            slowprint("Robert - \"Eyyyyyy, How you doing bud? You looking to stock up?\"", 50)
            print()
            slowprint("You - \"Stock up on what?\"", 50)
            print()
            slowprint(
                "Robert - \"Prime man! Eric's started selling some Prime in the Gym, he has been making a killing trading for medical supplies\"")
            print()
            slowprint("Robert - \"You know what? Head on in, then you will see what Im talking about\"", 50)
            input("Press Enter To Continue: ")
            gym_entered = True
        if gym_entered:
            wipe()
            slowprint("You step into the gym, almost half of it is taken up with boxes of prime. Eric waves you over.",
                      50)
            print()
            slowprint("Eric- \"You looking to buy some prime?\"", 50)
            print()
            action = input("What would you like to do (Move,Shop,Inventory):")
            if action.lower() == "move":
                map()
            if action.lower() == "shop":
                wipe()
                print(*shop_inventory, sep="\n")
                print()
                shop_item = int(input("What is the number of the item you want to buy: "))
                if shop_item == 1 and sold_out not in shop_inventory[1]:
                    if medical_supply < 2:
                        slowprint("You cannot afford that", 50)
                    if medical_supply >= 2:
                        medical_supply = medical_supply - 2
                        slowprint("GREEN PRIME ADDED TO INVENTORY!")
                        inventory.append("Green Prime - Lemon lime flavor, instant 20 health healed. (consumable)")
                        shop_inventory.pop(1)
                        shop_inventory.insert(1, "1. Sold Out")
                elif shop_item == 1 and sold_out in shop_inventory[1]:
                    slowprint("Eric - \"Sorry man, Im sold out of that\"", 50)
                if shop_item == 2 and sold_out not in shop_inventory[2]:
                    if medical_supply < 1:
                        slowprint("You cannot afford that", 50)
                    if medical_supply >= 1:
                        medical_supply = medical_supply - 1
                        slowprint("RED PRIME ADDED TO INVENTORY!", 50)
                        inventory.append(
                            "Red Prime - Tropical Punch flavor, instant 20 damage dealt to enemy. (consumable)")
                        shop_inventory.pop(2)
                        shop_inventory.insert(2, "2. Sold out")
                    elif shop_item == 2 and sold_out in shop_inventory[2]:
                        slowprint("Eric - \"Sorry man, Im sold out of that\"", 50)

                if shop_item == 3 and sold_out not in shop_inventory[3]:
                    if medical_supply < 5:
                        slowprint("you cannot afford that", 50)
                    if medical_supply >= 5:
                        medical_supply = medical_supply - 5
                        slowprint("BLUE PRIME ADDED TO INVENTORY!")
                        inventory.append("Blue Prime - Blue Raspberry flavor, ends combat instantly. (consumable)")
                        shop_inventory.pop(3)
                        shop_inventory.insert(3, "3. Sold Out")
                elif shop_item == 3 and sold_out in shop_inventory[3]:
                    slowprint("Eric - \"Sorry man, Im sold out of that\"", 50)
                elif shop_item != 1 and shop_item != 2 and shop_item != 3:
                    slowprint("That's not a valid item")
                    input("Press enter to return to game: ")
            if action.lower() == "inventory":
                wipe()
                print("Equipped: " + inventory[0])
                print()
                print(inventory[1:9], sep="\n")
                print("Medical Supplies:", medical_supply)
                inv_action = input("Would you like to Equip a new weapon? (Y/N): ")
                if inv_action.lower() == "y":
                    inv_index = int(input("Please enter the number of the weapon you want to equip: "))
                    try:
                        if consumable in inventory[inv_index]:
                            input("You cannot equip a consumable")
                        if consumable not in inventory[inv_index]:
                            inventory.insert(0, inventory.pop(inv_index))
                            if dmg_10 in inventory[0]:
                                damage = 10
                            if dmg_20 in inventory[0]:
                                damage = 20
                            if dmg_30 in inventory[0]:
                                damage = 30
                            if dmg_40 in inventory[0]:
                                damage = 40
                            if dmg_50 in inventory[0]:
                                damage = 50
                                input("NOW EQUIPPED: " + inventory[0] + "! Press enter to return to game: ")
                    except IndexError:
                        input("Invalid selection! Please press enter to return to the game: ")
#Gym Logic, Notible difference here is the shop system, it just appends the item to the player's inventory and removes it from the shops inventory after adding it to the players

def commons():
    wipe()
    global explored_list
    global action
    global medical_supply
    global inventory
    global damage
    while place.lower() == "commons":
        wipe()
        slowprint("There is nothing much to see in the commons area", 50)
        print()
        action = input("What would you like to do (Move,Explore,Inventory): ")
        # GLOBAL VARIABLES AAAAAAAAH
        # And this lets the player to make their choices
        if action == "move" or action == "Move":
            map()
            # If the player wants to move then call the map
        if action.lower() == "explore" and explored_list[0] == 1:
            slowprint("You have checked the commons over again, there is nothing left")
            input("Press enter to continue:")
        if action.lower() == "explore" and explored_list[0] == 0:
            ambush = random.randrange(1, 5)
            print()
            slowprint("You look around the commons area...", 50)
            if ambush == 4:
                slowprint("You Have Been Ambushed! Prepare for battle!", 50)
                input("Press enter to start combat:")
                combat()
            else:
                slowprint("Looks like there is a first aid kit hanging on the wall...", 50)
                slowprint("There should be enough in here to heal me 5 times, if I can be efficient with the supplies",
                          50)
                medical_supply = 5
                explored_list[0] = 1
                input("Press Enter To Continue:")

        if action.lower() == "get some bitches":
            print("L + Ratio")
        if action.lower() == "inventory":
            wipe()
            print("Equipped: " + inventory[0])
            print()
            print(*inventory[1:9], sep="\n")
            print("Medical Supplies:", medical_supply)
            inv_action = input("Would you like to Equip a new weapon? (Y/N): ")
            if inv_action.lower() == "y":
                try:
                    inv_index = int(input("Please enter the number of the weapon you want to equip: "))
                except ValueError:
                    input("You have entered a invalid input. Press enter to continue: ")
                    continue
                try:
                    if consumable in inventory[inv_index]:
                        input("You cannot equip a consumable")
                    if consumable not in inventory[inv_index]:
                        inventory.insert(0, inventory.pop(inv_index))
                        if dmg_10 in inventory[0]:
                            damage = 10
                        if dmg_20 in inventory[0]:
                            damage = 20
                        if dmg_30 in inventory[0]:
                            damage = 30
                        if dmg_40 in inventory[0]:
                            damage = 40
                        if dmg_50 in inventory[0]:
                            damage = 50
                        input("NOW EQUIPPED: " + inventory[0] + "! Press enter to return to game: ")
                except IndexError:
                    input("Invalid selection! Please press enter to return to the game: ")
#commons logic

def intro():
    while place == 1:
        wipe()
        slowprint("You made it. Last year was hellish, but you made it, you got that 3%.", 50)
        slowprint(
            "As you step off the bus and walk towards the east side doors, you notice that people are running away from the school?",
            50)
        slowprint("Davis runs up to you: \"Bro you gotta help us out. Cardinal Carter Kids are invading St. Max!\"", 50)
        action = input("What would you like to do (Move): ")
        wipe()
        slowprint("Before you enter St.Max, Davis hands you a Metal Water Bottle.", 50)
        slowprint("Davis: \"It's not the best weapon, but it should help\"", 50)
        slowprint("METAL WATER BOTTLE HAS BEEN ADDED TO YOUR INVENTORY!")
        input(
            "You can check you inventory whenever prompted for a input by entering inventory! Press enter to continue: ")
        if action.lower() == "move":
            map()
        else:
            map()
#Intro "Cinematic"

def menu():
    global new_game
    global place
    global inventory
    global shop_inventory
    global action
    global explored_list
    global medical_supply
    global damage
    global gym_entered
    global playerhealth
    new_game = 0
    place = 1
    inventory = ["Metal Water Bottle - A Metal Water Bottle given to you by Davis (DMG:10)", ]
    shop_inventory = ["ERIC'S PREMO PRIME!",
                      "1. Green Prime - Instant 20 health healed, no skill check needed (2 Medical Supplies)",
                      "2. Red Prime - Instant 20 damage to enemy (1 medical supply)",
                      "3. Blue Prime - 50/50 chance to instantly end combat when used (5 Medical supplies)"]
    action = 0
    explored_list = [0, 0, 0, 0, 0, 0]
    medical_supply = 0
    damage = 10
    gym_entered = False
    playerhealth = 100
    while place == 1:
        wipe()
        print("The Quest for the 3%: Junior year")
        print()

        print()
        new_game = input("Would you like start a new game or Play a tutorial? (Tutorial,New game): ")
        if new_game.lower() == "new game" or new_game.lower() == "newgame":
            intro()
        if new_game.lower() == "tutorial":
            tutorial()
#main menu, this allows the user to check the tutorial, or start a new game. This funtion also resets any persistant variables to default states

print("                THE QUEST FOR THE 3%: Junior Year")
print("                       ICS3U1a")
print("                    January 2023")
print("                  By: Erins Bozhori")
time.sleep(1.0)
place = 1
slowprint("loading: ", 50)
print(" ")
slowprint("____________________________________________________________", 1)
print(" ")
menu()
