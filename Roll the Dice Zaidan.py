import random

def main():
  value()

def value():
  min = 1
  max = 6
  rolldice(min, max)

def rolldice(min, max):
  roll_again = "yes"

  while roll_again == "yes" or roll_again == "y":
      print ("Rolling the dices...")
      print ("The values are....")
      print (random.randint(min, max))
      print (random.randint(min, max))

      roll_again = input("Roll the dices again?")

main()