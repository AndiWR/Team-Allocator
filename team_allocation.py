
# Team allocator program

# Import the random module to shuffle the player into team
import random

players=["Martin","Craig","Sue",
        "Claire","Dave","Alice",
        "Luciana","Harry","Jack",
        "Rose","Lexi","Maria",
        "Thomas", "James", "William",
        "Ada","Grace","Jean",
        "Marissa","Alan"]

# Welcome message
print("Welcome to Team Allocator!")

while True:

        # Shuffle the player order in the player list so each time the program used it will be different team member
        random.shuffle(players)

        # To assign the first half of the list to team 1
        team1=players[:len(players)//2]

        print("Team 1 Captain: "+random.choice(team1))

        print("Team 1:")
        for player in team1:
                print(player)

        # To assign the last half of the list to team 2
        team2=players[len(players)//2:]

        print("\nTeam 2 Captain: "+random.choice(team2))

        print("Team 2:")
        for player in team2:
                print(player)

        response=input("Pick teams again? Type y or n:")
        if response== "n":
                break