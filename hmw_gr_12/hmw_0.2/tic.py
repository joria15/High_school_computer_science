# Caio semi-pro
#gabby noob
#ant == hacker
def table():
    ttt = []
    row = ["☐"]*3
    for i in range(3):
        ttt.append(row.copy())
    for i in range(len(ttt)):
        return ttt
   
def spot_same_x(tables, row_x, column_x):
    if tables[row_x][column_x] == "X" or tables[row_x][column_x] == "O":
            print("There is a letter already there")
            return False
    else:
        return True


def spot_same_o(tables, row_o, column_o):
    if tables[row_o][column_o] == "X" or tables[row_o][column_o] == "O":
            print("There is a letter already there")
            return False
    else:
        return True
   
#for x
def x_win(tables):
    #across
    if (tables[2][0] == tables[1][1] == tables[0][2] == "X") or (tables[0][0] == tables[1][1] == tables[2][2] == "X"):
        print("You win")
        return True
    
    for i in range(len(tables)):
        #horizantal
        if tables[i][0] == tables[i][1] == tables[i][2] == "X":
            print("You win")
            return True
        #vertical
        if tables[0][i] == tables[1][i] == tables[2][i] == "X":
            print("You win")
            return True
        else:
            return False

#for o
def o_win(tables):
    #across
    if (tables[2][0] == tables[1][1] == tables[0][2] == "O") or (tables[0][0] == tables[1][1] == tables[2][2] == "O"):
        print("You win")
        return True
    
    for i in range(len(tables)):
    #horizantal
        if tables[i][0] == tables[i][1] == tables[i][2] == "O":
            print("You win")
            return True
        #vertical
        if tables[0][i] == tables[1][i] == tables[2][i] == "O":
            print("You win")
            return True
        else:
            return False

def tictactoe(tables):
    while True:

        while True:
            while True:
                row_x = int(input("top to bottom: where would you like to place 'X': "))
                if row_x < 1 or row_x > 3:
                    print("try again!")
                else:
                    row_x -= 1
                    break

            while True:
                column_x = int(input("left to right: where would you like to place 'X': "))
                if column_x < 1 or column_x > 3:
                    print("try again!")
                else:
                    column_x -= 1
                    break


            if spot_same_x(tables, row_x, column_x) == False:
                continue
            else:
                tables[row_x][column_x] = "X"
                for i in range(len(tables)):
                    print(tables[i])
                break
        #X win
        if x_win(tables) == True:
            print("Good game!")
            break          
       
        while True:
           
            while True:
                row_o = int(input("top to bottom: where would you like to place 'O': "))
                if row_o < 1 or row_o > 3:
                    print("try again!")
                else:
                    row_o -= 1
                    break

            while True:
                column_o = int(input("left to right: where would you like to place 'O': "))
                if column_o < 1 or column_o > 3:
                    print("try again!")
                else:
                    column_o -= 1
                    break


            if spot_same_o(tables, row_o, column_o) == False:
                continue
            else:
                tables[row_o][column_o] = "O"
                for i in range(len(tables)):
                    print(tables[i])
                break
        #O win
        if o_win(tables) == True:
            print("Good game!")
            break
   
table_x_o = table()
tictactoe(table_x_o)
# make sure you cannot place where there is already letter



