#Sudoku
#How should a board be represented?
#list of lists
#board = [r1, r2, ...]
#efficiency
    #check for 8s

#Define Functions

#Initial Create

def createBoard(r0, r1, r2, r3, r4, r5, r6, r7, r8):
    #different things later
    board = [r0, r1, r2, r3, r4, r5, r6, r7, r8];
    return board

def createNBoard(board, num):
    fill = []
    for i in range(9):
        row = []
        for j in range(9):
            if board[i][j]:
                row.append(0)
            else:
                row.append(num)
        fill.append(row)
    return fill

#Retrieve Data
def getRow(board, rowNum):
    row = board[rowNum]
    return row

def getColumn(board, colNum):
    col = []
    for i in range(9):
        col.append(board[i][colNum])
    return col

def getBox(board, boxNum):
    box = []
    ranB0 = ((boxNum+3)%3)*3
    ranT0 = ranB0 + 3
    ranB1 = (boxNum//3)*3
    ranT1 = ranB1 + 3
    for i in range(ranB1, ranT1):
        for j in range(ranB0, ranT0):
            box.append(board[i][j])
    return box

def getLoc(board, num):
    loc = [] #[[r,c,b],[r,c,b]...]
    for r in range(9):
        for c in range(9):
            b = 0
            if board[r][c] == num:
                b += (r//3)*3+(c//3)
                loc.append([r,c,b])
    return loc

def getBoxLoc(box_n, tile): #finds location of tile on board from box and tile in box
    row = (box_n//3)*3 + (tile//3)
    col = (box_n%3)*3 + (tile%3)
    return [row, col]

def getNum(board, row, col):
    return board[row][col]

def getMissing(listy, n=0):
    miss = []
    if n == 0:
        for i in range(1,10):
            if i not in listy:
                miss.append(i)
    else:
        for i in listy:
            if i != 0:
                miss.append(i)
    return miss


#display functions
def OLDprintBoard(board):
    brd = str(board)
    print(brd[2:27] + '\n' + brd[31:56] + '\n' + brd[60:85] + '\n'
        + brd[89:114] + '\n' + brd[118:143] + '\n' + brd[147:172] + '\n'
        + brd[176:201] + '\n' + brd[205:230] + '\n' + brd[234:259])

def printBox(box):
    box = str(box)
    print(box[1:8] + '\n' + box[10:17] + '\n' + box[19:26])

def printBoard(board):
    brd = str(board)
    print(brd[2:9]   + ' | ' + brd[11:18] + ' | ' + brd[20:27] + '\n'
        + brd[31:38] + ' | ' + brd[40:47] + ' | ' + brd[49:56] + '\n'
        + brd[60:67] + ' | ' + brd[69:76] + ' | ' + brd[78:85] + '\n\n'
        + brd[89:96] + ' | ' + brd[98:105] + ' | ' + brd[107:114] + '\n'
        + brd[118:125] + ' | ' + brd[127:134] + ' | ' + brd[136:143] + '\n'
        + brd[147:154] + ' | ' + brd[156:163] + ' | ' + brd[165:172] + '\n\n'
        + brd[176:183] + ' | ' + brd[185:192] + ' | ' + brd[194:201] + '\n'
        + brd[205:212] + ' | ' + brd[214:221] + ' | ' + brd[223:230] + '\n'
        + brd[234:241] + ' | ' + brd[243:250] + ' | ' + brd[252:259] + '\n')

def available(board, num):
    loc = getLoc(board, num)
    rows = []
    cols = []
    boxes = []
    check = createNBoard(board, 1)
    for i in loc:
        # out[i[0]][i[1]] = num
        rows.append(i[0])
        cols.append(i[1])
        boxes.append(i[2])
    for i in rows:
        for j in range(9):
            check[i][j] = 0
    for i in cols:
        for j in range(9):
            check[j][i] = 0
    for i in boxes:
        ranB0 = ((i+3)%3)*3
        ranT0 = ranB0 + 3
        ranB1 = (i//3)*3
        ranT1 = ranB1 + 3
        for j in range(ranB1, ranT1):
            for k in range(ranB0, ranT0):
                check[j][k] = 0
    return check

def easyFill(board):        #Fills obvious tiles
    for i in range(9):
        row = getRow(board, i)
        rowM = getMissing(row)
        if len(rowM) == 1:
            board[i][row.index(0)] = rowM[0]
            easyFill(board)
        col = getColumn(board, i)
        colM = getMissing(col)
        if len(colM) == 1:
            board[col.index(0)][i] = col[0]
            easyFill(board)
        box = getBox(board, i)
        boxM = getMissing(box)
        if len(boxM) == 1:
            print(box)
            loc = getBoxLoc(i, box.index(0))
            board[loc[0]][loc[1]] = boxM[0]
            easyFill(board)
    return board

def availableFill(board):
    availableArray = []
    for i in range(1,10):
        availableArray.append(available(board, i))
    # print(availableArray)
    for i in range(9):          #row
        for j in range(9):      #tile
            sum = 0
            for k in range(9):  #board
                # print('row = '+ str(i))
                # print('tile = '+ str(j))
                # print('board = '+ str(k))
                # print(availableArray[k][i][j])
                sum += availableArray[k][i][j]
                if availableArray[k][i][j] == 1:
                    h = k+1
            if sum == 1:
                # print("h = " + str(h))
                board[i][j] = h
                availableFill(board)
    return board



#Initial Variables
r0 = [0, 0, 9, 2, 0, 0, 7, 0, 0]; #Later will be set by function parsing through image
r1 = [0, 0, 0, 0, 0, 0, 0, 6, 0];
r2 = [0, 6, 5, 9, 1, 3, 8, 0, 2];
r3 = [6, 0, 7, 0, 0, 0, 0, 3, 5];
r4 = [0, 2, 4, 7, 3, 0, 0, 1, 0];
r5 = [0, 0, 0, 6, 5, 0, 0, 9, 0];
r6 = [0, 7, 0, 0, 0, 0, 0, 0, 6];
r7 = [0, 5, 0, 8, 6, 0, 0, 0, 0];
r8 = [1, 8, 0, 0, 9, 0, 3, 7, 0];


#Code

board_0 = createBoard(r0, r1, r2, r3, r4, r5, r6, r7, r8)       #Input board into proper formatting
board_1 = board_0       #copy of board used to test; updated throughout





#TestCode
# printBox(getBox(board_0,3))
# print(getMissing(getBox(board_0,3)))
# print(getBoxLoc(3, 4))
# printBoard(easyFill(board_0))
# printBoard(board_0)
# print('----------------------------------')
# printBoard(available(board_0, 8))
# print('----------------------------------')
# printBoard(availableFill(board_0))
printBoard(board_0)
availableFill(board_0)
printBoard(board_0)
# printBoard(easyFill(board_0))
# printBoard(board_0)
# print('----------------------------------')
# printBoard(avahttps://www.amazon.com/gp/product/B07CXG6C9W?tag=fbasaperd-20&ascsubtag=pfb-DEVERD-1-9-2wqzf2tvntojns76&ref_=pfb_DEVERD_1_9_2wqzf2tvntojns76&fbclid=IwAR0bC-sgNuyCvFNzdY00-pdgdLiZIoX7ttxBX6W98k2xaU27lA_o1USAo34ilable(board_0, 9))
