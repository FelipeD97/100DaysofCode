import random

rock = """
    ________
---'   _____)
      (_____)
      (_____)
      (____)  
---.__(___)
"""

paper = """
    ______
---'   ____)____
          ______)
         ________)
         _______)  
---.__________)
"""

scissors = """
    ______
---'   ____)____
          ______)
       __________)
      (____)  
---.__(___)
"""

player = '''
           88                                               
            88                                               
            88                                               
8b,dPPYba,  88 ,adPPYYba, 8b       d8  ,adPPYba, 8b,dPPYba,  
88P'    "8a 88 ""     `Y8 `8b     d8' a8P_____88 88P'   "Y8  
88       d8 88 ,adPPPPP88  `8b   d8'  8PP""""""" 88          
88b,   ,a8" 88 88,    ,88   `8b,d8'   "8b,   ,aa 88          
88`YbbdP"'  88 `"8bbdP"Y8     Y88'     `"Ybbd8"' 88          
88                            d8'                            
88                           d8'                           
'''
computer = """
                                             888                   
                                             888                   
                                             888                   
 .d8888b .d88b. 88888b.d88b. 88888b. 888  888888888 .d88b. 888d888 
d88P"   d88""88b888 "888 "88b888 "88b888  888888   d8P  Y8b888P"   
888     888  888888  888  888888  888888  888888   88888888888     
Y88b.   Y88..88P888  888  888888 d88PY88b 888Y88b. Y8b.    888     
 "Y8888P "Y88P" 888  888  88888888P"  "Y88888 "Y888 "Y8888 888     
                             888                                   
                             888                                   
                             888                  
"""


print(
    """
                       888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888                 ,   

88888b.  8888b. 88888b.  .d88b. 888d888 
888 "88b    "88b888 "88bd8P  Y8b888P"   
888  888.d888888888  88888888888888     
888 d88P888  888888 d88PY8b.    888     
88888P" "Y88888888888P"  "Y8888 888     
888             888                     
888             888                             ,
888             888      
                                                                                              
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 

                                                   

"""
)

weapons = ["Rock", "Paper", "Scissors"]

p1 = input('Please choose a weapon: "Rock", "Paper", or "Scissors"?\n')
p1_move = p1.capitalize()

comp_move = weapons[random.randint(0, 2)]

if p1_move == "Rock":
    print(player + "\n" + rock)
    if comp_move == "Rock":
        print(computer + "\n" + rock)
        print(" ")
        print("It's a draw!")
    elif comp_move == "Paper":
        print(computer + "\n" + paper)
        print(" ")
        print("Paper covers rock. The computer wins!")
    elif comp_move == "Scissors":
        print(computer + "\n" + scissors)
        print(" ")
        print("Rock breaks Scissors. You win!")

elif p1_move == "Paper":
    print(player + "\n" + paper)
    if comp_move == "Rock":
        print(computer + "\n" + rock)
        print(" ")
        print("Paper covers rock. You win!")
    elif comp_move == "Paper":
        print(computer + "\n" + paper)
        print(" ")
        print("It's a draw!")
    elif comp_move == "Scissors":
        print(computer + "\n" + scissors)
        print(" ")
        print("Scissors cut Paper. The computer wins!")

elif p1_move == "Scissors":
    print(player + "\n" + scissors)
    if comp_move == "Rock":
        print(computer + "\n" + rock)
        print(" ")
        print("Rock breaks Scissors. The computer wins!")
    elif comp_move == "Paper":
        print(computer + "\n" + paper)
        print(" ")
        print("Scissors cut Paper. You win!")
    elif comp_move == "Scissors":
        print(computer + "\n" + scissors)
        print(" ")
        print("Its a draw!")
else:
    print("Not a valid weapon! Try again!")
