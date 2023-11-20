import math
NumOfEggs = int(input("How many eggs would you like to order? "))
Dozen = round(NumOfEggs / 12, 1)
LooseEggs = int(Dozen % 1 // 0.1)
LEggsValue = round(LooseEggs * .45)
RoundedDozen = round(Dozen, 0) 
TotalValue = round(RoundedDozen*3.25 + LEggsValue, 2)
print("You ordered", NumOfEggs,".", "That's", Dozen, "per dozen and", LooseEggs, "loose eggs at 45c each for a total of R", TotalValue)

