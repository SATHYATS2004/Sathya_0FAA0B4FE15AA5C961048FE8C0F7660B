'''Implement a class called player that represents a cricket player. The player class should have a 
method called play() which prints "The player is playing cricket. Derive two classes batsman and "
Bowler, from the player class. Override the play() method in each derived class to print "The batsmen 
is batting" and "The bowler is bowling", respectively. write a program to create object of both the 
Batsmen and bowler classes and call the play() method for each  object'''


# Define the base class Player 
class Player:
    def play(self):
        print("The player is playing cricket.")
  
# Define the derived class Batsman 
class Batsman(Player):
  def play(self):
      print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")

# create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call one play() method for each object
batsman.play()
bowler.play()
