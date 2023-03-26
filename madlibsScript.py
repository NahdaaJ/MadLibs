## MADLIBS PROJECT
# Author: Nahdaa Jawed
# Date Started: 25/03/2023 23:45
# Date Finished: -
# Description:

def madLibs():
    print("\nWhich story line would you like to use? (A/B/C)\nA)The Witch\nB)The Dragon\nC)About You")
    storyChoice = input()
    if storyChoice == "A":
        print("\nYou have chosen 'The Witch'! Please enter the following:\n")
        colour = input("Your favourite colour: ")
        adj2 = input("Adjective: ")
        adj3 = input("Adjective: ")
        verb1 = input("Action Verb: ")
        animal = input("Your favourite animal: ")
        adj4 = input("Adjective: ")
        adj5 = input("Adjective: ")
        adj6 = input("Adjective: ")

        print(
            "\nThe Witch\nThere was once a " + colour + " cottage deep in a " + adj2 + " forest. \nIt was home to a " + adj3 + " witch who loved to " + verb1 + ".\n"
            "She was loved by all the animals in the forest, especially the " + animal + ".\n"
            "However, the residents of the " + adj4 + " village nearby hated her because she was " + adj5 + ", \nbut she did not care, and sipped her " + adj6 + " tea "
            "peacefully on her porch everyday. :)\nThe End!")

        print("\nPlay again? (Y/N)")
        playAgain = input()
        if playAgain == "Y":
            madLibs()
        else:
            print("Goodbye! Thanks for playing!")
            return



    elif storyChoice == "B":
        print("\nYou have chosen 'The Dragon'! Please enter the following: ")
        adj1 = input("\nAdjective: ")
        adj2 = input("Adjective: ")
        adj3 = input("Adjective: ")
        adj4 = input("Adjective: ")
        adj5 = input("Adjective: ")
        adj6 = input("Adjective: ")

        print(
            "\nThe Dragon\nIt was a " + adj1 + " day. The " + adj2 + " dragon was having her morning tea with the princess, \nwhen she heard a " + adj3 + " knight call up the stone tower saying "
            "'" + adj4 + " dragon! \nToday I will slay you, save the " + adj5 + " princess and then marry her!' "
            "\nThe dragon and princess exchanged glances, laughed, and continue to enjoy their " + adj6 + " tea party. :)\nThe End!")

        print("\nPlay again? (Y/N)")
        playAgain = input()
        if playAgain == "Y":
            madLibs()
        else:
            print("Goodbye! Thanks for playing!")
            return

    elif storyChoice == "C":
        print("You have chosen 'About You'! Please enter the following:\n")
        playerName = input("\nYour name: ")
        favColour = input("Your favourite colour: ")
        hatedColour = input("Your least liked colour: ")
        actionVerb = input("Action verb: ")
        someImportant = input("The name of someone important to you: ")
        celebName = input("Name of a celebrity: ")
        favFood = input("Your favourite food: ")

        print("\nAbout Me\nHello! My name is "+playerName+". \nMy hair is "+favColour+" and my eyes are "+hatedColour+"."
              "\nI absolutely love to "+actionVerb+"!. I have a cat called "+someImportant+
              " but it hates my best friend, "+celebName+". \nTo keep clean, i rub "+favFood+" all over before bed every night!")

        print("\nPlay again? (Y/N)")
        playAgain = input()
        if playAgain == "Y":
            madLibs()
        else:
            print("Goodbye! Thanks for playing!")
            return

    else:
        print("Oh, you didn't pick a story! Guess you don't want to play :(\nGoodbye!")
        return


madLibs()