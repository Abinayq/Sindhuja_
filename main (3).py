


class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects for Batsman and Bowler
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()


In this code, we have a base class `Player` with a `play` method that prints a generic message. Then, we have two derived classes, `Batsman` and `Bowler`, each of which overrides the `play` method to print specific messages. Finally, we create objects of both `Batsman` and `Bowler` and call the `play` method for each object, resulting in the appropriate messages being printed for each player type.