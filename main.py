from termcolor import colored
def makeBoard(o,x):
    print(f' {colored(0, "grey")} {colored('|', "magenta")} {colored(1, "grey")} {colored('|', "magenta")} {colored(2, "grey")} ')
    print(f'{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}')
    print(f' {colored(3, "grey")} {colored('|', "magenta")} {colored(4, "grey")} {colored('|', "magenta")} {colored(5, "grey")} ')
    print(f'{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}{colored('|', "magenta")}{colored('———', "magenta")}')
    print(f' {colored(6, "grey")} {colored('|', "magenta")} {colored(7, "grey")} {colored('|', "magenta")} {colored(8, "grey")} ')
    
# def text_color(num):
#     return f'\033[97m{num}'
        
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
            
        break
    
     
