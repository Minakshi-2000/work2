import random
# snake water Gun or Rock Paper Scissors
def gameWin(computer,you):
    # if two vallues are equal, declear a tie!
    if computer == you:  # dono same chiz chala to tie ho jyega none
        return None
    
    #check for all possibilities when computer chose s
    elif computer == 's':
        if you =='w':
            return False
        elif you =='g':
            return True
        #check for all possibilities when computer chose w
    elif computer == 'w':
        if you =='g':
            return False
        elif you == 's':
            return True
       #check for all possibilities when computer chose g 

    elif computer == 'g':
        if you == 's' :
            return False
        elif you =='w' :
            return True   

print ("computer Turn: snake(s) water (w)or gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 3:
    computer = 'g'        
you= input("your Turn: snake(s) water (w)or gun(g)?")



a =gameWin(computer,you)


print(f"computer chose {computer}")
print(f"you  chose {you}")
  # ye game btsyega ki kn jita or kn hara.
if a== None:
    print("the game is a tie!")
elif a:
    print("you win!")  
else:
    print("you lose!")      
