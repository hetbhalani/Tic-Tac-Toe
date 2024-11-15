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
    
def sum(a,b,c):
    return a+b+c

def checkWin(o,x):
    winPos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    for i in winPos:
        if sum(o[i[0]], o[i[1]], o[i[2]]) == 3:
            print(colored("O won th game! 🎉🎉🎉", "cyan"))
            return 0
        
            
            
    
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
    while True:
        #jo turn = 0 -> O and 1 -> X
        makeBoard(o,x)
        if(turn == 0):
            print("O's turn")
            val = int(input("Enter a Value: "))
            o[val] = 1 #j value nakhi tya jai ne 1 kari dese
        else:
            print("X's turn")
            val = int(input("Enter a Value: "))
            x[val] = 1
        turn = 1 - turn    