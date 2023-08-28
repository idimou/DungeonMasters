# imports
import time 
import os



# initialization of the Dungeon Masters
# global variables
exitGame = False
roomColour = "Blue"
statPoints = 0

# classes
class player_template:
    type = "Undefined"
    health = 100
    mana = 100
    strength = 1
    dexterity = 1
    intelligence = 3
    charisma = 1
    agility = 1
    faith = 0

    def __init__(self, player1wantsToBe):
        if player1wantsToBe== "MAGE":
            self.type = "Mage"
            self.health = 100
            self.mana = 100
            self.strength = 3
            self.dexterity = 4
            self.intelligence = 18
            self.charisma = 8
            self.agility = 4
            self.faith = 12
        elif player1wantsToBe == "WARRIOR":
            self.type = "Warrior"
            self.health = 100
            self.mana = 100
            self.strength = 18
            self.dexterity = 8
            self.intelligence = 3
            self.charisma = 6
            self.agility = 6
            self.faith = 10
        elif player1wantsToBe == "ROGUE":
            self.type = "Rogue"
            self.health = 100
            self.mana = 100
            self.strength = 5
            self.dexterity = 18
            self.intelligence = 4
            self.charisma = 4
            self.agility = 10
            self.faith = 8
        else:
            print("Creating default player.")

    def printPlayerStats(self):
        print("--------------------------")
        print("Player Stats: ")
        print("Type = " + self.type)
        print("Health = " + str(self.health))
        print("Mana = " + str(self.mana))
        print("Strength = " + str(self.strength))
        print("Dexterity = " + str(self.dexterity))
        print("Intelligence = " + str(self.intelligence))
        print("Charisma = " + str(self.charisma))
        print("Agility = " + str(self.agility))
        print("Faith = " + str(self.faith))
        print("--------------------------")
   
    def awardStatPoints(self, statPoints):
        print("You have been awarded some stat points")
        statPoints = statPoints + 3

    def statIncrease(self, statPoints):
        pickAttribute = input("Which attribute would you like to increase? (strength, dexterity, intelligence, charisma, agility, faith)").upper()
        if pickAttribute == ("STRENGTH"):
            self.strength = self.strength + statPoints
        elif pickAttribute == ("DEXTERITY"):
            self.dexterity = self.dexterity + statPoints
        elif pickAttribute == ("INTELLIGENCE"):
            self.intelligence = self.intelligence + statPoints
        elif pickAttribute == ("CHARISMA"):
            self.charisma = self.charisma + statPoints
        elif pickAttribute == ("AGILITY"):
            self.agility = self.agility + statPoints
        elif pickAttribute == ("FAITH"):
            self.faith = self.faith + statPoints
        else:
            print("You have not chosen a valid attribute")
            self.statIncrease(statPoints)

    
            
player1wantsToBe = input("Mage, Warrior or Rogue?").upper()
print(player1wantsToBe)
player1 = player_template(player1wantsToBe)


# functions
def CheckIfPlayerWantToPlayAgain():
    if exitGame == True:
        print("Do you want to play again? (y or n)")
        playAgain = input()
        if playAgain == "y":
            exitGame = False
        elif playAgain == "n":
            exitGame = True
        else:
            print("I don't understand that, please try again.")
            CheckIfPlayerWantToPlayAgain()

def introScene():
    os.system('cls')
    player1.printPlayerStats()
    time.sleep(5)
    print("You are in a dark room.")
    time.sleep(0.5)
    print("There is a door to your left and right, which one do you take? (l or r)")
    time.sleep(0.5)
    choice = input()
    time.sleep(0.5)
    if choice == "l":
        gold_room()
    elif choice == "r":
        print("You walk into a room with a hungry lion. It eats you. Good job!")
    else:
        print("You are stuck in the room forever. Game over!")
        global exitGame
        exitGame = True
        checkIfPlayerWantToPlayAgain()

def gold_room():
        os.system('cls')
        player1.printPlayerStats()

        print("You suddenly open your eyes and look around you, the room is filled with gleaming gold and dazzling jewels. What will you do?")
        time.sleep(0.5)
        print("Option (1) - You grab anything you can hold and run out the door in the back")
        time.sleep(0.5)
        print("Option (2) - You take your time finding the gems that would sell for the most and then leave through the gateway at the back")
        time.sleep(0.5)
        print("Option (3) - You leave the gold as it is and run out the exit at the back")
        treasure_option = input()
        if treasure_option == "1" and player1.strength> 4 :
            print("You successfully escape")
            player1.awardStatPoints(statPoints)
            monster_room()
        elif treasure_option == "1" and player1.strength< 4 :
            print("You try to escape but the gold is too heavy. You fall down and hit your head on a purple gemstone. You never wake up, Good job!")
            exitGame = True
        elif treasure_option == "2" and player1.agility> 5 :
            print("You search through the fortune and find a gleaming ring, different from all the others. You put it on and quietly slip out out the back door.")    
            player1.awardStatPoints(statPoints)
            monster_room()
        elif treasure_option == "2" and player1.agility< 5 :
            print("You slip and fall on the gold, your head making a terrifying crunch as it hits a pile of gold. You die of a skull fracture that pierced your brain, Good job!")
            exitGame = True
        elif treasure_option == "3" :
            print ("You successfully escape")
            player1.awardStatPoints(statPoints)            
            monster_room()





def monster_room():
    os.system('cls')
    print(statPoints)
    player1.printPlayerStats()
    player1.statIncrease(statPoints)
    player1.printPlayerStats()
    print("You enter a room with a monster. The monster is sleeping. Behind the monster is another door. What would you do? (1 , 2 or 3)")
    time.sleep(0.5)
    print("Option (1) - You sneak past the monster")
    time.sleep(0.5)
    print("Option (2) - You kill the monster and show your dominance")
    time.sleep(0.5)
    print("Option (3) - You try to distract the monster")
    monster_option = input()
    if monster_option == "1":
        print("You successfully escape")
    elif monster_option == "2":
        print("The monster wakes up and eats you. Good job!")
    elif monster_option == "3":
        print("You successfully escape")
    else:
        print("You are stuck in the room forever. Game over!")
        global exitGame
        exitGame = True
        checkIfPlayerWantToPlayAgain()

# game loop
while exitGame == False :
    print("Welcome to the Dungeon Masters game!")
    time.sleep(0.5)
    print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
    time.sleep(0.5)
    print("However, during your exploration, you find yourself lost.")
    time.sleep(0.5)
    print("You can choose to walk in multiple directions to find a way out.")
    time.sleep(0.5)
    print("Let's start with your name: ")
    time.sleep(0.5)
    name = input()
    time.sleep(0.5)
    print("Good luck, " +name+ ".")
    introScene()


