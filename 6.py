
# Write a function that validates whether a given Sudoku board is solved correctly. The board is represented as a 2D array of size 9x9. A valid solution must meet these conditions:
# Each row contains numbers 1–9 without repetition.
# Each column contains numbers 1–9 without repetition.
# Each 3x3 subgrid contains numbers 1–9 without repetition.

def func(board):

    # chashenebuli funqcia romelic amowmebs tu gadmocemuli masivi 1-9 ekemtebs sheicavs 
    # am yvelafers aketebs sortirebis mixedvit
    def is_valid_group(group):
        return sorted(group)==list(map(int, range(1, 10)))
    
    # vamowmebt rigebs
    for row in board:
        if not is_valid_group(row):
            return False
        
    # vamowmebt svetebs
    for j in range(9):
        col = [board[i][j] for i in range(9)]
        if not is_valid_group(col):
            return False
    
    # ! avamushave esec
    # vamowmebt 3x3ze - titoeul iteraciaze mowmdeba mtlianai 3x3 (qmnis masivs 9 elementit 2x3 gridis mixedvti da mas awvdis shemowmebis funqcias), 
    # ( 3 step ), shemdeg sam samobit gadadis titoeul jgufze
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [ board[i][j], board[i][j+1], board[i][j+2], 
                       board[i+1][j], board[i+1][j+1], board[i+1][j+2],
                       board[i+2][j], board[i+2][j+1], board[i+2][j+2],
                         ]
            print(subgrid)
            if not is_valid_group(subgrid):
                return False
    return True


# test cases 5:
print(func([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]))
print(func([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 7]  # Invalid: Two 7s in the last row
]
))
print(func([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 9, 7, 9]  # Invalid: Two 9s in the last column
]))
print(func([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 1, 9]  # Invalid: Two 1s in the bottom-right subgrid
]))
print(func([
    [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
]))
