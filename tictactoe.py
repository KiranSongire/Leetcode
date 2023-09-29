#Tic-Tac-Toe
def user_game():
    R1 = [' ',' ',' ']
    R2 = [' ',' ',' ']
    R3 = [' ',' ',' ']
    print(R1)
    print(R2)
    print(R3)
#Take user input at particular index 
    game_list = [0,1,2]
    #user_input = int(input("Enter the position at which you want to insert:" )
    string = 'wrong'
    while string not in ['0','1','2']:
        string = input("Enter the position at which you want to insert:" )
        if string not in ['0','1','2']:
            print("******* USER INPUT  CHOICE INVALID:*******")
    return int(string)
