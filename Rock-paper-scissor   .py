import random
import time 

while True:

  #Player's choice or weapon
  player_choice = input("What do u choose?:-").strip().lower()

  #Options for AI to choose from
  options = ["rock", "paper", "scissor"]

  #Code for random choice
  computer = random.choice(options)
  
#What would be seen on screen 
  time.sleep(2)
  print(f"\nAI chooses - {computer}")

#differenr senarios-
  if player_choice == computer:
    print("\nIts a tie.")

    time.sleep(1)
    #retry option
    retry = input ("\ntry again? y/n:- ")
    
    if retry!= "y":
      break

  elif ((player_choice =="rock" and computer=="scissor") or (player_choice=="paper" and computer=="rock") or (player_choice=="scissor" and computer=="paper")):
    print("\nYou won!!!")

    time.sleep(1)
    #retry option
    retry= input("\nPlay again??? y/n:-")
    
    if retry!= "y" or "Y":
      break

  else:
    print("\nYou lost")

    time.sleep(1)
    
    #Retry option
    retry= input("\nTry again? y/n:- ")
    if retry != "y":
      break