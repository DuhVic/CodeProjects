import multiprocessing
import random
import math
def play_game():
  print("Let's play a multiplication game!")

def numbers(): 
 number1 = random.randint(1, 11)
number2 = random.randint(1, 11)
number3 = random.randrange(1, 11) 

   
def answers():
 Score = 0
 print("What is the product of", number2, "and", number3, "?")
 product = int(number2 * number3)
 ask = eval(input("What is the product? "))
 if product == ask :
    Score += 1
    print("Correct! Your score is", Score)

def play_again():
 redo = input("Do you want to play again? (y/n) ")
 while True:
  if redo == "n":
   break
  

play_game()

numbers()

answers()

play_again()



 





