class Player:
    """Class has team color and points"""
    teamcolor = ""
    points = 0

    def printPlayer(self):
        print("The",self.teamcolor,"contender has",self.points,"points!")

def main():
    playerOne = Player()
    playerOne.points = 300
    playerOne.teamcolor = "Blue"
    playerOne.printPlayer()

if __name__ == "__main__":
    main()
