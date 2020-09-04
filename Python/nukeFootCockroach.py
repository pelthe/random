# -*- coding: cp1252 -*-
import random

playerScore = 0
compScore = 0
rounds = 0
ties = 0

while True:
    playerCh = input("Foot,  Nuke or Cockroach? (Quit ends): ")
    compCh = random.randint(1,4)
    if playerCh == "Quit":
        break

    elif playerCh == "Foot" and compCh == 1:
        print("You chose:",playerCh)
        print("Computer chose: Foot")
        print("It is a tie!")
        ties += 1
        rounds += 1
    
    elif playerCh == "Foot" and compCh == 2:
        print("You chose:",playerCh)
        print("Computer chose: Nuke")
        print("You LOSE!")
        compScore += 1
        rounds += 1

    elif playerCh == "Foot" and compCh == 3:
        print("You chose:",playerCh)
        print("Computer chose: Cockroach")
        print("You WIN!")
        playerScore += 1
        rounds += 1
        
    elif playerCh == "Nuke" and compCh == 1:
        print("You chose:",playerCh)
        print("Computer chose: Foot")
        print("You WIN!")
        playerScore += 1
        rounds += 1

    elif playerCh == "Nuke" and compCh == 2:
        print("You chose:",playerCh)
        print("Computer chose: Nuke")
        print("Both LOSE!")
        rounds += 1

    elif playerCh == "Nuke" and compCh == 3:
        print("You chose:",playerCh)
        print("Computer chose: Cockroach")
        print("You LOSE!")
        compScore += 1
        rounds += 1

    elif playerCh == "Cockroach" and compCh == 1:
        print("You chose:",playerCh)
        print("Computer chose: Foot")
        print("You LOSE!")
        compScore += 1
        rounds += 1

    elif playerCh == "Cockroach" and compCh == 2:
        print("You chose:",playerCh)
        print("Computer chose: Nuke")
        print("You WIN!")
        playerScore += 1
        rounds += 1

    elif playerCh == "Cockroach" and compCh == 3:
        print("You chose:",playerCh)
        print("Computer chose: Cockroach")
        print("It is a tie!")
        ties += 1
        rounds += 1

    else:
        print("Incorrect selection.")

print("You played",rounds,"rounds, and won",playerScore,"rounds, playing tie in",ties,"rounds.")
        
