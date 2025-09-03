values = {
    'queen': 9,
    'rook': 5,
    'bishop': 3,
    'knight': 3,
    'pawn': 1,
}

board1 = [['b-bishop',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ','b-queen',' ',' ',' ',' ','w-queen'],
              [' ','b-king',' ','b-pawn','w-rook',' ',' ',' '],
              [' ',' ',' ',' ','w-pawn',' ',' ',' '],
              [' ',' ',' ',' ',' ','w-bishop',' ',' '],
              ['w-king',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ','b-pawn','b-pawn',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ']]

def pieces_value(arr, s):
    color = s[0]
    total = 0
    for i in range(len(arr)):
        for x in range(len(arr[i])):
            if arr[i][x] != ' ' and arr[i][x][0:1] == color:
                piece = arr[i][x][2:]
                if piece != 'king':
                    total += values[piece]
    return total

pieces_value(board1, 'white')