from audioop import add


def getMatrix():
    h,w = 5,3
    return [[' ' for x in range(w)] for y in range(h)]

def fillY(col:int,matrix):
    for x in range(5):
        matrix[x][col] = '#'

def fillX(row:int,matrix):
    for x in range(3):
        matrix[row][x] = '#'

def eight():
    m = getMatrix()
    fillY(0,m)
    fillY(2,m)
    fillX(0,m)
    fillX(2,m)
    fillX(4,m)
    return m

def nine():
    m = eight()
    m[3][0]=' '
    return m

def three():
    m = nine()
    m[1][0]=' '    
    return m

def one():
    m = getMatrix()
    fillY(2,m)    
    return m

def four():
    m = nine()
    m[0][1] = ' '
    m[4][0] = ' '
    m[4][1] = ' '
    return m

def five():
    m = nine()
    m[1][2] = ' '
    return m

def six():
    m = eight()
    m[1][2] = ' '
    return m

def seven():
    m = getMatrix()
    fillX(0,m)
    fillY(2,m)    
    return m


def two():
    m = eight()
    m[1][0]=' '    
    m[3][2]=' '
    return m

options = {1 : one, 
           2 : two, 
           3 : three,
           4 : four,
           5 : five,
           6 : six,
           7 : seven,
           8 : eight,
           9 : nine,
}

def add(left:list,right:list):
    for x in range(5):
        left[x].append(' ')
        for e in right[x]:
            left[x].append(e)

def printMatrix(matrix):
    for x  in range(len(matrix)):
        for y in range(len(matrix[x])):
            print(matrix[x][y],end='')
        print()

def printDigits(v:str):
    m=options[int(v[0])]()
    if len(v) == 1:
        printMatrix(m)
    else :
        for e in v[1:]:
            add(m,options[int(e)]())
    printMatrix(m)            

