
def makeBoard():
    print(f' {text_color(0)} | {text_color(1)} | {text_color(2)} ')
    print(f'———|———|———')
    print(f' {text_color(3)} | {text_color(4)} | {text_color(5)} ')
    print(f'———|———|———')
    print(f' {text_color(6)} | {text_color(7)} | {text_color(8)} ')

def text_color(num):
    return f'\033[97m{num}'
        
if __name__ == "__main__":
    o = [0] *9 
    x = [0] *9
    turn = 0 
    makeBoard()
    
     
