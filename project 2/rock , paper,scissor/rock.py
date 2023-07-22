
import emoji
import random

a = emoji.emojize(":grinning_face_with_big_eyes:")
b = emoji.emojize(":smiling_face_with_sunglasses:")
c = emoji.emojize(":victory_hand:")

dic = {
    "rock": a,
    "paper": b,
    "scissor": c
}

player = input("ENTER THE PLAYER CHOICE(player1/player2)?")
player1_wins = 0
player2_wins = 0

if player == "player1":
    player1_choice = input("player1, please enter your choice(rock/paper/scissor):")
    player1 = dic[player1_choice]
    player2_choice = random.choice(["rock","paper","scissor"])
    player2 = dic[player2_choice]
    print("player2 chose:" , player2_choice)
    
    if player1_choice == "rock" and player2_choice == "paper":
        player2_wins+=1
    elif player1_choice == "paper" and player2_choice== "rock":
        player1_wins+=1
    elif player1_choice == "scissor" and player2_choice == "rock":
        player2_wins+=1
    elif player1_choice == "paper" and player2_choice == "scissor":
        player2_wins+=1
    elif player1_choice == "rock" and player2_choice == "scissor":
        player1_wins+=1
    elif player1_choice == "scissor" and player2_choice == "paper":
        player1_wins+=1

elif player == "player2":
    player2_choice = input("player2, please enter your choice(rock/paper/scissor):")
    player2 = dic[player2_choice]
    player1_choice = random.choice(["rock","paper","scissor"])
    player1 = dic[player1_choice]
    print("player1 chose:" , player1_choice)
    
    if player2_choice == "rock" and player1_choice == "paper":
        player1_wins+=1
    elif player2_choice == "paper" and player1_choice== "rock":
        player2_wins+=1
    elif player2_choice == "scissor" and player1_choice == "rock":
        player1_wins+=1
    elif player2_choice == "paper" and player1_choice == "scissor":
        player1_wins+=1
    elif player2_choice == "rock" and player1_choice == "scissor":
        player2_wins+=1
    elif player2_choice == "scissor" and player1_choice == "paper":
        player2_wins+=1
               

        
    if player1_wins > player2_wins:
        print("player1, Won!!!", player1)
    elif player2_wins > player1_wins:
        print("player2, Won!!!", player2)
    else:
        print("TIE")





