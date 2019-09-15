## Battleships ##
import time
import os

def grid1():
    """creating the arrays for the first grid"""
    grid_arr1.append(["",1,2,3,4,5,6,7,8,9,10])
    for i in range(10):
        grid_arr1.append([chr(65+i)])
        for j in range(1,11):
            grid_arr1[i+1].append(j)

def grid2():
    """creating the arrays for the second grid"""
    grid_arr2.append(["",1,2,3,4,5,6,7,8,9,10])
    for i in range(10):
        grid_arr2.append([chr(65+i)])
        for j in range(1,11):
            grid_arr2[i+1].append(j)


def grid_print1():
    """printing grid 1"""
    os.system('cls')
    print()
    print("#### GRID 1 ####")
    print()
    for j in range(11):                 #array in array
        for i in range(11):             #outer array
            if j == 0 and i == 0:       #so that "A" is in the right place
                print(grid_arr1[i][j],end = "    ")
                continue
            elif j == 10 and i==0:
                print(grid_arr1[i][j],end = "  ")    #10 offsets the alignment so accounting for that      
            elif i != 0 and type(grid_arr1[i][j]) == int:
                print(" ",end = "   ")              #all elements not on the border
            else:
                print(grid_arr1[i][j],end = "   ")
        print()
        
def grid_print2():
    """printing grid 2"""
    os.system('cls')
    print()
    print("#### GRID 2 ####")
    print()    
    for j in range(11):                 #array in array
        for i in range(11):             #outer array
            if j == 0 and i == 0:       #so that "A" is in the right place
                print(grid_arr2[i][j],end = "    ")
                continue
            elif j == 10 and i==0:
                print(grid_arr2[i][j],end = "  ")    #10 offsets the alignment so accounting for that      
            elif i != 0 and type(grid_arr2[i][j]) == int:
                print(" ",end = "   ")              #all elements not on the border
            else:
                print(grid_arr2[i][j],end = "   ")
        print()



def ship_position1(length):
    """selecting positions for the ships"""
    print()
    print("Ship length",length)
    ship_arr = []
    k = 0
    while k!= length:
        col = input("Pick column: ")
        row = eval(input("Pick row: "))
        for i in range(11):
            if grid_arr1[i][0] == col:
                del grid_arr1[i][row]
                grid_arr1[i].insert(row,"+")
                #print(grid_arr)
                grid_print1()
                
        k += 1
    

def ship_position2(length):
    """selecting positions for the ships"""
    print()
    print("Ship length",length)    
    ship_arr = []
    k = 0
    while k!= length:
        col = input("Pick column: ")
        row = eval(input("Pick row: "))
        for i in range(11):
            if grid_arr2[i][0] == col:
                del grid_arr2[i][row]
                grid_arr2[i].insert(row,"+")
                grid_print2()
                
        k += 1

        
def user_choice1():
    col = input("Choose column to shoot: ")
    row = eval(input("Choose row to shoot: "))
    for i in range(11):
        if grid_arr2[i][0] == col:
            if grid_arr2[i][row] == "+":
                print("\nHIT!!")                     
                del grid_arr2[i][row]
                grid_arr2[i].insert(row,"#")
                if grid_arr1[i][row] == "+":
                    del grid_arr1[i][row]
                    grid_arr1[i].insert(row,"*")
                    grid_print1()
                    time.sleep(3)
                    del grid_arr1[i][row]
                    grid_arr1[i].insert(row,"+")
                else:    
                    del grid_arr1[i][row]
                    grid_arr1[i].insert(row,"*")                
            else:
                print("\nMISS...")
                if grid_arr1[i][row] == "+":
                    del grid_arr1[i][row]
                    grid_arr1[i].insert(row,"-")
                    grid_print1()
                    time.sleep(3)
                    del grid_arr1[i][row]
                    grid_arr1[i].insert(row,"+")               
                else:
                    del grid_arr1[i][row]
                    grid_arr1[i].insert(row,"-") 
    grid_print1()
 
 
def user_choice2():
    col = input("Choose column to shoot: ")
    row = eval(input("Choose row to shoot: "))
    for i in range(11):
        if grid_arr1[i][0] == col:
            if grid_arr1[i][row] == "+":
                print("\nHIT!!")                     
                del grid_arr1[i][row]
                grid_arr1[i].insert(row,"#")
                if grid_arr2[i][row] == "+":
                    del grid_arr2[i][row]
                    grid_arr2[i].insert(row,"*")
                    grid_print2()
                    time.sleep(3)
                    del grid_arr2[i][row]
                    grid_arr2[i].insert(row,"+")
                else:    
                    del grid_arr2[i][row]
                    grid_arr2[i].insert(row,"*")                
            else:
                print("\nMISS...")
                if grid_arr2[i][row] == "+":
                    del grid_arr2[i][row]
                    grid_arr2[i].insert(row,"-")
                    grid_print2()
                    time.sleep(3)
                    del grid_arr2[i][row]
                    grid_arr2[i].insert(row,"+")               
                else:
                    del grid_arr2[i][row]
                    grid_arr2[i].insert(row,"-") 
    grid_print2()               
 
     



def main():
    os.system('cls')
    decider1 = 0
    decider2 = 0
    print("Welcome to BATTLESHIPS")
    time.sleep(3)
    player1 = input("Player 1: ")
    player1.upper()
    player2 = input("Player 2: ")
    player2.upper()
    choice = input("New Game?(y/n)\n")
    os.system('cls')
    if choice == "y":
        print(player1,"vs", player2)
        time.sleep(3)
        os.system('cls')
        print("--",player1,"--")
        input("Press Enter")
        grid1()
        grid_print1()
        ship_position1(2)
        #ship_position1(5)      #Uncomment to add more ships
        #ship_position1(4)
        print()
        input("Press enter for next player:")
        os.system('cls')
        print()
        print("--",player2,"--")
        input("Press Enter")
        grid2()
        grid_print2()        
        ship_position2(2)
        #ship_position2(5)
        #ship_position2(4)        
        while ("+" in grid_arr2[0] or "+" in grid_arr2[1] or "+" in grid_arr2[2] or "+" in grid_arr2[3] or "+" in grid_arr2[4] or "+" in grid_arr2[5] or "+" in grid_arr2[6] or "+" in grid_arr2[7] or "+" in grid_arr2[8] or "+" in grid_arr2[9] or "+" in grid_arr2[10]) and ("+" in grid_arr1[0] or "+" in grid_arr1[1] or "+" in grid_arr1[2] or "+" in grid_arr1[3] or "+" in grid_arr1[4] or "+" in grid_arr1[5] or "+" in grid_arr1[6] or "+" in grid_arr1[7] or "+" in grid_arr1[8] or "+" in grid_arr1[9] or "+" in grid_arr1[10]):
            input("Press enter for next player:")
            os.system('cls')
            print("--",player1,"--")
            input("Press Enter")            
            grid_print1()
            user_choice1()
            input("Press enter for next player:")
            os.system('cls')
            print("--",player2,"--")
            input("Press Enter")            
            grid_print2()
            user_choice2()
        for columns in grid_arr1:
            if "+" in columns:
                decider1 += 1
        for columns in grid_arr2:
            if "+" in columns:
                decider2 += 1
        if decider1 == 0 and decider2 == 0:
            print("\nGAME DRAWN")
        elif decider1 == 0:
            print("\n",player2, " WINS", sep = "")
        elif decider2 == 0:
            print("\n",player1, " WINS", sep = "")        
        time.sleep(3)
        os.system('cls')
        again = input("New Game?(y/n)\n")
        if again == "y":
            print("Initiating new game...")
            time.sleep(4)
            
            main()
        else:
            print("Exiting game...")
            time.sleep(4)



if __name__ == "__main__":
    grid_arr2 = []
    grid_arr1 = []
    main()