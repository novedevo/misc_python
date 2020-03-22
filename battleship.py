import random

board = [['O']*10 for _ in range(10)]

def printboard(brd):
    #for row in brd:
        #print(" ".join(row))
    for row in brd:
        row2 = []
        for i,point in enumerate(row):
            try:
                if row[i-1] == point == '█':
                    row2.append('█')
                else:
                    row2.append(' ')
            finally:
                row2.append(point)
        print(''.join(row2))
        #row2 = []

class Ship:
    def __init__(self, length, is_vertical):

        self.length = length
        self.is_vertical = is_vertical

    def place(ships):
        for ship in ships:
            ship.coords = (placeShip(ship))

    

def rint():
    x = random.randint(0,9)
    y = random.randint(0,9)
    return [x,y]

def checkIfOccupiedAndFill(x,y):
    if not board[x][y] == '█':
        board[x][y] = '█'
        return True
    else:
        return False

aircraft_carrier = Ship(5, random.choice([True, False]))
battleship = Ship(4, random.choice([True, False]))
destroyer = Ship(3, random.choice([True, False]))
submarine = Ship(3, random.choice([True, False]))
pt_cruiser = Ship(2, random.choice([True, False]))

def placeShip(ship):
    
    while True:
        infr = False
        cords = rint()
        xcords = cords[0]
        ycords = cords[1]
        cordlist = []
        
        for i in range(0, ship.length):
            if ship.is_vertical:
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
            if board[i[0]][i[1]] == '█':
                infr = True
                
        if not infr:
            break
    for i in cordlist:
        checkIfOccupiedAndFill(i[0], i[1])
    return(cordlist)

Ship.place([aircraft_carrier, battleship, destroyer, submarine, pt_cruiser])

printboard(board)
