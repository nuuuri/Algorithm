# U D F B L R
# 0 1 2 3 4 5
cube = [[x * 3] * 3 for x in 'wyrogb']

print(cube)

for _ in range(int(input())):
    n = int(input())
    for move in input().split():
        face = move[0]
        dir = move[1]
        
        if face == 'U':
            if dir == '+':
                temp = cube[2][0]
                cube[2][0] = cube[5][0]
                cube[5][0] = cube[3][0]
                cube[3][0] = cube[4][0]
                cube[4][0] = temp
            else:
                temp = cube[2][0]
                cube[2][0] = cube[4][0]
                cube[4][0] = cube[3][0]
                cube[3][0] = cube[5][0]
                cube[5][0] = temp

        elif face == 'D':
            if dir == '+':
                temp = cube[2][2]
                cube[2][2] = cube[5][2]
                cube[5][2] = cube[3][2]
                cube[3][2] = cube[4][2]
                cube[4][2] = temp
            else:
                temp = cube[2][2]
                cube[2][2] = cube[4][2]
                cube[4][2] = cube[3][2]
                cube[3][2] = cube[5][2]
                cube[5][2] = temp

        elif face == 'F':
            if dir == '+':
                cube[5][0][0], cube[5][1][0], cube[5][2][0] = temp

            print()
        elif face == 'B':
            print()
        elif face == 'L':
            print()
        elif face == 'R':
            print(0)