### Main Imports ###
import pickle
import cmd
import textwrap
import sys
import os 
import time
import random
import shelve

### Game Parameters ###
screen_width = 100





### Title ###
def title2():
    print("""
              _____      _      ____        _ _            
             / ____|    | |    / __ \      | (_)           
            | |  __  ___| |_  | |  | |_ __ | |_ _ __   ___ 
            | | |_ |/ _ \ __| | |  | | '_ \| | | '_ \ / _ \\
            | |__| |  __/ |_  | |__| | | | | | | | | |  __/
             \_____|\___|\__|  \____/|_| |_|_|_|_| |_|\___|
 """)


### Color Coding ###
class COLOR:
    PURPLE = '\033[95m'
    blue = '\033[96m'
    DARKblue = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

purple = COLOR.PURPLE
blue = COLOR.blue
dblue = COLOR.DARKblue
blue = COLOR.BLUE
green = COLOR.GREEN
yellow = COLOR.YELLOW
red = COLOR.RED
b = COLOR.BOLD
u = COLOR.UNDERLINE
e = COLOR.END
cyb = b + dblue
title = b + u

### Stored Information ###
chosen_character = ["Dan"]
player_name = ["Luke"]
wifi_password = "KovzhvYirmtNvZNzihyzi" ### Alphabetical Substitution Cipher ### ((PleaseBringMeAMarsbar)) ###
notepad = []
inventory = []
weapons = ['smack', 'metal baton', 'suspicious liquid']
game_attempts = 0
character_names = ["Dan", "Emily", "Ben", "Lana"]
current_chapter = []
fountainluck = 0
food = ['marsbar', 'snickers']
location = ""

### Save and Load ###
    

def loadgame():
    saves = pickle.load(open("saves.dat", "rb"))
    print(saves)

### Open Virtual Notepad ###
def open():
    filename = "/Users/lukeorriss/Desktop/Game/wifi.txt"
    os.system('open ' + filename)


### Character Stats ###
class Dan(object):
    health = 100
    special = "Charm"
    strength = 30
    defence = 5
    snickers = 130
    snickersbar = 1
    baton = 150
    sdefence = 30

class Emily(object):
    health = 100
    special = "Knowledge"
    strength = 30
    defence = 5
    snickers = 130
    snickersbar = 1
    baton = 150

class Ben(object):
    health = 150
    special = "Strength"
    strength = 80
    defence = 20
    snickers = 130
    snickersbar = 1
    baton = 150

class Lana(object):
    health = 100
    special = "Telepathy"
    strength = 30
    defence = 5
    snickers = 130
    snickersbar = 1
    baton = 150

### Boss Stats ###
class Shopkeeper(object):
	name = "Shopkeeper"
	health = 50
	strength = 10
	defence = 5
	weakness = "snickers", "nuts"
	loot = random.randint(0,2)

class Crispman(object):
	name = "Jarred"
	health = 80
	strength = 10
	defence = 6
	weakness = "ready salted crisps"

class Fluffy(object):
	name = "Fluffy"
	health = 60
	strength = 20
	defence = 10
	weakness = "bones"

class finalShopkeeper(object):
	name = "Shopkeeper"
	health = 150
	strength = 40
	strength = 20
	defence = 8

### Win Battle ###
def loot():
	loot = ["big stick", "wooden bat", "packet of ready salted crisps"]
	lootChance = random.randint(0,2)
	lootDrop = loot[lootChance]
	return lootDrop

### Player ###
class player:
    def __init__(self):
        self.name = ""
        self.hp = 100
        self.special = ""
        self.location = ""
        self.gameover = False

### Open notepad and inventory ###
def getnotepad():
    if not notepad:
        print("")
        print(purple + "You have nothing scribbled on your notepad." + e)
    else: 
        print("")
        print(purple + "Scribbled on your notepad you have: " + ", ".join(notepad) + "." + e)

def getinventory():
    if not inventory:
        print("")
        print(purple + "You have nothing stuffed in your pocket." + e)
    else:
        print("")
        print(purple + "Stuffed in your backpack you have: " + ", ".join(inventory) + "." + e)

def cipherkey():
    print("""
 +-------------------------+
 |          A = Z          |
 |          B = Y          |
 |          C = X          |
 |          D = W          |
 |          E = V          |
 |          F = U          |
 |          G = T          |
 |          H = S          |
 |          I = R          |
 |          J = Q          |
 |          K = P          |
 |          L = O          |
 |          M = N          |
 |          N = M          |
 |          O = L          |
 |          P = K          |
 |          Q = J          |
 |          R = I          |
 |          S = H          |
 |          T = G          |
 |          U = F          |
 |          V = E          |
 |          W = D          |
 |          X = C          |
 |          Y = B          |
 |          Z = A          |
 +-------------------------+

 """)

### Reset Game ###
def resetgame():
    inventory.clear()
    notepad.clear()
    chosen_character.clear()
    player_name.clear()

### Save Game ###

### Restart Game ###
def restart():
    if game_attempts >= 0:
        game_attempts + 1
        print("Game Restarting. Please wait...")
        #time.sleep()
        print("You hear muffled voices.")
        #time.sleep()
        print("5, 4, 3, 2, 1... CLEAR!")
        #time.sleep()
        print("Ow! What just happene...")
        #time.sleep()
        print("Clear!")
        #time.sleep()
        print("Everything goes black. Suddenly there is a flash of light...")
        #time.sleep()
        os.system('clear')

### Quit Game ###
def quitgame():
    print(red + "Game Quitting..." + e)
    #time.sleep()
    print("Thank you for playing")
    #time.sleep()
    resetgame()
    sys.exit()

### Chapter 3 Riddle Timer ###
t = 30
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
#countdown(int(t))
#finalShopkeeper

### Final Challenge ###
def finalchallenge():
    os.system('clear')
    while True:
        
        print("What is the wifi password? " + red + wifi_password + e + ". Type help if you're stuck.")
        wifi = input("> ")
        
        if wifi.lower().strip() == 'help':
            print("")
            print("Type " + cyb + "<something to write on>" + e + " for something to write on.")
            print("Type " + cyb + "<cipherkey>" + e + " for your cipherkey.")
            print("When you think you have the wifi password, simply type it in.")
            print("")
        elif wifi.lower().strip() == "cipherkey":
            cipherkey()
        elif wifi.lower().strip() == "something to write on":
            open()
        elif wifi.strip() == "PleaseBringMeAMarsbar":
            print("")
            print(green + "YOU DID IT! GAME COMPLETE. " + e)
            quitgame()
        

### Ending ###
def ending():
    location = "Chapter Five"
    
    time.sleep(3)
    os.system('clear')
    print("Almost as if by magic, the Shopkeeper disappears. Just like that, vanishes into thin air.")
    print("You look down at where he was.")
    print("There it is, Darren's marsbar. Right there on the floor.")
    print("You reach down and pick it up.")
    inventory.append("a marsbar")
    print("")
    print(purple + "A marsbar has been added to your inventory." + e)
    print("")
    print("You have one simple mission now. Go home, give it to Uncle Darren, and get back on the internet.")
    print("")
    print("To start walking home, type " + cyb + "<home>" + e)
    home = input("> ")
    if home.lower().strip() == "home":
        print("")
        print("You start the journey home... It might be a long one, you have no idea where the Shopkeeper lives.")
        print("")
        time.sleep(5)
        print("As you walk out of the door, you get very confused.")
        print(textwrap.fill("You're standing opposite your house, staring straight at your own front door. You turn around, met by empty space. The shopkeepers house has vanished.", 100))
        print("")
        time.sleep(4)
        print("You walk through your front door, relieved by the familiar sound of Uncle Darren shouting at you.")
        print("")
        print(blue)
        text = "Is that you " + ''.join(chosen_character) + ". What took you so long?? Do you have my marsbar?!"
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
        print(e + "")
        print("You give him the marsbar and tell him your story. The crisps, Fluffy, the cavern... He bursts into laughter.")
        print("")
        time.sleep(3)
        print("After some time, he says")
        text2 = "Well, that's some imagination you have... I just sent you down to the shops."
        print(blue)
        for c in text2:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
        print(e + "")
        print("Did you imagine this whole thing? Surely not...")
        time.sleep(15)
        os.system('clear')
        print(green + 'CONGRATULATIONS' + e)
        print("")
        print(textwrap.fill("You have defeated every battle that has been thrown your way. You're a true dungeon explorer. ", 100))
        print("")
        print("If you would like one final challenge, type " + cyb + "<final challenge>" + e + ".")
        final = input("> ")
        if final.lower().strip() == "final challenge":
            finalchallenge()
        else:
            print("That's not quite right... Please try again.")

    

### Chapter 5 ###

def lanabossbattle():
    os.system('clear')
    print("### Shopkeeper Battle: Finale ###")
    print("")
    print("Use the items in your inventory to defeat the Shopkeeper for the final time.")
    print("")
    print("As you take a closer look, you wonder if he got stronger... Perhaps this could be harder than last time.")
    print("")
    if "a makeshift shield" in inventory:
        Lana.defence = 30
    time.sleep(3)
    while finalShopkeeper.health > 0 and Lana.health > 0:
        if "suspicious liquid" in weapons:
            if Lana.health < 20:
                print(red + "You are running low on health. I wonder what the suspicious liquid does..." + e)
                print("")
        # Dynamically prints a list of available weapons or powerups, based on what the user has found throughout the game.
        weap = [x.strip().title() for x in weapons]; weap
        for row in enumerate(weap,1):
            print(*row) 
        print("")
        choice = input("> ")
        os.system('clear')
        if choice.lower().strip() == '1':
            print(b + "### Shopkeeper Battle: Finale ###" + e)
            print("")
            print("You smack the Shopkeeper with your fist.")
            hitchance = random.randint(0,10)
            if hitchance > 1:
                finalShopkeeper.health = finalShopkeeper.health - (Lana.strength / finalShopkeeper.defence)
                print("You hit the Shopkeeper. Their health is now " + red + str(round(finalShopkeeper.health)) + e + ".")
                if finalShopkeeper.health > 0:
                    Lana.health = Lana.health - (finalShopkeeper.strength / Lana.defence)
                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Lana.health)) + e + " left.")
                    print("")
                    if Lana.health <= 0:
                        print("")
                        print("The shopkeeper has killed you.")
                        print("Retry?")
                        retry = input("> ")
                        if retry.lower().strip() in ['y', 'yes']:
                            restart()
                            chapterfourend()
                        elif retry.lower().strip() in ['n', 'no']:
                            quitgame()
                        else:
                            print("Use yes or no.")
                else:
                    print("You have defeated the Shopkeeper.")
                    print("It looks like he dropped something.")
                    ending()
            else:
                print("The shop keeper steps away. You miss.")
                print(red + "The Shopkeeper hits you with everything he has." + e)
                Lana.health = Lana.health - finalShopkeeper.strength
                print("")
                print("You only have " + red + str(round(Lana.health)) + e + " remaining.")
                print("")
                if Lana.health <= 0:
                    print("")
                    print("The shopkeeper has killed you.")
                    print("Retry?")
                    retry = input("> ")
                    if retry.lower().strip() in ['y', 'yes']:
                        restart()
                        lanabossbattle()
                    elif retry.lower().strip() in ['n', 'no']:
                        quitgame()
                    else:
                        print("Use yes or no.")
        elif choice.lower().strip() == '2':
            print(b + "### Shopkeeper Battle ###" + e)
            print("")
            print("You smack the Shopkeeper with the baton.")
            print("")
            hitchance = random.randint(0,10)
            if hitchance > 1:
                finalShopkeeper.health = finalShopkeeper.health - (Lana.baton / Shopkeeper.defence)
                print("You hit the Shopkeeper. Their health is now " + red + str(round(finalShopkeeper.health)) + e + ".")
                if finalShopkeeper.health > 0:
                    Lana.health = Lana.health - (Shopkeeper.strength / Lana.defence)
                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Lana.health)) + e + " left.")
                    print("")
                    if Lana.health <= 0:
                        print("")
                        print("The shopkeeper has killed you.")
                        print("Retry?")
                        retry = input("> ")
                        if retry.lower().strip() in ['y', 'yes']:
                            restart()
                            lanabossbattle()
                        elif retry.lower().strip() in ['n', 'no']:
                            quitgame()
                        else:
                            print("Use yes or no.")
                else:
                    print("")
                    print("You have defeated the Shopkeeper.")
                    time.sleep(4)
                    ending()
            else:
                print("The shop keeper steps away. You miss.")
                print("The Shopkeeper hits you for full damage")
                Lana.health = Lana.health - finalShopkeeper.strength
                print("")
                print("You only have " + red + str(round(Lana.health)) + e + " remaining.")
                print("")
                if Lana.health <= 0:
                    print("")
                    print("The shopkeeper has killed you.")
                    print("Retry?")
                    retry = input("> ")
                    if retry.lower().strip() in ['y', 'yes']:
                        restart()
                        lanabossbattle()
                    elif retry.lower().strip() in ['n', 'no']:
                        quitgame()
                    else:
                        print("Use yes or no.")
        elif choice.lower().strip() == '3':
            weapons.remove("suspicious liquid")
            print("")
            print("You use the suspicious liquid on yourself.")
            print("")
            Lana.health = 100
            print(green + "Your health is now " + red + str(round(Lana.health)) + e + ".")
            print("")

def benbossbattle():
    os.system('clear')
    print("### Shopkeeper Battle: Finale ###")
    print("")
    print("Use the items in your inventory to defeat the Shopkeeper for the final time.")
    print("")
    print("As you take a closer look, you wonder if he got stronger... Perhaps this could be harder than last time.")
    print("")
    if "a makeshift shield" in inventory:
        Ben.defence = 55
    time.sleep(3)
    while finalShopkeeper.health > 0 and Ben.health > 0:
        if "suspicious liquid" in weapons:
            if Ben.health < 20:
                print(red + "You are running low on health. I wonder what the suspicious liquid does..." + e)
                print("")
        # Dynamically prints a list of available weapons or powerups, based on what the user has found throughout the game.
        weap = [x.strip().title() for x in weapons]; weap
        for row in enumerate(weap,1):
            print(*row) 
        print("")
        choice = input("> ")
        os.system('clear')
        if choice.lower().strip() == '1':
            print(b + "### Shopkeeper Battle: Finale ###" + e)
            print("")
            print("You smack the Shopkeeper with your fist.")
            hitchance = random.randint(0,10)
            if hitchance > 1:
                finalShopkeeper.health = finalShopkeeper.health - (Ben.strength / finalShopkeeper.defence)
                print("You hit the Shopkeeper. Their health is now " + red + str(round(finalShopkeeper.health)) + e + ".")
                if finalShopkeeper.health > 0:
                    Ben.health = Ben.health - (finalShopkeeper.strength / Ben.defence)
                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Ben.health)) + e + " left.")
                    print("")
                    if Ben.health <= 0:
                        print("")
                        print("The shopkeeper has killed you.")
                        print("Retry?")
                        retry = input("> ")
                        if retry.lower().strip() in ['y', 'yes']:
                            restart()
                            chapterfourend()
                        elif retry.lower().strip() in ['n', 'no']:
                            quitgame()
                        else:
                            print("Use yes or no.")
                else:
                    print("You have defeated the Shopkeeper.")
                    print("It looks like he dropped something.")
                    ending()
            else:
                print("The shop keeper steps away. You miss.")
                print(red + "The Shopkeeper hits you with everything he has." + e)
                Ben.health = Ben.health - finalShopkeeper.strength
                print("")
                print("You only have " + red + str(round(Ben.health)) + e + " remaining.")
                print("")
                if Ben.health <= 0:
                    print("")
                    print("The shopkeeper has killed you.")
                    print("Retry?")
                    retry = input("> ")
                    if retry.lower().strip() in ['y', 'yes']:
                        restart()
                        benbossbattle()
                    elif retry.lower().strip() in ['n', 'no']:
                        quitgame()
                    else:
                        print("Use yes or no.")
        elif choice.lower().strip() == '2':
            print(b + "### Shopkeeper Battle ###" + e)
            print("")
            print("You smack the Shopkeeper with the baton.")
            print("")
            hitchance = random.randint(0,10)
            if hitchance > 1:
                finalShopkeeper.health = finalShopkeeper.health - (Ben.baton / Shopkeeper.defence)
                print("You hit the Shopkeeper. Their health is now " + red + str(round(finalShopkeeper.health)) + e + ".")
                if Shopkeeper.health > 0:
                    Ben.health = Ben.health - (Shopkeeper.strength / Ben.defence)
                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Ben.health)) + e + " left.")
                    print("")
                    if Ben.health <= 0:
                        print("")
                        print("The shopkeeper has killed you.")
                        print("Retry?")
                        retry = input("> ")
                        if retry.lower().strip() in ['y', 'yes']:
                            restart()
                            benbossbattle()
                        elif retry.lower().strip() in ['n', 'no']:
                            quitgame()
                        else:
                            print("Use yes or no.")
                else:
                    print("")
                    print("You have defeated the Shopkeeper.")
                    time.sleep(4)
                    ending()
            else:
                print("The shop keeper steps away. You miss.")
                print("The Shopkeeper hits you for full damage")
                Ben.health = Ben.health - finalShopkeeper.strength
                print("")
                print("You only have " + red + str(round(Ben.health)) + e + " remaining.")
                print("")
                if Ben.health <= 0:
                    print("")
                    print("The shopkeeper has killed you.")
                    print("Retry?")
                    retry = input("> ")
                    if retry.lower().strip() in ['y', 'yes']:
                        restart()
                        benbossbattle()
                    elif retry.lower().strip() in ['n', 'no']:
                        quitgame()
                    else:
                        print("Use yes or no.")
        elif choice.lower().strip() == '3':
            weapons.remove("suspicious liquid")
            print("")
            print("You use the suspicious liquid on yourself.")
            print("")
            Ben.health = 100
            print(green + "Your health is now " + red + str(round(Ben.health)) + e + ".")
            print("")

def danbossbattle():
    os.system('clear')
    print("### Shopkeeper Battle: Finale ###")
    print("")
    print("Use the items in your inventory to defeat the Shopkeeper for the final time.")
    print("")
    print("As you take a closer look, you wonder if he got stronger... Perhaps this could be harder than last time.")
    print("")
    if "a makeshift shield" in inventory:
        Dan.defence = 30
    time.sleep(3)
    while finalShopkeeper.health > 0:
        if "suspicious liquid" in weapons:
            if Dan.health < 20:
                print(red + "You are running low on health. I wonder what the suspicious liquid does..." + e)
                print("")
        # Dynamically prints a list of available weapons or powerups, based on what the user has found throughout the game.
        weap = [x.strip().title() for x in weapons]; weap
        for row in enumerate(weap,1):
            print(*row) 
        print("")
        choice = input("> ")
        os.system('clear')
        if choice.lower().strip() == '1':
            print(b + "### Shopkeeper Battle: Finale ###" + e)
            print("")
            print("You smack the Shopkeeper with your fist.")
            hitchance = random.randint(0,10)
            if hitchance > 1:
                finalShopkeeper.health = finalShopkeeper.health - (Dan.strength / finalShopkeeper.defence)
                print("You hit the Shopkeeper. Their health is now " + red + str(round(finalShopkeeper.health)) + e + ".")
                if finalShopkeeper.health > 0:
                    Dan.health = Dan.health - (finalShopkeeper.strength / Dan.defence)
                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Dan.health)) + e + " left.")
                    print("")
                    if Dan.health <= 0:
                        print("")
                        print("The shopkeeper has killed you.")
                        print("Retry?")
                        retry = input("> ")
                        if retry.lower().strip() in ['y', 'yes']:
                            restart()
                            chapterfourend()
                        elif retry.lower().strip() in ['n', 'no']:
                            quitgame()
                        else:
                            print("Use yes or no.")
                else:
                    print("You have defeated the Shopkeeper.")
                    print("It looks like he dropped something.")
                    ending()
            else:
                print("The shop keeper steps away. You miss.")
                print(red + "The Shopkeeper hits you with everything he has." + e)
                Dan.health = Dan.health - finalShopkeeper.strength
                print("")
                print("You only have " + red + str(round(Dan.health)) + e + " remaining.")
                print("")
                if Dan.health <= 0:
                    print("")
                    print("The shopkeeper has killed you.")
                    print("Retry?")
                    retry = input("> ")
                    if retry.lower().strip() in ['y', 'yes']:
                        restart()
                        danbossbattle()
                    elif retry.lower().strip() in ['n', 'no']:
                        quitgame()
                    else:
                        print("Use yes or no.")
        elif choice.lower().strip() == '2':
            print(b + "### Shopkeeper Battle ###" + e)
            print("")
            print("You smack the Shopkeeper with the baton.")
            print("")
            hitchance = random.randint(0,10)
            if hitchance > 1:
                finalShopkeeper.health = finalShopkeeper.health - (Dan.baton / Shopkeeper.defence)
                print("You hit the Shopkeeper. Their health is now " + red + str(round(finalShopkeeper.health)) + e + ".")
                if Shopkeeper.health > 0:
                    Dan.health = Dan.health - (Shopkeeper.strength / Dan.defence)
                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Dan.health)) + e + " left.")
                    print("")
                    if Dan.health <= 0:
                        print("")
                        print("The shopkeeper has killed you.")
                        print("Retry?")
                        retry = input("> ")
                        if retry.lower().strip() in ['y', 'yes']:
                            restart()
                            danbossbattle()
                        elif retry.lower().strip() in ['n', 'no']:
                            quitgame()
                        else:
                            print("Use yes or no.")
                else:
                    print("")
                    print("You have defeated the Shopkeeper.")
                    time.sleep(4)
                    ending()
            else:
                print("The shop keeper steps away. You miss.")
                print("The Shopkeeper hits you for full damage")
                Dan.health = Dan.health - finalShopkeeper.strength
                print("")
                print("You only have " + red + str(round(Dan.health)) + e + " remaining.")
                print("")
                if Dan.health <= 0:
                    print("")
                    print("The shopkeeper has killed you.")
                    print("Retry?")
                    retry = input("> ")
                    if retry.lower().strip() in ['y', 'yes']:
                        restart()
                        danbossbattle()
                    elif retry.lower().strip() in ['n', 'no']:
                        quitgame()
                    else:
                        print("Use yes or no.")
        elif choice.lower().strip() == '3':
            weapons.remove("suspicious liquid")
            print("")
            print("You use the suspicious liquid on yourself.")
            print("")
            Dan.health = 100
            print(green + "Your health is now " + red + str(round(Dan.health)) + e + ".")
            print("")

def emilybossbattle():
    os.system('clear')
    print("### Shopkeeper Battle: Finale ###")
    print("")
    print("Use the items in your inventory to defeat the Shopkeeper for the final time.")
    print("")
    print("As you take a closer look, you wonder if he got stronger... Perhaps this could be harder than last time.")
    print("")
    if "a makeshift shield" in inventory:
        Emily.defence = 30
    time.sleep(3)
    while finalShopkeeper.health > 0 and Emily.health > 0:
        if "suspicious liquid" in weapons:
            if Emily.health < 20:
                print(red + "You are running low on health. I wonder what the suspicious liquid does..." + e)
                print("")
        # Dynamically prints a list of available weapons or powerups, based on what the user has found throughout the game.
        weap = [x.strip().title() for x in weapons]; weap
        for row in enumerate(weap,1):
            print(*row) 
        print("")
        choice = input("> ")
        os.system('clear')
        if choice.lower().strip() == '1':
            print(b + "### Shopkeeper Battle: Finale ###" + e)
            print("")
            print("You smack the Shopkeeper with your fist.")
            hitchance = random.randint(0,10)
            if hitchance > 1:
                finalShopkeeper.health = finalShopkeeper.health - (Emily.strength / finalShopkeeper.defence)
                print("You hit the Shopkeeper. Their health is now " + red + str(round(finalShopkeeper.health)) + e + ".")
                if finalShopkeeper.health > 0:
                    Emily.health = Emily.health - (finalShopkeeper.strength / Emily.defence)
                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Emily.health)) + e + " left.")
                    print("")
                    if Emily.health <= 0:
                        print("")
                        print("The shopkeeper has killed you.")
                        print("Retry?")
                        retry = input("> ")
                        if retry.lower().strip() in ['y', 'yes']:
                            restart()
                            chapterfourend()
                        elif retry.lower().strip() in ['n', 'no']:
                            quitgame()
                        else:
                            print("Use yes or no.")
                else:
                    print("You have defeated the Shopkeeper.")
                    print("It looks like he dropped something.")
                    ending()
            else:
                print("The shop keeper steps away. You miss.")
                print(red + "The Shopkeeper hits you with everything he has." + e)
                Emily.health = Emily.health - finalShopkeeper.strength
                print("")
                print("You only have " + red + str(round(Emily.health)) + e + " remaining.")
                print("")
                if Emily.health <= 0:
                    print("")
                    print("The shopkeeper has killed you.")
                    print("Retry?")
                    retry = input("> ")
                    if retry.lower().strip() in ['y', 'yes']:
                        restart()
                        emilybossbattle()
                    elif retry.lower().strip() in ['n', 'no']:
                        quitgame()
                    else:
                        print("Use yes or no.")
        elif choice.lower().strip() == '2':
            print(b + "### Shopkeeper Battle ###" + e)
            print("")
            print("You smack the Shopkeeper with the baton.")
            print("")
            hitchance = random.randint(0,10)
            if hitchance > 1:
                finalShopkeeper.health = finalShopkeeper.health - (Emily.baton / Shopkeeper.defence)
                print("You hit the Shopkeeper. Their health is now " + red + str(round(finalShopkeeper.health)) + e + ".")
                if Shopkeeper.health > 0:
                    Emily.health = Emily.health - (Shopkeeper.strength / Emily.defence)
                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Emily.health)) + e + " left.")
                    print("")
                    if Emily.health <= 0:
                        print("")
                        print("The shopkeeper has killed you.")
                        print("Retry?")
                        retry = input("> ")
                        if retry.lower().strip() in ['y', 'yes']:
                            restart()
                            emilybossbattle()
                        elif retry.lower().strip() in ['n', 'no']:
                            quitgame()
                        else:
                            print("Use yes or no.")
                else:
                    print("")
                    print("You have defeated the Shopkeeper.")
                    time.sleep(4)
                    ending()
            else:
                print("The shop keeper steps away. You miss.")
                print("The Shopkeeper hits you for full damage")
                Emily.health = Emily.health - finalShopkeeper.strength
                print("")
                print("You only have " + red + str(round(Emily.health)) + e + " remaining.")
                print("")
                if Emily.health <= 0:
                    print("")
                    print("The shopkeeper has killed you.")
                    print("Retry?")
                    retry = input("> ")
                    if retry.lower().strip() in ['y', 'yes']:
                        restart()
                        emilybossbattle()
                    elif retry.lower().strip() in ['n', 'no']:
                        quitgame()
                    else:
                        print("Use yes or no.")
        elif choice.lower().strip() == '3':
            weapons.remove("suspicious liquid")
            print("")
            print("You use the suspicious liquid on yourself.")
            print("")
            Emily.health = 100
            print(green + "Your health is now " + red + str(round(Emily.health)) + e + ".")
            print("")

def chapterfivenice():
    print("You seem to be in someone's office.")
    while True:
        climbout = input("> ")
        if climbout.lower().strip() == "look":
            print("")
            print(textwrap.fill("You look around the room, it sure does smell nice. There's a door in front of you... As you look around, you spot a picture on the wall, with many clues on it... Should you take it?", 100))
            take = input("> ")
            if take.lower().strip() in ['y', 'yes']:
                print("")
                print(textwrap.fill("Upon closer inspection, this scroll seems to match the clues that you have been following.", 100))
                print("")
                print(purple + "A cipher key has been added to your inventory." + e + " To view it, type " + cyb + "<cipherkey>" + e + ".")
        elif climbout.lower().strip() == "cipherkey":
            cipherkey()
        elif climbout.lower().strip() in ['i door', 't door', 'go through door', 'door']:
            print("")
            print(textwrap.fill("You open the door slowly and go through. It opens into a stretching corridor. You creep through, taking in your surroundings.", 100))
            time.sleep(3)
            print("")
            print(textwrap.fill("Suddenly, a figure appears at the end of the corridor. The same man as before, the Shopkeeper. You should have known it was his house. What a weirdo.", 100))
            time.sleep(4)
            if "Dan" in chosen_character:
                danbossbattle()
            elif "Ben" in chosen_character:
                benbossbattle()
            elif "Emily" in chosen_character:
                emilybossbattle()
            elif "Lana" in chosen_character:
                lanabossbattle()

def chapterfivenotnice():
    print("You seem to be in someone's office.")
    print("")
    print(textwrap.fill("Then you notice him. Slumped in his chair. The same man as before. The shopkeeper. You should have known it was him that had set all of this up. Only someone with a twisted mind would put someone through all of this torture.", 100))
    print("")
    #time.sleep()
    print("He sees you.")
    #time.sleep()
    print("He spins around on his chair to get a better look at you. He goes quiet...")
    print("")
    print("All of a sudden, he screams:")
    text = "WHAT DO YOU THINK YOU ARE DOING HERE? IN MY HOUSE."
    text2 = "YOU WILL REGRET THE DAY THAT YOU WERE BORN BOY. LET'S SETTLE THIS, ONCE AND FOR ALL!"
    text3 = "YOU WILL REGRET THE DAY THAT YOU WERE BORN GIRL. LET'S SETTLE THIS, ONCE AND FOR ALL!"
    print(blue)
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")
    print("")
    if chosen_character in ['Dan', 'Ben']:
        for c in text2:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.04)
        print("")
    else:
        for c in text3:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.04)
        print("")
    print(e + "")
    if "Dan" in chosen_character:
        danbossbattle()
    elif "Ben" in chosen_character:
        benbossbattle()
    elif "Emily" in chosen_character:
        emilybossbattle()
    elif "Lana" in chosen_character:
        lanabossbattle()
    


### Chapter 4 end ###
def chapterfourend():
    os.system('clear')
    location = "Chapter Four End"
    
    print("Once at the other side, you can see the ladder... What could be up there...")
    while True:
        response = input("> ")
        if response.lower().strip() == "look":
            print("")
            print(textwrap.fill("You look around the platform you are on. To the East there seems to be something metal lying on the floor. You can't see what it is, though it is shining in the candlelight. To the West there is the ladder, it looks like it could be a way out. To your north there is a chest.", 100))
            print("")
            while True:
                investigate = input("> ")
                if investigate.lower().strip() in ['i object', 'i shiny', 'i metal', 'i metal object', 'i thing', 'i unknown', 't east', 'travel east']:
                    if "a metal baton" in inventory:
                        print("You have already picked up the baton.")
                    elif "a metal baton" not in inventory:
                        print("")
                        print(textwrap.fill("You wander over to the object. Upon closer inspection it is clear to you that it is a metal baton... It looks to be sturdy and strong... It's not amazing, but it's something. Do you pick it up?", 100))
                        
                        baton = input("> ")
                        if baton.lower().strip() in ['y', 'yes']:
                            print("")
                            print(purple + "A metal baton has been added to your inventory." + e)
                            weapons.append("a metal baton")
                            print("")
                            print(textwrap.fill("There is also a vial of what seems to be red liquid next to the baton. Do you want to take it?", 100))
                            vial = input("> ")
                            if vial.lower().strip() in ['y', 'yes']:
                                print("")
                                print(purple + "A bottle of suspicious liquid has been added to your inventory." + e)
                                weapons.append("suspicious liquid")
                            continue
                        else:
                            print("")
                            print("You leave the baton alone.")
                            continue
                elif investigate.lower().strip() in ['t ladder', 'i ladder', 'ladder', 'the ladder', 'west', 't west', 'travel west']:
                    print("")
                    print("You wander over to the ladder.")
                    print("Do you climb it?")
                    climb = input("> ")
                    if climb.lower().strip() in ['y', 'yes']:
                        print("")
                        print("You start to climb the ladder.")
                        time.sleep(3)
                        print("As you reach the top you can hear voices...")
                        print("Do you open the hatch and go through or wait until its quiet?")
                        wait = input("> ")
                        if wait.lower().strip() in ['wait', 'wait until clear', 'wait clear', 'wait until quiet', 'wait quiet']:
                            print("")
                            print("You wait until there is no sound... You open the hatch.")
                            time.sleep(4)
                            print("As you peer into the room above, you see that you are in someones house... ")
                            print("")
                            print("You climb out...")
                            time.sleep(3)
                            chapterfivenice()
                        elif wait.lower().strip() in ['open', 'go through', 'open the hatch', 'go through the hatch']:
                            print("")
                            print("You open and go through the hatch...")
                            time.sleep(4)
                            chapterfivenotnice()

                            
                    elif climb.lower().strip() in ['no', 'n']:
                        print("You ignore the ladder.")
                        continue
                    else:
                        print("")
                        print("Please use a yes or no answer.")
                elif investigate.lower().strip() in ['t north', 'i north', 'i chest', 't chest']:
                    print("")
                    print("You wander over to the chest. It's unlocked...")
                    print("")
                    print("You open it.")
                    print("")
                    print(textwrap.fill("Inside there seems to be some form of metal plate with a handle.. It kind of resembles a shield. Would you like to pick it up?", 100))
                    pick = input("> ")
                    if pick.lower().strip() in ['y', 'yes']:
                        print("")
                        print(purple + "A makeshift shield has been added to your inventory." + e)
                        inventory.append("a makeshift shield")
                    else:
                        print("")
                        print("You leave the makeshift shield alone.")
                elif investigate.lower().strip() == "inventory":
                    getinventory()
                elif investigate.lower().strip() == "notepad":
                    getnotepad()
                elif investigate.lower().strip() == "help":
                    print("")
                    print(green + "Your aim is simple, you need to get to the ladder. If you lost your items, you may find it helpful to see if there is anything in the room that will aid you on your mission. If you still have your items, some more tools wouldn't go a miss. ")
                else:
                    print("")
                    print("Please use a travel or inspect command.")
        else:
            print("")
            print("Look around to find out more.")


### Chapter 4 ###
def chapterfour():
    os.system('clear')
    location = "Chapter Four"
    
    print("""
                             """ + title + """### Chapter Four: The Cavern ###""" + e + """
    """)
    print("")
    print("You reach the door, stuffing the key into the golden padlock. You dive through, slamming it behind you.")
    #time.sleep()
    print("")
    print("That was a close one... You think to yourself. ")
    print("")
    print(textwrap.fill("You spin around to assess your new room. A wide cavern lit by candlelight, the floor filled by a bottomless pit. You walk to the edge of the hole, picking up a stone and throwing it in. It never hits the bottom.", 100))
    while True:
        look = input("> ")
        if look.lower().strip() in ['look around', 'search', 'search room', 'look']:
            print("")
            print(textwrap.fill("You search the room. To your east, a ladder stands on the other side of the pit. You're not sure where it goes, although there seems to be a slight glow of light coming from the roof in that area.. Perhaps that is the way out. Upon closer inspection, there looks to be two possible routes for getting across... A dangerous, rewarding path - a rickety plank stretching across the pit. Or, a thin ledge around the edge of the hole. It's a far safer route, but it isn't big enough for you and your backpack. You'll have to leave your belongings behind...  ", 100))
            print("")
            print(textwrap.fill("Do you choose to walk the plank, or make your way around? If you choose to walk the plank, there will be a high chance of death. However, if you choose to walk around, you will leave this area with nothing. Think wisely.", 100))
            print("")
            print(textwrap.fill("You can inspect either choice further, if you need more information to make your decison. When you are ready to make a decision, on the direction you would like to travel. Use the travel command.", 100))
            while True:
                choice = input("> ")
                if choice.lower().strip() in ['i walk plank', 'i plank', 'i risky', 'i risky choice', 'i walk the plank', 'i cavern']:
                    if "Emily" in chosen_character:
                        print("")
                        print(textwrap.fill("You stare long and hard at the plank... You do the maths in your head. If your calculations are correct, which they are... You should be able to walk across the plank without a problem. It should be more than strong enough to support the weight of you and your bag.", 100))
                    elif fountainluck == 1:
                        print("")
                        print(textwrap.fill("You believe that luck is on your side. Let's hope your luck doesn't run out. ", 100))
                    else:
                        print("")
                        print(textwrap.fill("You're not sure whether you have the best chance at survival if you try to walk across the plank... Although there is a chance. Maybe it would be best if you walk around... But that decision is yours to make.", 100))
                elif choice.lower().strip() in ['i walk around', 'i around the outside', 'i around', 'i safe', 'i outside', 'i safe route']:
                    print("")
                    print(textwrap.fill("You look around the cavern. You can see that there is a narrow path around the perimeter. It looks as though it is stable enough to support you. Although there is not enough room for you and your bag. As there is a small gap that requires you to squeeze through.", 100))
                elif choice.lower().strip() in ['t walk plank', 't plank', 't risky', 't risky choice', 't walk the plank', 't cavern']:
                    if "Emily" in chosen_character or fountainluck == 1:
                        print(textwrap.fill("You slowly start to make your way across the cavern. So far, it seems as though it is supporting your weight. Let's hope that you make it.", 100))
                        print("")
                        print(red + "Walking Across..." + e)
                        time.sleep(5)
                        survive = random.randint(0,10)
                        if survive < 1:
                            print("")
                            print(textwrap.fill("As you walk across the cavern, you hear Fluffy run and leap at the door... The force of him hitting the door shakes the plank you are walking across. You slip and lose your balance.", 100))
                            print("")
                            print("Retry?")
                            while True:
                                response = input("> ")
                                if response.lower().strip() in ['y', 'yes']:
                                    restart()
                                    chapterfour()
                                elif response.lower().strip() in ['n', 'no']:
                                    quitgame()
                        elif survive > 1:
                            print("")
                            print(textwrap.fill("You made it! Your extreme dexterity allowed you to maintain your balance. Whilst your daring attitude allowed you to survive and keep your items. Good work.", 100))
                            chapterfourend()
                                  
                    else:
                        print("You slowly start to make your way across the cavern... ")
                        print("")
                        print("The further you get across, the more it starts to creek.")
                        survive = random.randint(0,10)
                        if survive > 3:
                            time.sleep(5)
                            print("")
                            print(textwrap.fill("Suddenly, you hear a snap... The plank splits in half, you plummet...", 100))
                            print("")
                            print("Retry?")
                            while True:
                                response = input("> ")
                                if response.lower().strip() in ['y', 'yes']:
                                    restart()
                                    chapterfour()
                                elif response.lower().strip() in ['n', 'no']:
                                    quitgame()
                        else:
                            print("")
                            print("The plank starts to crack and fall beneath your feet. You LEAP for the other side....")
                            time.sleep(5)
                            print("")
                            print("You made it! It might not have been an easy task, but you did it. You step off the plank and take a sigh of relief.")
                            chapterfourend()

                elif choice.lower().strip() in ['t walk around', 't around the outside', 't around', 't safe', 't outside', 't safe route']:
                    print("")
                    print("You start to walk around the cavern... It sure is a long walk.")
                    print("")
                    print(textwrap.fill("You reach the point that is not big enough for you and your bag to go through. Do you chuck the bag into the cavern and continue, or walk back to take the other option?", 100))
                    response = input("> ")
                    if response.lower().strip() in ['go back', 'travel back', 'walk back', 'back']:
                        print("You slowly make your way back.")
                        print("")
                        print("You can either investigate another option, or choose a different direction.")
                    elif response.lower().strip() in ['carry on', 'forward', 'continue', 'keep going', 'chuck bag', 'chuck', 'chuck bag in cavern']:
                        print("")
                        print("You chuck your bag into the cavern and watch it float down slowly...")
                        inventory.clear()
                        print("")
                        print(textwrap.fill("You make it to the otherside unharmed. As you step onto solid ground again, you take a sigh of relief.", 100))
                        time.sleep(5)
                        chapterfourend()
                elif choice.lower().strip() == "notepad":
                    getnotepad()
                elif choice.lower().strip() == "inventory":
                    getinventory()
                else:
                    print("")
                    print("Please choose an investigate or travel command. Use " + cyb + "<i/t>" + e + " followed by the area of your choice.")

### Fluffy win ###
def fluffywin():
    print("")
    print("Fluffy has caught you. He eats you whole...")
    print("")
    print("Restart?")
    restarts = input("> ")
    if restarts.lower().strip() in ['y', 'yes']:
        restart()
        chapterthreechase()
    else:
        print("")
        print("Are you sure you want to quit?")
        while True:
            quitt = input("> ")
            if quitt.lower().strip() in ['y', 'yes']:
                quitgame()
            else:
                restart()
                chapterthreechase()

## Chapter 3 Chase ###
def chapterthreechase():
    os.system('clear')
    location = "Chapter Three Chase"
    
    print("You make a run for the door.")
    print("")
    #time.sleep()
    print("Fluffy is hot on your heels.")
    print("")
    #time.sleep()
    print(textwrap.fill(b + red + "Welcome to the chase. Get a question right and you continue. Get one wrong and Fluffy will gain on you. 3 wrong and you lose." + e, 100))
    Fluffy = 30
    while Fluffy > 0:
        print("")
        print(yellow + "Question 1: What is Mr O'donohue's wifes name?" + e)
        qonea = input("> ")
        if qonea.lower().strip() == "notepad":
            getnotepad()
        elif qonea.lower().strip() != "ann":
            print("")
            print(red + "Wrong!" + e + " Fluffy is gaining on you.")
            Fluffy = Fluffy - 10
            if Fluffy == 0:
                fluffywin()
        else:
            print("")
            print(green + "Correct!" + e + " You stay ahead of fluffy.")
            #time.sleep()
            print("")
            while Fluffy > 0: 
                print("")
                print(yellow + "Question 2: The more you take, the more you leave behind. What am I?" + e)
                qtwoa = input("> ")
                if qtwoa.lower().strip() not in ['footsteps', 'steps']:
                    print("")
                    print(red + "Wrong!" + e + " Fluffy is gaining on you.")
                    Fluffy = Fluffy - 10
                    if Fluffy == 0:
                        fluffywin()
                elif qtwoa.lower().strip() == "notepad":
                    getnotepad()
                else:
                    print("")
                    print(green + "Correct!" + e + " You stay ahead of fluffy.")
                    #time.sleep()
                    print("")
                    while Fluffy > 0: 
                        print(yellow + "Question 3: What has a head, a tail, has no legs and is brown?" + e)
                        qtwoa = input("> ")
                        if qtwoa.lower().strip() not in ['penny', 'a penny', '1p', '2p', '1p coin', '2p coin', 'coin']:
                            print(red + "Wrong!" + e + " Fluffy is gaining on you.")
                            Fluffy = Fluffy - 10
                            if Fluffy == 0:
                                fluffywin()
                        elif qtwoa.lower().strip() == "notepad":
                            getnotepad()
                        else:
                            print("")
                            print(green + "Correct!" + e + " You stay ahead of fluffy.")
                            #time.sleep()
                            print("")
                            while Fluffy > 0: 
                                print(yellow + "Question 4: What is more useful when it's broken?" + e)
                                qtwoa = input("> ")
                                if qtwoa.lower().strip() not in ['egg', 'an egg', 'eggs']:
                                    print(red + "Wrong!" + e + " Fluffy is gaining on you.")
                                    Fluffy = Fluffy - 10
                                    if Fluffy == 0:
                                        fluffywin()
                                elif qtwoa.lower().strip() == "notepad":
                                    getnotepad()
                                else:
                                    print("")
                                    print(green + "Correct!" + e + " You stay ahead of fluffy.")
                                    #time.sleep()
                                    print("")
                                    while Fluffy > 0: 
                                        print(yellow + "Question 5: Before Mount Everest was discovered, what was the highest mountain on Earth?" + e)
                                        qtwoa = input("> ")
                                        if qtwoa.lower().strip() not in ['mount everest']:
                                            print(red + "Wrong!" + e + " Fluffy is gaining on you.")
                                            Fluffy = Fluffy - 10
                                            if Fluffy == 0:
                                                fluffywin()
                                        elif qtwoa.lower().strip() == "notepad":
                                            getnotepad()
                                        else:
                                            print("")
                                            print(green + "Correct!" + e + " You stay ahead of fluffy.")
                                            print("")
                                            print(textwrap.fill("You have survived... You made it out alive. A congratulations is in order... Maybe. Probably not...", 100))
                                            time.sleep(3)
                                            chapterfour()

### Chapter 3 ###
def chapterthree():
    os.system('clear')
    location = "Chapter Three"
    
    print("""
                             """ + title + """### Chapter Three: Fluffy ###""" + e + """
    """)
    print("")
    print(textwrap.fill("You stagger through the large metal door... Into another dark and eery room. There is a candle in the centre of the room, emitting enough light to barely see where you are going.", 100))
    print("")
    print("There seems to be an obscure shadow lurking in the corner. You hear a slight rustle of chains.")
    print("")
    while True:
        chthree = input("> ")
        if chthree.lower().strip() in ['look around', 'search', 'search room', 'look']:
            print("")
            print(textwrap.fill("As your eyes adjust to the light, it becomes clear that the unknown shadow is in fact a dog. Not just any dog... It has three heads. THREE. Who or what would create such a monster. The three headed beast lies to your East, whilst to the West is the remains of what looks to be a human skeleton. Far in front to the North, you can see a large wooden door, with a golden padlock.", 100))
            print("")
            print("Either travel in a direction, or investigate an option some more.")
            print("")
            while True:
                investigate = input("> ")
                if investigate.lower().strip() in ['i dog', 'i three headed dog', 'dog']:
                    print(textwrap.fill("You approach the three headed beast, its body rising and falling with heavy breaths. As you get closer, you spot a nametag: FLUFFY. The dog shifts in its sleep, dreaming of rabbits. It rolls to the side, revealing a heavy golden key trapped beneath its paws.", 100))
                elif investigate.lower().strip() in ['i door', 'i wooden door', 'i golden padlock', 'i padlock',]:
                    print(textwrap.fill("A massive wooden door. It looks like a perfect escape. If only you had the key.", 100))
                elif investigate.lower().strip() in ['i skeleton', 'i remains', 'i dead body', 'i body', 'i person', 'i dead person']:
                    print("")
                    print(textwrap.fill("A skeleton. The beast must have left this here. What sick person would feed a human to this creature. Maybe it was one of the characters from earlier... That's a little concerning... ", 100))
                    print("")
                    print(textwrap.fill("As you get closer, you notice something... A lose bone sticking out next to the leg, it may come in handy. There also seems to be an enscription on the skull. It reads: " + blue + "Here lies Mr O'donohue. A quaint and secretive man, but do not be fooled, for he was married to Zmm. (A = Z)" + e, 100))
                    print("")
                    print("Perhaps these could be useful... Would you like to pick up the bone and make a note of the clue?")
                    while True:
                        clue = input("> ")
                        if clue.lower().strip() in ['y', 'yes']:
                            print("")
                            print(purple + "You pick up a human bone, and write down 'Rhyme: Married to Zmm?', A = Z." + e)
                            inventory.append("a human bone")
                            notepad.append("Rhyme: Married to Zmm? A = Z")
                            break
                        else:
                            print("")
                            print("You leave the skeleton alone... If you change your mind, you can always come back.")
                            break
                elif investigate.lower().strip() in ['t east', 'travel east', 't dog', 't fluffy', 'travel dog', 'travel fluffy', 't three headed dog', 'travel three headed dog']:
                    print("")
                    print(textwrap.fill("You slowly creep over to the dog... It hears you...", 100))
                    if "Lana" in chosen_character:
                        print("")
                        print("Would you like to try and ask the dog for the key, using your animal telepathy?")
                        tele = input("> ")
                        if tele.lower().strip() in ['y', 'yes']:
                            print("")
                            print("You try to explain to the dog what is happening... He seems to understand. He looks at you with three concerned and thoughtful faces, as he backs away from the key.")
                            print("")
                            print("Pick up the key?")
                            pickup = input("> ")
                            if pickup.lower().strip() in ['y', 'yes']:
                                print("")
                                print(purple + "A golden key has been added to your inventory.")
                                inventory.append("a golden key")
                                print("")
                                print("Would you like to go through the door?")
                                leave = input("> ")
                                if leave.lower().strip() in ['y', 'yes']:
                                    chapterfour()
                                else:
                                    break
                            else:
                                print("")
                                print("You leave the key where it is... Without it, there might not be a way out.")
                        else:
                            print("")
                            print("You try to pick up the key without asking... ")
                            time.sleep(3)
                            chapterthreechase()
                    else:
                        print("")
                        print("Do you try to grab the key? Or throw the bone to distract him.")
                        throw = input("> ")
                        if throw.lower().strip() in ['throw', 'throw the bone', 'throw bone']:
                            print("")
                            print("You throw the bone. Fluffy jumps to his feet, lumbering after it. You quickly grab the key.")
                            inventory.remove("a human bone")
                            print("")
                            print(purple + "A golden key has been added to your inventory." + e)
                            inventory.append("a golden key")
                            print("")
                            print("As you grab the key, Fluffy turns around and looks at you. He growls. RUN!")
                            time.sleep(5)
                            chapterthreechase()
                        elif throw.lower().strip() in ['grab key', 'key', 'get key', 'reach for key']:
                            print("")
                            print("The dog snaps at your arm, just missing you as you grab the key. He growls and leaps to his feet.")
                            print("")
                            print("Do you accept defeat, or try to run?")
                            while True:
                                run = input("> ")
                                if run.lower().strip() in ['run', 'try to run', 'leggit', 'gtfo']:
                                    chapterthreechase()
                                else:
                                    print("")
                                    print("Do you want to quit the game?")
                                    quitt = input("> ")
                                    if quitt in ['y', 'yes']:
                                        quitgame()
                                    else:
                                        break
                        else:
                            print("")
                            print("Choose whether you want to throw the bone to distract, or grab the key. ")
                elif investigate.lower().strip() in ['t north', 'travel north', 't door', 't padlock', 'travel golden padlock', 'travel door']:
                    print("")
                    print("You wander over to the wooden door... It's locked... Perhaps there is a key somewhere... You should investigate further.")
                elif investigate.lower().strip() == "notepad":
                    getnotepad()
                elif investigate.lower().strip() == "inventory":
                    getinventory()
                else:
                    print("")
                    print("Please choose one of the available options. Either travel or investigate an object or direction " + cyb + "<t/i>" + e + ".")
                    continue
        elif chthree.lower().strip() == "notepad":
            getnotepad()
        elif chthree.lower().strip() == "inventory":
            getinventory()
        elif chthree.lower().strip() == "quit":
            print("")
            print("Are you sure you want to quit?")
            while True:
                quitt = input("> ")
                if quitt.lower().strip() in ['y', 'yes']:
                    quitgame()
                else:
                    break
        

### Chapter 2 ###
def chaptertwo():
    os.system('clear')
    location = "Chapter Two"
    
    print("""
                             """ + title + """### Chapter Two: Crispy ###""" + e + """
    """)
    print(textwrap.fill("You stick your head through the hole, looking into a dark and gloomy store room. As you ease in further, you can see something laying in front of you. It's an empty packet of crisps, how strange...", 100))
    print("Search the room for things of interest.")
    print("")
    while True:
        search = input("> ")
        if search.lower().strip() == "look":
            print("")
            print(textwrap.fill("As you look around the room, there are a number of things you notice. Firstly, there seems to be an endless supply of food down here. Everywhere you look there are crisps, sandwiches and caprisun's... To your east you can see a giant man, slouching in front of a metal door. To your west you can see a large stack of crates, with unopened crisps inside. To your North, there is a bin filled to the brim with empty packets of ready salted crisps. You think to yourself, Perhaps the man is responsible for those...", 100))
            print("")
            print("Move in one of the directions.")
            while True:
                move = input("> ")
                if move.lower().strip() in ['t west', 'travel west']:
                    print("")
                    print(textwrap.fill("You wander over to the stack of crisps. You can see, ready salted, salt and vinegar, cheese and onion and prawn cocktail.\nDo you pick up a packet?", 100))
                    crisps = input("> ")
                    if crisps.lower().strip() in ['yes', 'y']:
                        print("Which flavour?")
                        pickcrisps = input("> ")
                        if pickcrisps.lower().strip() in ['readysalted', 'ready salted', 'ready-salted', 'salted', 'the red ones', 'red']:
                            inventory.append("a packet of ready salted crisps")
                            print("")
                            print(purple + "A packet of ready salted crisps has been added to your inventory" + e)
                            print("")
                            inventory.append("a packet of ready salted crisps") 
                        elif pickcrisps.lower().strip() in ["prawn cocktail", "prawn and cocktail"]:
                            print(purple + "A packet of prawn cocktail crisps has been added to your inventory" + e)
                            print("")
                            inventory.append("a packet of prawn cocktail crisps.")
                        elif pickcrisps.lower().strip() in ['salt and vinegar', 'salt n vinegar']:
                            print(purple + "A packet of salt and vinegar crisps has been added to your inventory" + e)
                            print("")
                            inventory.append("a packet of salt and vinegar crisps")
                        elif pickcrisps.lower().strip() in ['cheese and onion', 'cheese n onion']:
                            print(purple + "A packet of cheese and onion crisps has been added to your inventory" + e)
                            print("")
                            inventory.append("a packet of cheese and onion crisps")
                        else:
                            print("Please use the above flavours.")
                elif move.lower().strip() in ['t east', 'travel east']:
                    if "a packet of ready salted crisps" not in inventory:
                        print("")
                        print("As you walk towards the man slouched on the floor, he starts to speak to you.")
                        slman = "You don't work here! What do you think you're doing!"
                        print(blue)
                        for c in slman: 
                            sys.stdout.write(c)
                            sys.stdout.flush()
                            time.sleep(0.04)
                        print(e)
                        print("")
                        print("As the man talks, you seem confused. Almost as if the voice doesn't match the friendly face that sits before you.")
                        print("")
                        print("Type speech, to try and talk yourself out of it.")
                        while True:
                            speech = input("> ")
                            if speech.lower().strip() in ['talk out', 'talk', 'speech', 'conversation']:
                                print("""
 You seem to have landed in a sticky situation. Do you tell

 1. The truth.

 2. A little lie. 

 3. A big lie.
 
 Type the number of your response.
                                """)
                                success = input("> ")
                                if success.lower().strip() == "1":
                                    print("You explain to him what has been going on...")
                                    #time.sleep()
                                    print("")
                                    print("He seems to understand better than you thought he would...")
                                    #time.sleep()
                                    print("")
                                    print(textwrap.fill("He proceedes to explain to you that the shopkeeper is a nasty man. You should be careful if you follow him...", 100))
                                    #time.sleep()
                                    print("")
                                    print("He steps out of the way, and allows you to go through the door. As you go through the door. He warns you.")
                                    print("")
                                    warning = "Be careful my crispy friend... He's a tricky bastard..."
                                    print(blue)
                                    for c in warning:
                                        sys.stdout.write(c)
                                        sys.stdout.flush()
                                        time.sleep(0.04)
                                    print(e)
                                    print("")
                                    time.sleep(4)
                                    chapterthree()

                                elif "Ben" in chosen_character:
                                    survive = random.randint(0,10)
                                    if survive > 4:
                                        print(textwrap.fill("You try to explain to the man what you are doing, leaving out some vital bits of information.", 100))
                                        #time.sleep()
                                        print("")
                                        print("He doesn't look as though he's buying anything...")
                                        #time.sleep()
                                        print("")
                                        print("He stands up...")
                                        #time.sleep()
                                        print("")
                                        print("Once stood, he towers above you dramatically.")
                                        #time.sleep()
                                        print("")
                                        print("He stretches his arms high into the air.")
                                        #time.sleep()
                                        print("")
                                        print("Suddenly, he smacks the floor, nearly knocking you over...")
                                        #time.sleep()
                                        print("")
                                        print("You seem unharmed for the most part. You stand there unphased.")
                                        print("")
                                        print(textwrap.fill("He proceedes to explain to you that the shopkeeper is a nasty man. You should be careful if you follow him...", 100))
                                        #time.sleep()
                                        print("")
                                        print("He steps out of the way, and allows you to go through the door. As you go through the door. He warns you.")
                                        print("")
                                        warning = "Be careful my crispy friend... He's a tricky bastard..."
                                        print(blue)
                                        for c in warning:
                                            sys.stdout.write(c)
                                            sys.stdout.flush()
                                            time.sleep(0.04)
                                        print(e)
                                        print("")
                                        time.sleep(4)
                                        chapterthree()
                                    else:

                                        print(textwrap.fill("You try to explain to the man what you are doing, leaving out some vital bits of information.", 100))
                                        #time.sleep()
                                        print("")
                                        print("He doesn't look as though he's buying anything...")
                                        #time.sleep()
                                        print("")
                                        print("He stands up...")
                                        #time.sleep()
                                        print("")
                                        print("Once stood, he towers above you dramatically.")
                                        #time.sleep()
                                        print("")
                                        print("He stretches his arms high into the air.")
                                        #time.sleep()
                                        print("")
                                        print("Suddenly, he smacks the floor, knocking you over...")
                                        #time.sleep()
                                        print("As you fall, you knock your head on a rock, you are unconscious.")
                                        #time.sleep()
                                        print("")
                                        print(red + "Retry?" + e)
                                        retry = input("> ")
                                        if retry.lower().strip() in ['n', 'no']:
                                            print("Quit game?")
                                            quitt = input("> ")
                                            if quitt in ['y', 'yes']:
                                                quitgame()
                                            else:
                                                restart()
                                                chaptertwo()
                                        elif retry.lower().strip() in ['y', 'yes']:
                                            restart()
                                            chaptertwo()
                                        else:
                                            print("Please use " + cyb + "<y/n>" + e + ".")
                                else:
                                    print(textwrap.fill("You try to explain to the man what you are doing, leaving out some vital bits of information.", 100))
                                    #time.sleep()
                                    print("")
                                    print("He doesn't look as though he's buying anything...")
                                    #time.sleep()
                                    print("")
                                    print("He stands up...")
                                    #time.sleep()
                                    print("")
                                    print("Once stood, he towers above you dramatically.")
                                    #time.sleep()
                                    print("")
                                    print("He stretches his arms high into the air.")
                                    #time.sleep()
                                    print("")
                                    print("Suddenly, he smacks the floor, knocking you over...")
                                    #time.sleep()
                                    print("")
                                    print("As you fall, you knock your head on a rock, you are unconscious.")
                                    #time.sleep()
                                    print("")
                                    print(red + "Retry?" + e)
                                    retry = input("> ")
                                    if retry.lower().strip() in ['n', 'no']:
                                        print("Quit game?")
                                        quitt = input("> ")
                                        if quitt in ['y', 'yes']:
                                            quitgame()
                                        else:
                                            restart()
                                            chaptertwo()
                                    elif retry.lower().strip() in ['y', 'yes']:
                                        restart()
                                        chaptertwo()
                                    else:
                                        print("Please use " + cyb + "<y/n>" + e + ".")

                            else:
                                print("Use the " + cyb + "<speech>" + e + " command.")
                    else:
                        print("As you walk towards the man slouched on the floor, he starts to speak to you.")
                        slman = textwrap.fill("You don't work here! What do you think you're doi... Oh my, is that a packet of ready salted crisps in your bag? If you let me have them... I'll give up some valuble information.", 100)
                        print(blue)
                        for c in slman: 
                            sys.stdout.write(c)
                            sys.stdout.flush()
                            time.sleep(0.04)
                        print(e)
                        print("")
                        print("Do you give him the packet of ready salted crisps?")
                        givecrisps = input("> ")
                        if givecrisps.lower().strip() in ['y', 'yes']:
                            inventory.remove("a packet of ready salted crisps")
                            print(purple + "You give the man a packet of ready salted crisps." + e)
                            print("")
                            print("In a more sincere voice, he asks you again why you are down here.")
                            print("")
                            print("You explain to him what has been going on...")
                            #time.sleep()
                            print("")
                            print("He seems to understand better than you thought he would...")
                            #time.sleep()
                            print("")
                            print(textwrap.fill("He proceedes to explain to you that the shopkeeper is a nasty man. You should be careful if you follow him...", 100))
                            #time.sleep()
                            print("")
                            print("He steps out of the way, and allows you to go through the door. As you go through the door. He warns you.")
                            print("")
                            warning = "Be careful my crispy friend... He's a tricky bastard..."
                            print(blue)
                            for c in warning:
                                sys.stdout.write(c)
                                sys.stdout.flush()
                                time.sleep(0.04)
                            print(e)
                            print("")
                            time.sleep(10)
                            chapterthree()
                        elif givecrisps.lower().strip() in ['n', 'no']:
                            print("")
                            print(textwrap.fill("You back away slowly from the big man and the door... Perhaps that is your only way out... Perhaps, there is no going back now...", 100))
                elif move.lower().strip() in ['t north', 'travel north']:
                    print(textwrap.fill("As you walk towards the bin with the crisps, the man sitting infront of the door calls you over. He wants you to go over to him. ", 100))
                elif move.lower().strip() in ['t south', 'travel south']:
                    print("The hole you crawled through doesn't look big enough to get back through. It was a tight squeeze.")
                else:
                    print("Please use of of the directional travel commands.")
        else:
            print("Use " + cyb + "<look>" + e + " to continue.")
            print("")

### Battle 1 Options ###
def Lanabattleshopkeeper():
    os.system('clear')
    print("""
        """+ title + """### You are about to have your first battle ###""" + e + """


 * The aim is simple. Get the opponents health to """ + red + """0""" + e + """ before yours reaches it.

 * In each battle, your options will be generated based on your inventory.
                
 * Simply type the option you wish to use. Use the number or the tool as an command. """ + red + """

 * This is the only time this message will appear. """ + e +  """Next time, you won't have the heads up.""" + green + """

            Good luck on your journey.""" + e + """

 -------------------------------------------------------------------------------------------

 If you agree to these terms and wish to proceed, type """ + cyb + "<agree>" + e + """.""")
    print("")

    while True:
        agree = input("> ")
        if agree.lower().strip() in ['y', 'agree']:
            os.system('clear')
            print(b + "### Shopkeeper Battle ###" + e)
            if "a snickers" in inventory:
                while Shopkeeper.health > 0 and Lana.snickersbar > 0 and Lana.health > 0:
                    print("""
    1. Smack
    2. Hit with snickers
                        """)
                    choice = input("\n> ")
                    os.system('clear')
                    if choice.lower().strip() in ['1', 'smack']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with your fist.")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Lana.strength / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Lana.health = Lana.health - (Shopkeeper.strength / Lana.defence)
                                print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Lana.health)) + e + " left.")
                            else:
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print(red + "The Shopkeeper hits you with everything he has." + e)
                            Lana.health = Lana.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Lana.health)) + e + " remaining.")
                    elif choice.lower().strip() in ['2', 'snickers', 'hit with snickers']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with the snickers bar.")
                        print("")
                        print(textwrap.fill(blue + b + "You remember the homeless man telling you that the shopkeeper is allergic to nuts. Perhaps this is a more effective way to deal damage." + e, 100))
                        print("")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Lana.snickers / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Lana.snickersbar = Lana.snickersbar - 1	
                                if Lana.snickersbar > 0:
                                    print("Your snickers bar took some damage. It only has " + red + str(Lana.snickersbar) + e + " use left.")
                                    continue
                                else:
                                    print("Your snickers bar has broken. Fists only.")
                                    inventory.remove("a snickers")
                                    break
                                if Shopkeeper.health > 0:
                                    Lana.health = Lana.health - (Shopkeeper.strength / Lana.defence)
                                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Lana.health)) + e + " left.")
                            else:
                                
                                print("")
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print("The Shopkeeper hits you for full damage")
                            Lana.health = Lana.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Lana.health)) + e + " remaining.")
                    else: 
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print(red + "Please use one of the available options." + e)
            if "a snickers" not in inventory:
                while Shopkeeper.health > 0 and Lana.health > 0:
                    print("""
    1. Smack
                            """)
                    choice = input("\n> ")
                    os.system('clear')
                    if choice.lower().strip() in ['1', 'smack']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with your fist.")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Lana.strength / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Lana.health = Lana.health - (Shopkeeper.strength / Lana.defence)
                                print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Lana.health)) + e + " left.")
                            else:
                                print("")
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print("")
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print("The Shopkeeper hits you for full damage")
                            Lana.health = Lana.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Lana.health)) + e + " remaining.")
        else:
            print("")
            print("You did not agree to the terms. Would you like to back out? This will end the game.")
            chickenout = input("> ")
            if chickenout.lower().strip() in ['y', 'yes']:
                time.sleep(1)
                quitgame()
            else:
                print("Please choose one of the available options " + cyb + "<y/agree>" + e + ".")
                continue

def Danbattleshopkeeper():
    os.system('clear')
    print("""
         """ + title + """### You are about to have your first battle ###""" + e + """


 * The aim is simple. Get the opponents health to """ + red + """0""" + e + """ before yours reaches it.

 * In each battle, your options will be generated based on your inventory.
                
 * Simply type the option you wish to use. Use the number or the tool as an command. """ + red + """

 * This is the only time this message will appear. """ + e +  """Next time, you won't have the heads up.""" + green + """

             Good luck on your journey.""" + e + """

 -------------------------------------------------------------------------------------------

 If you agree to these terms and wish to proceed, type """ + cyb + "<agree>" + e + """.""")
    print("")

    while True:
        agree = input("> ")
        if agree.lower().strip() in ['y', 'agree']:
            os.system('clear')
            print(b + "### Shopkeeper Battle ###" + e)
            if "a snickers" in inventory:
                while Shopkeeper.health > 0 and Dan.snickersbar > 0 and Dan.health > 0:
                    print("""
    1. Smack
    2. Hit with snickers
                        """)
                    choice = input("\n> ")
                    os.system('clear')
                    if choice.lower().strip() in ['1', 'smack']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with your fist.")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Dan.strength / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Dan.health = Dan.health - (Shopkeeper.strength / Dan.defence)
                                print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Dan.health)) + e + " left.")
                            else:
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print(red + "The Shopkeeper hits you with everything he has." + e)
                            Dan.health = Dan.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Dan.health)) + e + " remaining.")
                    elif choice.lower().strip() in ['2', 'snickers', 'hit with snickers']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with the snickers bar.")
                        print("")
                        print(textwrap.fill(blue + b + "You remember the homeless man telling you that the shopkeeper is allergic to nuts. Perhaps this is a more effective way to deal damage." + e, 100))
                        print("")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Dan.snickers / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Dan.snickersbar = Dan.snickersbar - 1	
                                if Dan.snickersbar > 0:
                                    print("Your snickers bar took some damage. It only has " + red + str(Dan.snickersbar) + e + " use left.")
                                    continue
                                else:
                                    print("Your snickers bar has broken. Fists only.")
                                    inventory.remove("a snickers")
                                    break
                                if Shopkeeper.health > 0:
                                    Dan.health = Dan.health - (Shopkeeper.strength / Dan.defence)
                                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Dan.health)) + e + " left.")
                            else:
                                
                                print("")
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print("The Shopkeeper hits you for full damage")
                            Dan.health = Dan.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Dan.health)) + e + " remaining.")
                    else: 
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print(red + "Please use one of the available options." + e)
            if "a snickers" not in inventory:
                while Shopkeeper.health > 0 and Dan.health > 0:
                    print("""
    1. Smack
                            """)
                    choice = input("\n> ")
                    os.system('clear')
                    if choice.lower().strip() in ['1', 'smack']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with your fist.")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Dan.strength / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Dan.health = Dan.health - (Shopkeeper.strength / Dan.defence)
                                print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Dan.health)) + e + " left.")
                            else:
                                print("")
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print("")
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print("The Shopkeeper hits you for full damage")
                            Dan.health = Dan.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Dan.health)) + e + " remaining.")
        else:
            print("")
            print("You did not agree to the terms. Would you like to back out? This will end the game.")
            chickenout = input("> ")
            if chickenout.lower().strip() in ['y', 'yes']:
                time.sleep(1)
                quitgame()
            else:
                print("Please choose one of the available options " + cyb + "<y/agree>" + e + ".")
                continue

def Emilybattleshopkeeper():
    os.system('clear')
    print("""
         """ + title + """### You are about to have your first battle ###""" + e + """


 * The aim is simple. Get the opponents health to """ + red + """0""" + e + """ before yours reaches it.

 * In each battle, your options will be generated based on your inventory.
                
 * Simply type the option you wish to use. Use the number or the tool as an command. """ + red + """

 * This is the only time this message will appear. """ + e +  """Next time, you won't have the heads up.""" + green + """

             Good luck on your journey.""" + e + """

 -------------------------------------------------------------------------------------------

 If you agree to these terms and wish to proceed, type """ + cyb + "<agree>" + e + """.""")
    print("")

    while True:
        agree = input("> ")
        if agree.lower().strip() in ['y', 'agree']:
            os.system('clear')
            print(b + "### Shopkeeper Battle ###" + e)
            if "a snickers" in inventory:
                while Shopkeeper.health > 0 and Emily.snickersbar > 0 and Emily.health > 0:
                    print("""
    1. Smack
    2. Hit with snickers
                        """)
                    choice = input("\n> ")
                    os.system('clear')
                    if choice.lower().strip() in ['1', 'smack']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with your fist.")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Emily.strength / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Emily.health = Emily.health - (Shopkeeper.strength / Emily.defence)
                                print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Emily.health)) + e + " left.")
                            else:
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print(red + "The Shopkeeper hits you with everything he has." + e)
                            Emily.health = Emily.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Emily.health)) + e + " remaining.")
                    elif choice.lower().strip() in ['2', 'snickers', 'hit with snickers']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with the snickers bar.")
                        print("")
                        print(textwrap.fill(blue + b + "You remember the homeless man telling you that the shopkeeper is allergic to nuts. Perhaps this is a more effective way to deal damage." + e, 100))
                        print("")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Emily.snickers / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Emily.snickersbar = Emily.snickersbar - 1	
                                if Emily.snickersbar > 0:
                                    print("Your snickers bar took some damage. It only has " + red + str(Emily.snickersbar) + e + " use left.")
                                    
                                    continue
                                else:
                                    print("Your snickers bar has broken. Fists only.")
                                    inventory.remove("a snickers")
                                    break
                                if Shopkeeper.health > 0:
                                    Emily.health = Emily.health - (Shopkeeper.strength / Emily.defence)
                                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Emily.health)) + e + " left.")
                            else:
                                
                                print("")
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print("The Shopkeeper hits you for full damage")
                            Emily.health = Emily.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Emily.health)) + e + " remaining.")
                    else: 
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print(red + "Please use one of the available options." + e)
            if "a snickers" not in inventory:
                while Shopkeeper.health > 0 and Emily.health > 0:
                    print("""
    1. Smack
                            """)
                    choice = input("\n> ")
                    os.system('clear')
                    if choice.lower().strip() in ['1', 'smack']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with your fist.")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Emily.strength / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Emily.health = Emily.health - (Shopkeeper.strength / Emily.defence)
                                print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Emily.health)) + e + " left.")
                            else:
                                print("")
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print("")
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print("The Shopkeeper hits you for full damage")
                            Emily.health = Emily.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Emily.health)) + e + " remaining.")
        else:
            print("")
            print("You did not agree to the terms. Would you like to back out? This will end the game.")
            chickenout = input("> ")
            if chickenout.lower().strip() in ['y', 'yes']:
                time.sleep(1)
                quitgame()
            else:
                print("Please choose one of the available options " + cyb + "<y/agree>" + e + ".")
                continue

def Benbattleshopkeeper():
    os.system('clear')
    print("""
         """ + title + """### You are about to have your first battle ###""" + e + """


 * The aim is simple. Get the opponents health to """ + red + """0""" + e + """ before yours reaches it.

 * In each battle, your options will be generated based on your inventory.
                
 * Simply type the option you wish to use. Use the number or the tool as an command. """ + red + """

 * This is the only time this message will appear. """ + e +  """Next time, you won't have the heads up.""" + green + """

             Good luck on your journey.""" + e + """

 -------------------------------------------------------------------------------------------

 If you agree to these terms and wish to proceed, type """ + cyb + "<agree>" + e + """.""")
    print("")

    while True:
        agree = input("> ")
        if agree.lower().strip() in ['y', 'agree']:
            os.system('clear')
            print(b + "### Shopkeeper Battle ###" + e)
            if "a snickers" in inventory:
                while Shopkeeper.health > 0 and Ben.snickersbar > 0 and Ben.health > 0:
                    print("""
    1. Smack
    2. Hit with snickers
                        """)
                    choice = input("\n> ")
                    os.system('clear')
                    if choice.lower().strip() in ['1', 'smack']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with your fist.")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Ben.strength / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Ben.health = Ben.health - (Shopkeeper.strength / Ben.defence)
                                print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Ben.health)) + e + " left.")
                            else:
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                                
                        else:
                            print("The shop keeper steps away. You miss.")
                            print(red + "The Shopkeeper hits you with everything he has." + e)
                            Ben.health = Ben.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Ben.health)) + e + " remaining.")
                    elif choice.lower().strip() in ['2', 'snickers', 'hit with snickers']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with the snickers bar.")
                        print("")
                        print(textwrap.fill(blue + b + "You remember the homeless man telling you that the shopkeeper is allergic to nuts. Perhaps this is a more effective way to deal damage." + e, 100))
                        print("")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Ben.snickers / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Ben.snickersbar = Ben.snickersbar - 1	
                                if Ben.snickersbar > 0:
                                    print("Your snickers bar took some damage. It only has " + red + str(Ben.snickersbar) + e + " use left.")
                                    inventory.remove("a snickers")
                                    continue
                                else:
                                    print("Your snickers bar has broken. Fists only.")
                                    inventory.remove("a snickers")
                                    break
                                if Shopkeeper.health > 0:
                                    Ben.health = Ben.health - (Shopkeeper.strength / Ben.defence)
                                    print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Ben.health)) + e + " left.")
                            else:
                                
                                print("")
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)

                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print("The Shopkeeper hits you for full damage")
                            Ben.health = Ben.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Ben.health)) + e + " remaining.")
                    else: 
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print(red + "Please use one of the available options." + e)
            if "a snickers" not in inventory:
                while Shopkeeper.health > 0 and Ben.health > 0:
                    print("""
    1. Smack
                            """)
                    choice = input("\n> ")
                    os.system('clear')
                    if choice.lower().strip() in ['1', 'smack']:
                        print(b + "### Shopkeeper Battle ###" + e)
                        print("")
                        print("You smack the Shopkeeper with your fist.")
                        hitchance = random.randint(0,10)
                        if hitchance > 2:
                            Shopkeeper.health = Shopkeeper.health - (Ben.strength / Shopkeeper.defence)
                            print("You hit the Shopkeeper. Their health is now " + red + str(round(Shopkeeper.health)) + e + ".")
                            if Shopkeeper.health > 0:
                                Ben.health = Ben.health - (Shopkeeper.strength / Ben.defence)
                                print("The Shopkeeper takes a swing. He hits you. You have " + red + str(round(Ben.health)) + e + " left.")
                            else:
                                print("")
                                print("You have defeated the Shopkeeper.")
                                print("It looks like he dropped something.")
                                lootDrop = loot()
                                print("")
                                print(purple + "You pick up a " + lootDrop + "." + e)
                                inventory.append("a " + lootDrop)
                                time.sleep(4)
                                chapteroneending()
                        else:
                            print("The shop keeper steps away. You miss.")
                            print("The Shopkeeper hits you for full damage")
                            Ben.health = Ben.health - Shopkeeper.strength
                            print("You only have " + red + str(round(Ben.health)) + e + " remaining.")
        else:
            print("")
            print("You did not agree to the terms. Would you like to back out? This will end the game.")
            chickenout = input("> ")
            if chickenout.lower().strip() in ['y', 'yes']:
                time.sleep(1)
                quitgame()
            else:
                print("Please choose one of the available options " + cyb + "<y/agree>" + e + ".")
                continue

### Chapter 1 Ending ###
def chapteroneending():
    os.system('clear')
    print(textwrap.fill("You watch the shopkeeper tumble to the ground. You get closer, inspecting his corpse-like body.",100))
    #time.sleep()
    print("")
    print("He moves slightly.")
    print("")
    crawl = "Ha. Ha.. Ha... YOU WISH YOU COULD DEFEAT ME! You'll never be so lucky!"
    print(blue)
    for c in crawl:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    print(e)
    print("")
    print("The shopkeeper leaps to his feet. Almost knocking you over. He darts forwards, stealing the marsbar from you.")
    print("")
    print(purple + "A marsbar has been stolen from your inventory." + e)
    print("")
    inventory.remove("a marsbar")
    print(textwrap.fill("The Shopkeeper drops to the ground, slithering through a vent in the wall.", 100))
    print("")
    print(textwrap.fill("Search his office or follow him through the hole.", 100))
    print("")
    while True:
        follow = input("> ")
        if follow.lower().strip() in ['y', 'yes', 'follow', 'follow shopkeeper','hole']:
            chaptertwo()
        elif follow in ['search', 'look' 'search office']:
                print("")
                print(textwrap.fill("You look around his office. There doesn't seem to be much of interest. Although on the whiteboard there are the letters 'E=V'. It might be some form of maths equation, or it could also be a clue.", 100))
                print("")
                if "E = V" in notepad:
                    print("You have already written this clue down.")
                else:
                    print("Do you wish to write this down?")
                    clue2 = input("> ")
                    if clue2.lower().strip() in ['y', 'yes']:
                        print("")
                        print(purple + "'E = V' has been added to your notepad." + e)
                        notepad.append("E = V")
                    else:
                        print("You ignore the writing, perhaps it isn't of any use...")
        elif follow.lower().strip() == "notepad":
            getnotepad()
        elif follow.lower().strip() == "inventory":
            getinventory()
        elif follow.lower().strip() in ['q', 'quit']:
            print("Are you sure you want to exit?")
            quitt = input("> ")
            if quitt.lower().strip() in ['y', 'yes']:
                quitgame()
            else:
                continue
        else:
            print("Type " + cyb + "<follow>" + e + " to follow the shopkeeper through the hole. Or type " + cyb + "<search> " + e + "to look around his office.")

def chapteroneendingdan():
    #print(textwrap.fill("You successfully manage to convince him that you are not in fact the man he thought you are. You escaped this time...", 100))
    #print("")
    text = textwrap.fill("You make a valid point... I suppose you do look slightly different.", 100)
    text2 = textwrap.fill("However, I am hungry. So, I will be taking that marsbar... Thank you very much.", 100)
    print(blue)
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    #print(e)
    print("")
    print("")
    for c in text2:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    print(e)
    print("")
    print(purple + "The marsbar has been stolen from your inventory!" + e)
    inventory.remove("a marsbar")
    print("")
    print("The shopkeeper drops to the ground. Slithering through a vent in the wall. He's got your marsbar!")
    print("")
    print(textwrap.fill("Do you search his office or follow him through the hole.", 100))
    print("")
    while True:
        follow = input("> ")
        if follow.lower().strip() in ['y', 'yes', 'follow', 'follow shopkeeper','hole', 'go through hole']:
            chaptertwo()
        elif follow in ['search', 'look' 'search office', 'look around office']:
                print("")
                print(textwrap.fill("You look around his office. There doesn't seem to be much of interest. Although on the whiteboard there are the letters 'E=V'. It might be some form of maths equation but it could also be a clue.", 100))
                print("")
                if "E = V" in notepad:
                    print("You have already written this clue down.")
                else:
                    print("Do you wish to write this down?")
                    clue2 = input("> ")
                    if clue2.lower().strip() in ['y', 'yes']:
                        print("")
                        print(purple + "'E = V' has been added to your notepad." + e)
                        notepad.append("E = V")
                    else:
                        print("You ignore the writing, perhaps it isn't of any use...")
        elif follow.lower().strip() == "notepad":
            getnotepad()
        elif follow.lower().strip() == "inventory":
            getinventory()
        elif follow.lower().strip() in ['q', 'quit']:
            print("Are you sure you want to exit?")
            quitt = input("> ")
            if quitt.lower().strip() in ['y', 'yes']:
                quitgame()
            else:
                continue
        else:
            print("Type " + cyb + "<follow>" + e + " to follow the shopkeeper through the hole. Or type " + cyb + "<search> " + e + "to look around his office.")


### Chapter 1 Battle ###
def chapteronebattle():
    os.system('clear')
    print("As you approach the counter, you can't help but think that something seems off...")
    #time.sleep()
    print("The man at the counter is giving you a stern look. He doesn't seem pleased.")
    #time.sleep()
    print(textwrap.fill("As you get to the counter he stops serving the woman in front of you. Has a quiet word with his colleage, and asks you to follow him.", 100))
    #time.sleep()
    print("Surely not... First class service? You wonder to yourself. Maybe this day isn't so bad after all.")
    #time.sleep()
    print("As he approaches you he starts to speak. In a low, assertive voice.")
    #time.sleep()
    say = textwrap.fill("You there. With the muddy arms. Follow me. I need to speak to you.", 100)
    say2 = textwrap.fill("It's brave of you to show your face around here. I promised my wife when I next saw you, I would finish what we started all those years ago.", 100)
    print("")
    print(blue)
    for c in say:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")
    time.sleep(2)
    print("")
    for c in say2:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print(e)
    print("")
    print("You have no idea what he's going on about...")
    print("Perhaps he has mistaken you for someone else.")
    print("")
    time.sleep(2)
    if "Dan" in chosen_character:
        print("Do you try to explain that he's mistaken?")
        ddcharm = input("> ")
        if ddcharm.lower().strip() in ['y', 'yes']:
            getout = random.randint(0,10)
            if getout > 6:
                print("")
                print(textwrap.fill("You try to explain that you aren't who he thinks you are. It hasn't worked. He doesn't believe you.", 100))
                Danbattleshopkeeper()
            else:
                chapteroneendingdan()
        else:
            Danbattleshopkeeper()
    elif "Ben" in chosen_character:
        Benbattleshopkeeper()
    elif "Lana" in chosen_character:
        Lanabattleshopkeeper()
    elif "Emily" in chosen_character:
        Emilybattleshopkeeper()
    else:
        print(red + "Invalid" + e)

### Chapter 1 ###
def chapterone():
    os.system('clear')
    print("""
                             """ + title + """### Chapter One: The Letter ###""" + e + """
    """)
    print("")
    prologue = textwrap.fill("You wake up in your gloomy one bedroom flat in Milton Keynes. Clothes are thrown all over the floor and you can't help but notice the strong odour of rotten food. You really should sort your life out.\n", 100)
    # for c in prologue:
    #     sys.stdout.write(c)
    #     sys.stdout.flush()
    #     time.sleep(0.05)
    print(prologue)
    #time.sleep()
    print("")
    
    print("To examine your surroundings, type " + cyb + "<look>" + e + ".")
    while True:
        lookaround = input("> ")
        if lookaround.lower().strip() == "look":
            print("")
            print(textwrap.fill("You scan the room with your blurry vision. To your right, you have the assortment of old pot noodles, the source of the smell. Your phone is to your left, its screen cracked. In front of you, there is a door. It looks to be unlocked.", 100))
            print("")
            print("To investigate a specific object in your surroundings. Type " + cyb + "<i>" + e + " followed by the object. ")
            while True:
                investigate = input("> ")
                if investigate.lower().strip() in ['i noodles', 'i pot noodle', 'i pot noodles', 'i noodle']:
                    print("")
                    print(textwrap.fill("You are utterly disgusting. The stench is awful and there is fur growing in some of the pots. Tucked behind one of the pots is a small fork. It looks clean. Do you wish to take it?", 100))
                    while True: 
                        takenoodles = input("> ")
                        if takenoodles.lower().strip() in ['y', 'yes']:
                            if "a small fork" in inventory:
                                print("")
                                print(red + "Sorry, you have already taken the fork." + e)
                                break
                            else:
                                inventory.append("a small fork")
                                print("")
                                print(textwrap.fill(purple + "A small fork has been added to your inventory." + e +  " To view your inventory, type " + cyb + "<inventory>" + e + ". This can be used at anytime.", 100))
                                break
                        else: 
                            print("")
                            print("You leave the small fork alone. Perhaps it could have been useful. Then again, perhaps not.")
                            break
                elif investigate.lower().strip() in ['i yourself', 'i self', 'i me', 'i myself']:
                    print("")
                    print(textwrap.fill("You stare down at yourself, there is food on your top, stains on your jeans, and mud on your arms. You wonder how you could have gotten into such a state.", 100))
                elif investigate.lower().strip() == "i phone": 
                    print("")
                    print(textwrap.fill("You glance over at your phone. The cracked screen wasn't there before. How did that happen, you wonder... No wifi connection either, strange. There's a text from Uncle Darren, your landlord. Why does he call himself that? He isn't even your uncle. Regardless, the text reads:", 100)) 
                    print("")
                    print(blue + "Uncle Darren:")
                    print(textwrap.fill("If you want to get back on the internet. You have two options. Decipher the code or go to the shop and bring me back a marsbar. IM HUNGRY. The code for the wifi password is: " + wifi_password +". ", 100))
                    print("" + e)
                    print("Do you want to add this to your notepad?")
                    while True:
                        addwifi = input("> ")
                        if addwifi.lower().strip() in ['y', 'yes']:
                            notepad.append("Wifi = " + wifi_password)
                            print("")
                            print(purple + "A clue has been added to your inventory." + e + " To view, type " + cyb + "<notepad>" + e)
                            break
                        else:
                            print("")
                            print("You should probably make a note of that...")
                            continue
                elif investigate.lower().strip() == "inventory": 
                    getinventory()
                elif investigate.lower().strip() == "notepad":
                    getnotepad() 
                elif investigate.lower().strip() == "i door":
                    if not any(notepad):
                        print("")
                        print("The door looks as though it's open. Perhaps it could be a way out.")
                    elif any(notepad): 
                        while True: 
                            print("")
                            print(textwrap.fill("You glance towards the door. It's open. You have collected everything of value in this room, would you like to exit?", 100))
                            exit = input("> ")
                            if exit.lower().strip() in ['y', 'yes']:
                    
                                os.system('clear')
                                print(textwrap.fill("You leave through the door and head outside.", 100))
                                print(textwrap.fill("You read the text again. A mars bar, that shouldn't be too difficult to get, you think to yourself.", 100))
                                #time.sleep()
                                print("")
                                print("As you step outside into the cold, bright world. The sunlight burns your eyes. Make your way to the shop.")
                                print("")
                                print("To the " + cyb + "<east>" + e + " there doesn't seem to be anything of interest. To the " + cyb + "<west>" + e + " there looks to be a small town.")
                                print("To travel in either direction, use " + cyb + "<t>" + e + " and the direction you would like to go.")
                                while True: 
                                    travel = input("> ")
                                    if travel.lower().strip() in ['t west', 'travel west']:
                                        print("You walk for a while. After some time you think as though you must be getting close to the town. Although it doesn't appear any closer. You start to feel faint. Suddenly, you fall... Landing in the road, you probably won't make it. Sadly, you don't.")
                                        #time.sleep()
                                        print("You have died.")
                                        #time.sleep()
                                        print(red + "Game Over." + e)
                                        print("")
                                        print("Would you like to try again from the current level?")
                                        while True:
                                            tryagain = input("> ")
                                            if tryagain.lower().strip() in ['y', 'yes']:
                                                restart()
                                                chapterone()
                                            elif tryagain.lower().strip() in ['n', 'no']:
                                                quitgame()
                                            else:
                                                print(red + "Please answer with <y/yes> or <n/no>")

                                    elif travel.lower().strip() in ['t east', 'travel east']:
                                        print("")
                                        print(textwrap.fill("You walk for a while. Eventually you reach the shop. Your first mission was a basic one. You passed with flying colours.", 100))
                                        print("")
                                        print("Use the " + cyb + "<look>" + e + " command to look for things of interest.")
                                        while True:
                                            lookshop = input("> ")
                                            if lookshop.lower().strip() == "look":
                                                print("")
                                                print(textwrap.fill("You stand outside the shop and have a look around. To the east you have the shop. To the west there is a homeless man, asking strange questions. To the north there is a fountain, and to the south, is home.", 100))
                                                print("")
                                                print("Use the " + cyb + "<t>" + e + " command again to choose which direction to travel in.")
                                                while True:
                                                    shoptravel = input("> ")
                                                    if shoptravel.lower().strip() in ['t west', 'travel west']:
                                                        if "a small fork" in inventory:
                                                            print("")
                                                            print(textwrap.fill("You walk up to the homeless man. He's talking to himself, speaking in riddles. He is eating something, looks like a pasta based dish. Without cutlery... He clocks you and shouts", 100))
                                                            print("")
                                                            hman = textwrap.fill("HEY! YOU! Over there with the backpack! I don't suppose you have a fork in there I could have do you? This lasagne is burning my fingers...", 100)
                                                            print(blue)
                                                            for c in hman:
                                                                sys.stdout.write(c)
                                                                sys.stdout.flush()
                                                                time.sleep(0.03)
                                                            print(e)
                                                            print("")
                                                            print("")
                                                            print("Do you wish to give him the fork you collected?")
                                                            while "a small fork" in inventory: 
                                                                givefork = input("> ")
                                                                
                                                                if givefork.lower().strip() in ['y', 'yes']: 
                                                                    print("")  
                                                                    print("You give the homeless man your fork.")
                                                                    inventory.remove("a small fork")
                                                                    print("")
                                                                    s = textwrap.fill("Thank you good Sir. I don't know if this information is of any use to you. But I have heard rumors that K becomes P, and the man inside the shop, is allergic to nuts.", 100)
                                                                    print(blue)
                                                                    for c in s:
                                                                        sys.stdout.write(c)
                                                                        sys.stdout.flush()
                                                                        time.sleep(0.03)
                                                                    print(e)
                                                                    print("")
                                                                    print("")
                                                                    print("Although this message is cryptic. You feel as though 'K becomes P' may be of some use.")
                                                                    print("")
                                                                    print("Do you wish to write this down?")
                                                                    while True: 
                                                                        writedown = input("> ")
                                                                        if writedown.lower().strip() in ['y', 'yes']:
                                                                            notepad.append("K becomes P")
                                                                            print("")
                                                                            print(purple + "A clue has been added to your notepad." + e)
                                                                            break
                                                                        else:
                                                                            print("Unless you have a very good memory. It might be worth writing these clues down...")
                                                                            continue
                                                                elif givefork.lower().strip() in ['n', 'no']:
                                                                    print("")
                                                                    print("Confused by the converstaion you have. You slowly back away.")
                                                                    break
                                                                elif givefork.lower().strip() == "notepad":
                                                                    print("")
                                                                    getnotepad()
                                                                    break
                                                                else: 
                                                                    print("")
                                                                    print(red + "Please use the <y/n> commands" + e)
                                                        else:
                                                            print("")
                                                            print("You glance over to the homeless man. He seems to be enjoying his food.")
                                                    elif shoptravel.lower().strip() in ['t east', 'travel east']:
                                                        print("")
                                                        print("Do you wish to go into the shop?")
                                                        while True:
                                                            goin = input("> ")
                                                            if goin.lower().strip() in ['y', 'yes']:
                                                                print("")
                                                                print("You wander into the shop. You know the drill by now. Look around...")
                                                                shop = input("> ")
                                                                if shop.lower().strip() == "look":
                                                                    print("")
                                                                    print(textwrap.fill("You glance around the shop. To the east, there is the shopkeeper and to the west, there is the chocolate aisle. To the north there seems to be some form of café.", 100))
                                                                    print("")
                                                                    print("Which direction would you like to travel in?")
                                                                    while True: 
                                                                        shopdir = input("> ")
                                                                        if shopdir.lower().strip() in ['t east', 'travel east']:
                                                                            chapteronebattle()
                                                                        elif shopdir.lower().strip() in ['t west', 'travel west']:
                                                                            print("")
                                                                            print("You wander down to the chocolate aisle. Do you want to pick up a marsbar?")
                                                                            pickupcho = input("> ")
                                                                            if "a marsbar" not in inventory:
                                                                                if pickupcho.lower().strip() in ['y', 'yes']:
                                                                                    inventory.append("a marsbar")
                                                                                    print("")
                                                                                    print(purple + "A marsbar has been added to your inventory." + e)
                                                                                    print("")
                                                                                    print("That was lucky. It was the last one...")
                                                                                    print("Would you like to pick up anything else?" + cyb + " <y/n>" + e)
                                                                                    pickupmore = input("> ")
                                                                                    if pickupmore.lower().strip() in ['yes', 'y']:
                                                                                        print("")
                                                                                        print("What would you like to pick up?")
                                                                                        while True:
                                                                                            pickup = input("> ")
                                                                                            if pickup.lower().strip() in str(food):
                                                                                                print("")
                                                                                                print(purple + "A " + pickup.lower().strip() + " has been added to your inventory." + e)
                                                                                                inventory.append("a " + pickup.lower().strip())
                                                                                                break
                                                                                            elif pickupcho.lower().strip() == "notepad":
                                                                                                getnotepad()
                                                                                            elif pickupcho.lower().strip() == "inventory":
                                                                                                getinventory()
                                                                                            else:
                                                                                                print("")
                                                                                                print("You can't seem to see any " + pickup.lower().strip() + ". Perhaps they are sold out. Choose something else.")
                                                                                                continue
                                                                                    elif pickupcho.lower().strip() == "notepad":
                                                                                            getnotepad()
                                                                                            continue
                                                                                    elif pickupcho.lower().strip() == "inventory":
                                                                                        getinventory()
                                                                                        continue
                                                                                    elif pickupcho.lower().strip() in ['n', 'no']:
                                                                                        print("Now you have the marsbar, it's time to checkout. Type " + cyb + "<checkout>" + e)
                                                                                    else:
                                                                                        print("")
                                                                                        print("Please use " + cyb + "<y/n>" + e + ".")
                                                                                        continue
                                                                            else:
                                                                                print("You already have the marsbar. Type " + cyb + "<checkout>" + e + ".")
                                                                                
                                                                        elif shopdir.lower().strip() in ['t north', 'travel north']:
                                                                            print("")
                                                                            print("You came here for chocolate... You should probably stick to the plan.")
                                                                        elif shopdir.lower().strip() in ['t south', 'travel south']:
                                                                            print("")
                                                                            print("There isn't much point in going home. You've come this far.")
                                                                        elif shopdir.lower().strip() == "notepad":
                                                                            getnotepad()
                                                                        elif shopdir.lower().strip() == "inventory":
                                                                            getinventory()
                                                                        
                                                                        elif shopdir.lower().strip() == "checkout":
                                                                            print("")
                                                                            chapteronebattle()
                                                                        else:
                                                                            print("")
                                                                            print(textwrap.fill("Please use one of the directions. Type " + cyb + "<t>" + e + " followed by" + cyb + " <north/south/east/west>" + e + " to keep investigating, or type " + cyb + "<checkout>" + e + " to continue.", 100))
                                                                            continue
                                                            elif goin.lower().strip() in ['n', 'no']:
                                                                print("You stay where you are.")
                                                                break
                                                            else:
                                                                print("")
                                                                print("Please use " + cyb + "<yes/no>" + e + ".")
                                                                continue
                                                    elif shoptravel.lower().strip() in ['t north', 'travel north']:
                                                        print("")
                                                        print(textwrap.fill("You glance over towards the fountain. As you wander over to it, you notice a shimmer at the bottom. It seems as though many people have thought to chuck a coin in, perhaps for luck. You're not very superstitious, but it makes you wonder.", 100))
                                                        print("")
                                                        print("Do you want to toss a coin in?")
                                                        while True:
                                                            tosscoin = input("> ")
                                                            if tosscoin.lower().strip() in ['y', 'yes']:
                                                                if fountainluck >= 0:
                                                                    fountainluck + 1
                                                                    print("")
                                                                    print("You toss a coin into the fountain. As it lands, it seems to glow slightly. Strange.")
                                                                    break
                                                            else:
                                                                print("")
                                                                print("You wonder what could have happened if you did toss a coin in. Maybe it's just there for show...")
                                                                break
                                                    elif shoptravel.lower().strip() in ['t south', 'travel south']:
                                                        print("")
                                                        print(textwrap.fill("You look back at the direction you travelled from. Perhaps it isn't too late to return. You wonder to yourself, do you actually need an internet connection?", 100))
                                                        print("")
                                                        print("Do you wish to travel home? Note: This will restart the level.")
                                                        while True: 
                                                            travelhome = input("> ")
                                                            if travelhome.lower().strip() in ['y', 'yes']:
                                                                print("")
                                                                print("You start the long treck back to your home. With no marsbar in hand. The day surely will be a dull one.")
                                                                print("")
                                                                resetgame()
                                                                restart()
                                                            else:
                                                                print("")
                                                                print("It's probably for the best that you stick to the task at hand.")
                                                                break
                                                    elif shoptravel.lower().strip() == "inventory":
                                                        getinventory()
                                                    elif shoptravel.lower().strip() == "notepad":
                                                        getnotepad()
                                                    elif shoptravel.lower().strip() == "help":
                                                        print("")
                                                        print("Your aim is to make it to the shop. Use the " + cyb + "<t>" + e + "command to travel in a direction " + cyb + "<north/south/east/west>" + e + ". Good luck.")
                                                    else:
                                                        print("")
                                                        print(red + "Please use one of the options provided." + e)
        elif lookaround.lower().strip() == "help":
            print("You need to find something useful to interact with in your environment. Try investigating the noodles, mirror, or youself.")
        elif lookaround.lower().strip() == "quit":
            while True: 
                print("Are you sure you would like to quit? Type " + cyb + "<y>" + e + " to confirm or press any key to go back.")
                quitgame1 = input("> ")
                if quitgame1.lower().strip() in ['y', 'yes']:
                    quitgame()
                else:
                    break
        elif lookaround.lower().strip() == "inventory": 
            getinventory()
        elif lookaround.lower().strip() == "notepad":
            getnotepad()

### Character Creation ###
option = None
profiles = {}
points = 20 

def creation():
    os.system('clear')
    while option != "0":
        print("""
        ####################################
        #        Character Creation        #
        
                0  Quit
                1  Start New Adventure

        #      Please choose an option:    #
        ####################################
        """)

        choice = input("> ")
        print()

        ### Choice 0 ###
        if choice == "0":
            os.system('clear')
            print(red + "Quitting Game..." + e)
            time.sleep(2)
            print("Thank you for playing")
            sys.exit()

        ### Choice 1 ###
        
        elif choice == "1": 
            os.system('clear')
            print("""
        ######################################################
        # Which character would you like to know more about? #
        #            Made your choice? Type """ + cyb + "<ready>" + e + """          #

                               1. Dan
                               2. Ben
                               3. Lana
                               4. Emily 

        #               To go back, type """ + cyb + "<back>" + e + """              #
        ######################################################
            """)
            while True:
                character = input("> ")
                if character.title() in ["Dan", "1"]:
                    print(textwrap.fill(green + "\nDan is a prolific writer from the depths of Kent. With his superior knowledge of the English language, charming his way out of sticky situations with the art of conversation is where Dan and his blue eyes, really shine." + e, 100))
                elif character.title() in ["Ben", "2"]:
                    print(textwrap.fill(green + "\nBen, AKA Big Ben. Not to be confused with the London Landmark. Big Ben is 6ft 5' and 15 stone of pure British beef. An amateur body builder, he is sure never to lose a battle." + e, 100))
                elif character.title() in ["Lana", "3"]:
                    print(textwrap.fill(green + "\nLana. Vegan, Pisces, 21. An activist for animal rights. Her life long devotion to the lives of our furry friends, has lead her to develop the animal telepathy. A strange but somewhat useful skill..." + e, 100))
                elif character.title() in ["Emily", "4"]:
                    print(textwrap.fill(green + "\nEmily, firey mathematician, with a burning desire for Ben. Reigning pub quiz champion, she knows anything about everything... Her brain may be perfect, but her eyes certainly aren't. She has the eysight of an elderly mole." + e, 100))
                elif character.title() == "quit":
                    os.system('clear')
                    quitgame()
                elif character.title() in ["Ready", "5"]:
                    print("")
                    print("Type the name of the character you would like to select: ")
                    while True:
                        charselect = input("> ")
                        if charselect.title().strip() not in character_names:
                            print("")
                            print("Sorry, please try again using one of the names provided.")
                            continue
                        elif charselect.title().strip() in character_names:
                            chosen_character.append(charselect.title().strip())
                            # chosen_character = charselect.title().strip()
                            os.system('clear')
                            print("**Voice from above**")
                            #time.sleep()
                            # print("You have chosen to continue your life as " + str(chosen_character) + ".")
                            # print("One final question. What should we call you?")
                            text1 = str("\nYou have chosen to continue your life as " + ''.join(chosen_character) + ".\nOne final question. What should we call you?\n")
                            print(blue)
                            
                            for c in text1: 
                                sys.stdout.write(c)
                                sys.stdout.flush()
                                time.sleep(0.05)
                            print(e)
                            your_name = input("> ")
                            print(blue)
                            player_name.append(your_name.title().strip())
                            text2 = str("Perfect. Now we know to call you " + ','.join(player_name) + ". You can begin your adventure.\n")
                            print("")
                            # pickle.dump(player_name, open("saves.dat", "wb"))
                            for c in text2:
                                sys.stdout.write(c)
                                sys.stdout.flush()
                                time.sleep(0.05)
                            print(e)
                            time.sleep(2)
                            
                            chapterone()

                elif character.title() == "Back":
                    os.system('clear')
                    break           
                else: 
                    print(red + "\nPlease choose one of the available options." + e)
                    continue
        elif choice == "2":
            saves = pickle.load(open("saves.dat", "rb"))
            print(saves)

        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "back":
            introduction()

### Introduction ###
def introduction():
    os.system('clear')
    print(red)
    title2()
    print(e)
    print("""
    ####################################################################
    #        Welcome to Get Online. A text based MUD game designed     #
    #                      as a university project.                    #
    # ---------------------------------------------------------------- #
            Here are some basic commands to get you started.  

        """ + cyb + "<help>" + e +"""       Will give a list of useable commands.
        """ + cyb + "<info>" + e +"""       More about the development of Get Online.
        """ + cyb + "<save>" + e +"""       Save your current progress (can use anywhere)
        """ + cyb + "<y/yes>" + e +"""      Used for y/n questions.
        """ + cyb + "<n/no>" + e +"""       Used for y/n questions.
      ---------------------------------------------------------------- 
                                :  Start  :
                                :  Quit   :      
    #                                                                  #
    ####################################################################

    """)
    while True: 
        startgame = input("> ")
        if startgame.lower() == "help":
            print("Choose one of the options above.")
        elif startgame.lower() == "info":
            print("This game was developed as a university project..............") # Finish this later. TIME IS OF THE ESSENCE. 
        elif startgame.lower() == "start": 
            print("Your adventure is about to begin.")
            #time.sleep(2)
            creation()
        elif startgame.lower() == "quit":
            print("Are you sure you want to exit? " + cyb + "<y/n>" + e + ".")
            quitgametitle = input("> ")
            if quitgametitle.lower() == "y":
                print(red + "Quitting Game..." + e)
                #time.sleep(2)
                print("Thank you for playing")
                sys.exit()
            elif quitgametitle.lower() == "n":
                continue
            else:
                print(red + 'Please choose one of the available options.' + e)
        else:
            print(red + "Please choose one of the available options." + e)


introduction()
