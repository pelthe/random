# -*- coding: cp1252 -*-
import random

while True:
    playerScore = 0
    compScore = 0
    playerCh = int(input(print("Foot,  Nuke or Cockroach (Quit ends): ")))
    compCh = random.randint(1,4)
        if playerCh < compCh:
            print("You LOSE!")
            compScore += 1

        elif playerCh > compCh:
            print("You WIN!")
            playerScore += 1

        elif playerCh == compCh && playerCh == 3:
            print("Both LOSE!")
            playerScore -= 1
            compScore -= 1

        
