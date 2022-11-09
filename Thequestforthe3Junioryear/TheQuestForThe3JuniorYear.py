'''
-------------------------------------------------------------------------------
Name:  TheQuestforthe3%JuniorYear.py
Purpose: A text based adventure game

Author:   Erins Bozhori

Created:  19/10/2022
------------------------------------------------------------------------------
'''
#test
from typing import List

new_game = 0
place = 1
inventory: list[str] = ["Metal Water Bottle - A Metal Water Bottle given to you by Davis (DMG:10)", ]
shop_inventory: list[str] = ["ERIC'S PREMO PRIME!", "1. Green Prime - Instant 20 health healed, no skill check needed (2 Medical Supplies)",
                              "2. Red Prime - Instant 20 damage to enemy (1 medical supply)", "3. Blue Prime - 50/50 chance to instantly end combat when used (5 Medical supplies)"]
consumable = "(Consumable)"
sold_out = "Sold Out"
dmg_10 = "(DMG:10)"
dmg_20 = "(DMG:20)"
dmg_30 = "(DMG:30)"
dmg_40 = "(DMG:40)"
dmg_50 = "(DMG:50)"
action = 0
commons_explored = 0
weapon_equiped = inventory[0]
medical_supply = 0
damage = 10
gym_entered = False
try:
    import os
    import time
    import sys
    import random
    import colorama
#This tries to import all the libraries that are required to run the games. All but one are pre installed with python

except ModuleNotFoundError:
    print("You seem to be missing a dependency for the game, we will auto-install it for you now.")
    os.system("pip install colorama")
    os.system("py -m install colorama")
    print("The dependency is now installed and we must restart the game")
    input("press enter to restart: ")
    quit()
from colorama import init
init()
#This initalizes colorama

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
    slowprint("In all locations, with the exception of the gym, you have a 25% chance of being ambushed, this chance resets every time you explore a location", 50)
    slowprint("Once a location is explored properly (I.E without being ambushed), there will be nothing else to find", 50)
    input("Press enter to continue: ")
    print()
    print("COMBAT AND AMBUSHES")
    slowprint("Combat is decided on D20 dice roll system, attacking, healing, checking inventory and checking enemy health will all use up one turn", 50)
    slowprint("If you are victorious, you will be rewarded with Medical supplies", 50)
    input("Press enter to continue: ")
    print()
    print("MEDICAL SUPPLIES")
    slowprint("Medical supplies can be found in certain locations and gained from winning combat encounters", 50)
    slowprint("Medical supplies can be used to trade from items in the Gym or used to heal yourself in combat",50)
    slowprint("Without Medical supplies, you will be unable to heal, so please budget accordingly.", 50)
    input("Press enter to end the tutorial: ")
    intro()

def map():
    wipe()
    global place
    global key1
    place = "test"
    print()
    while place.lower() != "gym" or place.lower() != "commons" or place.lower() != "arts hall" or place.lower() == "floor 1" or place.lower() == "floor1" or place.lower() == "floor 2" or place.lower() == "floor2" or place.lower() == "floor 3" or place.lower() == "floor3" or place.lower() == "machine shop" or place.lower == ("machineshop"):
        place = input("Where would you like to go? (Commons, Arts Hall, Gym, Floor 1, Floor 2, Floor 3):  ")
        if place.lower() == "commons":
            commons()
        if place.lower() == "gym":
            gym()
        if place.lower() == "arts hall":
            arts()
        if place.lower() == "floor 1" or place.lower() == "floor1":
            floor_1()
        if place.lower() == "floor 2" or place.lower() == "floor2":
            floor_2()
        if place.lower() == "floor 3" or place.lower() == "floor3":
            floor_3()
        if place.lower() == "machine shop" or place.lower() == "machineshop":
            machine_shop()
#Long story short, if the place variable matches the location, then it calls the location function
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
            slowprint("As you approach the gym, Robert is standing outside. He's holding a meter stick ",50)
            print()
            slowprint("Robert - \"Eyyyyyy, How you doing bud? You looking to stock up?\"",50)
            print()
            slowprint("You - \"Stock up on what?\"",50)
            print()
            slowprint("Robert - \"Prime man! Eric's started selling some Prime in the Gym, he has been making a killing trading for medical supplies\"")
            print()
            slowprint("Robert - \"You know what? Head on in, then you will see what Im talking about\"",50)
            gym_entered = True
        if gym_entered:
            wipe()
            slowprint("You step into the gym, almost half of it is taken up with boxes of prime. Eric waves you over.",50)
            print()
            slowprint("Eric- \"You looking to buy some prime?\"",50)
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
                    if medical_supply <= 2:
                        slowprint("You cannot afford that", 50)
                    if medical_supply >= 2:
                        medical_supply = medical_supply - 2
                        slowprint("GREEN PRIME ADDED TO INVENTORY!")
                        inventory.append("Green Prime - Lemon lime flavor, instant 20 health healed. (consumable)")
                        shop_inventory.pop(1)
                        shop_inventory.insert(1,"1. Sold Out")
                if shop_item == 1 and sold_out in shop_inventory[1]:
                    slowprint("Eric - \"Sorry man, Im sold out of that\"", 50)
                if shop_item == 2 and sold_out not in shop_inventory[2]:
                    if medical_supply <= 1:
                        slowprint("You cannot afford that", 50)
                    if medical_supply >= 1:
                        medical_supply = medical_supply - 1
                        slowprint("RED PRIME ADDED TO INVENTORY!", 50)
                        inventory.append("Red Prime - Tropical Punch flavor, instant 20 damage dealt to enemy. (consumable)")
                        shop_inventory.pop(2)
                        shop_inventory.insert(2, "2. Sold out")
                    if shop_item == 2 and sold_out in shop_inventory[2]:
                        slowprint("Eric - \"Sorry man, Im sold out of that\"", 50)

                if shop_item == 3 and sold_out not in shop_inventory[3]:
                    if medical_supply <= 5:
                        slowprint("you cannot afford that", 50)
                    if medical_supply >= 5:
                        medical_supply = medical_supply - 5
                        slowprint("BLUE PRIME ADDED TO INVENTORY!")
                        inventory.append("Blue Prime - Blue Raspberry flavor, 50/50 shot to end combat instantly. (consumable)")
                        shop_inventory.pop(3)
                        shop_inventory.insert(3, "3. Sold Out")
                if shop_item == 3 and sold_out in shop_inventory[3]:
                    slowprint("Eric - \"Sorry man, Im sold out of that\"", 50)
                if shop_item != 1 and shop_item != 2 and shop_item != 3:
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


def commons():
    wipe()
    global commons_explored
    global action
    global medical_supply
    global inventory
    global damage
    while place.lower() == "commons":
      wipe()
      slowprint("There is nothing much to see in the commons area", 50)
      print()
      action = input("What would you like to do (Move,Explore,Inventory): ")
      #GLOBAL VARIABLES AAAAAAAAH
      #And this lets the player to make their choices
      if action == "move" or action == "Move":
        map()
          # If the player wants to move then call the map
      if action.lower() == "explore" and commons_explored == 0:
        ambush = random.randrange(1,5)
        print()
        slowprint("You look around the commons area...", 50)
        if ambush == 4:
            slowprint("You Have Been Ambushed! Prepare for battle!", 50)
            input("Press enter to start combat:")
            combat()
        else:
            slowprint("Looks like there is a first aid kit hanging on the wall...", 50)
            slowprint("There should be enough in here to heal me 5 times, if I can be efficient with the supplies", 50)
            medical_supply = 5
      if action.lower() == "explore" and commons_explored == 1:
          print("You have checked the commons over again, there is nothing left")
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
            inv_index = int(input("Please enter the number of the weapon you want to equip: "))
            try:
                if consumable in inventory[inv_index]:
                    input("You cannot equip a consumable")
                if consumable not in inventory[inv_index]:
                    inventory.insert(0,inventory.pop(inv_index))
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
def intro():
    while place == 1:
        wipe()
        slowprint("You made it. Last year was hellish, but you made it, you got that 3%.", 50)
        slowprint("As you step off the bus and walk towards the east side doors, you notice that people are running away from the school?", 50)
        slowprint("Davis runs up to you: \"Bro you gotta help us out. Cardinal Carter Kids are invading St. Max!\"", 50 )
        action = input("What would you like to do (Move): ")
        wipe()
        slowprint("Before you enter St.Max, Davis hands you a Metal Water Bottle.", 50)
        slowprint("Davis: \"It's not the best weapon, but it should help\"", 50)
        slowprint("METAL WATER BOTTLE HAS BEEN ADDED TO YOUR INVENTORY!")
        input("You can check you inventory whenever prompted for a input by entering inventory! Press enter to continue: ")
        if action.lower() == "move":
            map()
        else:
            map()
def menu():
 while place == 1:
   wipe()
   global new_game
   while new_game == 0:
     print("The Quest for the 3%: Junior year")
     print()

     print()
     new_game = input("Would you like start a new game or Play a tutorial? (Tutorial,New game): ")
     if new_game.lower() == "new game" or new_game.lower() == "newgame":
        intro()
     if new_game.lower() == "tutorial":
        tutorial()


print("                THE QUEST FOR THE 3%: Junior Year")
print("                       ICS3U1a")
print("                    January 2020")
print("                  By: Erins Bozhori")
time.sleep(1.0)
place = 1
slowprint("loading: ", 50)
print(" ")
slowprint("____________________________________________________________", 1)
print(" ")
menu()



