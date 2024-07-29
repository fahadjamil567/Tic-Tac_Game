rows, cols = (3, 3)
arr = [['', '', ''],
    ['', '', ''],
    ['', '', '']
]
player = ['x', 'y']
curr_player = 0
win = False
def print_game():
    for i in range(rows):
        print(arr[i], end='\n')
    #print((arr))

def place(r,c):
    global curr_player
    if(arr[r][c]!=''):
        print("you can not overwite ")
        return
    arr[r][c] = player[curr_player]
    curr_player += 1
    if curr_player == 2:
        curr_player = 0
    return
def win_game():
    global win

    if ((arr[0][0] == 'x' and arr[0][1] == 'x' and arr[0][2] == 'x') or (
            arr[1][0] == 'x' and arr[1][1] == 'x' and arr[1][2] == 'x') or (
            arr[2][0] == 'x' and arr[2][1] == 'x' and arr[2][2] == 'x') or(

            arr[0][0] == 'x' and arr[1][0] == 'x' and arr[2][0] == 'x') or (
            arr[0][1] == 'x' and arr[1][1] == 'x' and arr[2][1] == 'x') or (
            arr[0][2] == 'x' and arr[1][2] == 'x' and arr[2][2] == 'x') or(


            arr[0][0] == 'x' and arr[1][1] == 'x' and arr[2][2] == 'x') or (
            arr[2][0] == 'x' and arr[1][1] == 'x' and arr[0][2] == 'x') or (
arr[2][0] == 'x' and arr[1][1] == 'x' and arr[0][2] == 'x') ):
        print("Player 1 wins :)")
        win = True

    if ((arr[0][0] == 'y' and arr[0][1] == 'y' and arr[0][2] == 'y') or (
            arr[1][0] == 'y' and arr[1][1] == 'y' and arr[1][2] == 'y') or (
            arr[2][0] == 'y' and arr[2][1] == 'y' and arr[2][2] == 'y') or (

            arr[0][0] == 'y' and arr[1][0] == 'y' and arr[2][0] == 'y') or (
            arr[0][1] == 'y' and arr[1][1] == 'y' and arr[2][1] == 'y') or (
            arr[0][2] == 'y' and arr[1][2] == 'y' and arr[2][2] == 'y') or (


            arr[0][0] == 'y' and arr[1][1] == 'y' and arr[2][2] == 'y') or (
            arr[2][0] == 'y' and arr[1][1] == 'y' and arr[0][2] == 'y')):
        print("Player 2 wins :)")
        win = True

    return

def game():
    while not win:
        print_game()
        win_game()
        print("Enter row and column")
        x = ord(input())-48
        y = ord(input())-48
        if x > 2 or y > 2:

            print(f"{x},{y}")
            continue
        place(x, y)

game()