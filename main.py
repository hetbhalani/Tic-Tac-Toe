from termcolor import colored
def makeBoard():
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
    makeBoard()
    
     
