# '2 1' -> (2, 1)

def print_arr():
    print(f'''* 0 1 2
0 {arr[0][0]} {arr[0][1]} {arr[0][2]}
1 {arr[1][0]} {arr[1][1]} {arr[1][2]}
2 {arr[2][0]} {arr[2][1]} {arr[2][2]}''')


def check_placement(x, y):
    if arr[x][y] != "-":
        return False
    return True


def is_winner():
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] != "-":
            return True
        if arr[0][i] == arr[1][i] == arr[2][i] != "-":
            return True
    if arr[0][0] == arr[1][1] == arr[2][2] != "-" or arr[0][2] == arr[1][1] == arr[2][0] != "-":
        return True
    return False


def is_end():
    for i in range(3):
        for j in range(3):
            if arr[i][j] == "-":
                return False
    return True


arr = [["-", "-", "-"],
       ["-", "-", "-"],
       ["-", "-", "-"]]
print_arr()


representation = (
    ('x', 'крестика'),
    ('o', 'нолика')
)
k = 0
has_error = False
while True:
    if not has_error:
        message = f"введите координаты {representation[k][1]}: "
    else:
        message = f"координаты не удовлетворяют условию, введите другие координаты {representation[k][1]}: "
    x, y = list(map(int, input(message).split()))

    if x < 0 or x > 2 or y < 0 or y > 2 or not check_placement(x, y):
        has_error = True
        continue

    has_error = False
    arr[x][y] = representation[k][0]
    k = (k + 1) % 2
    print_arr()

    if is_winner():
        print(f"игра закончена, выиграл игрок, играющий {representation[not k][1]}ми")
        break
    elif is_end():
        print("игра закончилась вничью")
        break

