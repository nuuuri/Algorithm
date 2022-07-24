# U D F B L R
cube = [[x * 3] * 3 for x in 'wyrogb']

print(cube)

for _ in range(int(input())):
    n = int(input())
    for move in input().split():
        face = move[0]
        dir = move[1]
        
        if face == 'U':
            print()
        elif face == 'D':
            print()
        elif face == 'F':
            print()
        elif face == 'B':
            print()
        elif face == 'L':
            print()
        elif face == 'R':
            print(0) 