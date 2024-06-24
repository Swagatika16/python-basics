import random

print("")
playerchoice = input("Enter...\n1 for Rock ,\n2 for paper, \n3 for scissor-")
player = int (playerchoice)
if player< 1 |   player > 3:
    print(playerchoice+"invalid choice")  
computerchoice = random.choice("123")
 
computer = int(computerchoice)
 
print("")  
print("Your choice" + playerchoice)  
print("Computer choice" + computerchoice)
print("")

if player ==1 and  computer == 3 :
    print("You win")
if player ==2 and  computer == 1 : 
    print("Computer win")   
elif player ==  computer:
    print("Tie game !!")    
elif player ==3 and computer ==2 :
    print("you win ")     
else :
    print("Computer win")       