# imports
import time 


# initialization of the Dungeon Masters
# global variables
exitGame = False
roomColour = "Blue"

# functions
def introScene():
    print("You are in a dark room.")
    time.sleep(0.5)
    print("There is a door to your left and right, which one do you take? (l or r)")
    time.sleep(0.5)
    choice = input()
    time.sleep(0.5)
    if choice == "l":
        gold_room()+
    elif choice == "r":
        print("You walk into a room with a hungry lion. It eats you. Good job!")
    else:
        print("You are stuck in the room forever. Game over!")
        global exitGame
        exitGame = True



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


def gold_room():
        print("You suddenly open your eyes and look around you, the room is filled with gleaming gold and dazzling jewels. What will you do?")
        time.sleep(0.5)
        print("Option (1) - You grab anything you can hold and run out the door in the back")
        time.sleep(0.5)
        print("Option (2) - You take your time finding the gems that would sell for the most and then leave through the gateway at the back")
        time.sleep(0.5)
        print("Option (3) - You leave the gold as it is and run out the exit at the back")
        treasure_option = input()
        if treasure_option == "1":
            print("You successfully escape")
            monster_room()
        elif treasure_option == "2":
            print("You search through the fortune and find a gleaming a ring, different from all the others. You put it on and quietly slip out out the back door.")


def monster_room():

        
        

