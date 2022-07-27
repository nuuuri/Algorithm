# P[5] 메모리 119560 KB  시간 424ms

def rotateFace(idx):
    cube[idx] = list(map(list, zip(*cube[idx][::-1])))

def rotate(arr, dir, idx):
    if dir == '+':
        temp = [cube[x][y][z] for x,y,z in arr[3]]
        for i in range(3, -1, -1):
            for j in range(3):
                x, y, z = arr[i][j]

                if i == 0:
                    cube[x][y][z] = temp[j]
                else:
                    xx, yy, zz = arr[i-1][j]
                    cube[x][y][z] = cube[xx][yy][zz]
        rotateFace(idx)

    else:
        temp = [cube[x][y][z] for x,y,z in arr[0]]
        for i in range(0, 4):
            for j in range(3):
                x, y, z = arr[i][j]

                if i == 3:
                    cube[x][y][z] = temp[j]
                else:
                    xx, yy, zz = arr[i+1][j]
                    cube[x][y][z] = cube[xx][yy][zz]
        for _ in range(3):
            rotateFace(idx)

for _ in range(int(input())):
    n = int(input())
    cube = [[[x for _ in range(3)] for _ in range(3)] for x in 'wyrogb']

    for move in input().split():
        face = move[0]
        dir = move[1]
        
        if face == 'U':
            rotate([[(3,0,2), (3,0,1), (3,0,0)],[(5,0,2), (5,0,1), (5,0,0)],[(2,0,2), (2,0,1), (2,0,0)],[(4,0,2), (4,0,1), (4,0,0)]], dir, 0)
        elif face == 'D':
            rotate([[(2,2,0), (2,2,1), (2,2,2)],[(5,2,0), (5,2,1), (5,2,2)],[(3,2,0), (3,2,1), (3,2,2)],[(4,2,0), (4,2,1), (4,2,2)]], dir, 1)
        elif face == 'F':
            rotate([[(0,2,0), (0,2,1), (0,2,2)],[(5,0,0), (5,1,0), (5,2,0)],[(1,0,2), (1,0,1), (1,0,0)],[(4,2,2), (4,1,2), (4,0,2)]], dir, 2)
        elif face == 'B':
            rotate([[(0,0,2), (0,0,1), (0,0,0)],[(4,0,0), (4,1,0), (4,2,0)],[(1,2,0), (1,2,1), (1,2,2)],[(5,2,2), (5,1,2), (5,0,2)]], dir, 3)
        elif face == 'L':
            rotate([[(0,0,0), (0,1,0), (0,2,0)],[(2,0,0), (2,1,0), (2,2,0)],[(1,0,0), (1,1,0), (1,2,0)],[(3,2,2), (3,1,2), (3,0,2)]], dir, 4)
        elif face == 'R':
            rotate([[(0,2,2), (0,1,2), (0,0,2)],[(3,0,0), (3,1,0), (3,2,0)],[(1,2,2), (1,1,2), (1,0,2)],[(2,2,2), (2,1,2), (2,0,2)]], dir, 5)

    for i in range(3):
        print(''.join(cube[0][i]))