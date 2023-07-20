import random

def printMenu():
    print("\n========================================================")
    print("Welcome to the Dice Roller program!\nPlease select an option:\n")
    print("1. Rolle Dice")
    print("2. Instructions")
    print("3. Credits\n")
    print("0. Exit")
    print("========================================================\n")

printMenu()
opt = input("");
while(opt != '0'):

    #No Option
    if( (opt != '1') & (opt != '2') & (opt != '3') & (opt != '0') ):
        print("ERROR: Option number not available! Please select another number.")
    
    #Dice Roller
    elif(opt == '1'):
        yn = 'Y'
        while(yn == 'Y'):
            print("\n========================================================")
            text= input("Insert number of dices to rolle and type of dice: ")
            num = text.split()

            if(len(num) != 2):
                print("ERROR: To many or to low number of attributes! Please try again.")
                print("========================================================\n")
            elif(not num[0].isdigit() or not num[1].isdigit):
                print("ERROR: Incorrect type of attributes! Please try again.")
                print("========================================================\n")
            else:
                print("Rolling",num[0],"dice(s) of",num[1],":")
                i = 0
                while i < int(num[0]):
                    print(random.randint(0,int(num[1])-1) + 1)
                    i = i+1
                yn = input("Do you want to change and rolle the dice again? (Y/else): ") 
                print("========================================================\n")
        

    #Intstructions
    elif(opt == '2'):
        print("\n========================================================")
        print("For this program you only need to input two numbers:")
        print(" -> The number of dices you want to rolle (N)")
        print(" -> The the type of dice you want to rolle (T)\n")
        print("Exemple:\nInsert number od dices to rolle and type of dice: N T\n")
        print("0. Back")
        print("========================================================\n")
        ext = input("")
        while(ext != '0'):
            ext = input("")

    #Credits
    elif(opt == '3'):
        print("\n========================================================")
        print("This Program was created by sonic28g :D\n")
        print("0. Back")
        print("========================================================\n")
        ext = input("")
        while(ext != '0'):
            ext = input("")

    #Menu
    printMenu()
    opt = input("");





