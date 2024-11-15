from termcolor import colored
def makeBoard(o,x):
    mark = ['O' if o[0]== 1 else ("X" if x[0] == 1 else 0),
            'O' if o[1]== 1 else ("X" if x[1] == 1 else 1),
            'O' if o[2]== 1 else ("X" if x[2] == 1 else 2),
            'O' if o[3]== 1 else ("X" if x[3] == 1 else 3),
            'O' if o[4]== 1 else ("X" if x[4] == 1 else 4),
            'O' if o[5]== 1 else ("X" if x[5] == 1 else 5),
            'O' if o[6]== 1 else ("X" if x[6] == 1 else 6),
            'O' if o[7]== 1 else ("X" if x[7] == 1 else 7),
            'O' if o[8]== 1 else ("X" if x[8] == 1 else 8)]
    
    print(f' {colored(mark[0], "grey" if mark[0] == 0 else ("cyan" if mark[0]=="O" else "red"))} {colored('|', "magenta")} {colored(mark[1], "grey" if mark[1] == 1 else ("cyan" if mark[1] == "O" else "red"))} {colored('|', "magenta")} {colored(mark[2], "grey" if mark[2] == 2 else ("cyan" if mark[2]=="O" else "red"))} ')
    print(f'{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}')
    print(f' {colored(mark[3], "grey" if mark[3] == 3 else ("cyan" if mark[3]=="O" else "red"))} {colored('|', "magenta")} {colored(mark[4], "grey" if mark[4] == 4 else ("cyan" if mark[4]=="O" else "red"))} {colored('|', "magenta")} {colored(mark[5], "grey" if mark[5] == 5 else ("cyan" if mark[5]=="O" else "red"))} ')
    print(f'{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}')
    print(f' {colored(mark[6], "grey" if mark[6] == 6 else ("cyan" if mark[6]=="O" else "red"))} {colored('|', "magenta")} {colored(mark[7], "grey" if mark[7] == 7 else ("cyan" if mark[7]=="O" else "red"))} {colored('|', "magenta")} {colored(mark[8], "grey" if mark[8] == 8 else ("cyan" if mark[8]=="O" else "red"))} ')
    
def makeSum(a,b,c):
    return a+b+c

def checkWin(o,x):
    winPos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    for i in winPos:
        if makeSum(o[i[0]], o[i[1]], o[i[2]]) == 3:
            print(colored("O won th game! 🎉🎉🎉", "cyan"))
            return 0
        if makeSum(x[i[0]], x[i[1]], x[i[2]]) == 3:
            print(colored("X won th game! 🎉🎉🎉", "red"))
            return 1
        
    return -1 
            

def checkFull(o, x):
    if all(val != 0 for val in o) and all(val != 0 for val in x):
        return True
    return False

# def fun(x,o):
#     for val in x:
#         if x[val] == 1 :
#             x[val] == "X"
#             break
    
#     for val in o:
#         if o[val] == 1:
#             o[val] == "O"
#             break
     
if __name__ == "__main__":
    o = [0] *9 
    x = [0] *9
    turn = 0 
    playerOne = input("Enter name of Player 1: ")
    playerTwo = input("Enter name of Player 2: ")
    makeBoard(o,x)
    
    while True:
        #jo turn = 0 -> O and 1 -> X
        if(turn == 0):
            print(f'{playerOne}\'s turn')
            val = int(input("Enter a Value: "))
            o[val] = 1 #j value nakhi tya jai ne 1 kari dese
        else:
            print(f'{playerOne}\'s turn')
            val = int(input("Enter a Value: "))
            x[val] = 1
        
        makeBoard(o,x)
        turn = 1 - turn 
        
        winner = checkWin(o,x)
        if winner != -1 :
            print("Match is over!")
            break
        if checkFull(o, x):
            print("It's a draw!")
            break