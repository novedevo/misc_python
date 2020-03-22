import random

board = [['O']*10 for _ in range(10)]

#for i in range(10):
#    board.append(['O']*10)

def printboard(brd):
    for i in brd:
        print(i)

class Ship:

    def __init__(self, length, coords, isVertical):

        self.length = length
        self.coords = coords
        self.isVertical = isVertical

    def place(ships):
        for ship in ships:
            placeShip(ship)

def rint():
#    while True:
    x = random.randint(0,9)
    y = random.randint(0,9)
    return [x,y]
#        if board[x][y] == 'O':
#            board[x][y] = 'X'
#            return [x,y]
#            break

def checkIfOccupiedAndFill(x,y):
    if not board[x][y] == 'A':
        board[x][y] = 'A'
        return True
    else:
        return False

ship_0 = Ship(5, 0, random.choice([True, False]))
ship_1 = Ship(4, 0, random.choice([True, False]))
ship_2 = Ship(3, 0, random.choice([True, False]))
ship_3 = Ship(3, 0, random.choice([True, False]))
ship_4 = Ship(2, 0, random.choice([True, False]))

def placeShip(ship):
    
    while True:
        infr = False
        cords = rint()
        xcords = cords[0]
        ycords = cords[1]
        cordlist = []
        for i in range(0, ship.length):
            if ship.isVertical:
                cordlist.append([xcords,ycords+i])
                if ycords+i > 9:
                    infr = True
            else:
                cordlist.append([xcords+i, ycords])
                if xcords+i > 9:
                    infr = True
        if infr:
            continue
        for i in cordlist:
            #print(i)
            if not board[i[0]][i[1]] == 'A':
                pass
            else:
                infr = True
        if not infr:
            break
    for i in cordlist:
        checkIfOccupiedAndFill(i[0], i[1])
    return(cordlist)

Ship.place([ship_0,ship_1,ship_2, ship_3, ship_4])

printboard(board)
