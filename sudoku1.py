import random

#grid



# level dificuldade

print("level de dificuldade")
print("     1. Beginner")
print("     2. Intermediate")
print("     3. Advanced")
print()
print("Insira seu level de dificuldade : ",end="")
level = int(input())
if level==1:
    q = 35
elif level==2:
    q = 20
else:
    q = 8
#lugar grid

grid = [[0 for x in range(9)] for y in range(9)]

# valida grid

def check_valid(mesh,r,c,n):
    valid = True
    #checa row e column
    for x in range(9):
        if mesh[x][c] == n:
            valid = False
            break
    for y in range(9):
        if mesh[r][y] == n:
            valid = False
            break
    row_section = r // 3
    col_section = c // 3
    for x in range(3):
        for y in range(3):
            #valida sessao
            if mesh[row_section * 3 + x][col_section * 3 + y] == n:
                valid = False
                break
    return valid

# gerando o grid
for i in range(q):
    row = random.randrange(9)
    col = random.randrange(9)
    num = random.randrange(1,10)
    while not check_valid(grid,row,col,num) or grid[row][col]!=0:
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
    grid[row][col]=num


# print o grid

cnt_i = 0
for i in range(13):
    cnt_j = 0
    for j in range(13):
        if i%4==0:
            print("+---------+---------+---------+",end="")
            cnt_i+=1
            break
        elif j%4==0:
            print("|",end="")
            cnt_j+=1
        else:
            print("",grid[i-cnt_i][j-cnt_j],"" ,end="")
    print()