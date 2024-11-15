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
    print(f' {colored(mark[0], "grey")} {colored('|', "magenta")} {colored(mark[1], "grey")} {colored('|', "magenta")} {colored(mark[2], "grey")} ')
    print(f'{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}')
    print(f' {colored(mark[3], "grey")} {colored('|', "magenta")} {colored(mark[4], "grey")} {colored('|', "magenta")} {colored(mark[5], "grey")} ')
    print(f'{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}')
    print(f' {colored(mark[6], "grey")} {colored('|', "magenta")} {colored(mark[7], "grey")} {colored('|', "magenta")} {colored(mark[8], "grey")} ')
    
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