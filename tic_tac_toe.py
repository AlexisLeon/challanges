def isSolved(board):
    t = testcases(board)
    if 1 in t: return 1
    if 2 in t: return 2
    if all(x == None for x in t):
        for n in board:
            if 0 in n: return -1  # Unsolved
        if all(x != 0 for x in board):
            return 0  # Cat's Game

def testcases(b):
    tc_1 = winner(b[0][0], b[0][1], b[0][2])  # Top horizontal
    tc_2 = winner(b[1][0], b[1][1], b[1][2])  # Middle horizontal
    tc_3 = winner(b[2][0], b[2][1], b[2][2])  # Bottom horizontal
    tc_4 = winner(b[0][0], b[1][0], b[2][0])  # Left vertical
    tc_5 = winner(b[0][1], b[1][1], b[2][1])  # Middle vertical
    tc_6 = winner(b[0][2], b[1][2], b[2][2])  # Right vertical
    tc_7 = winner(b[0][0], b[1][1], b[2][2])  # From top left to bottom right
    tc_8 = winner(b[0][2], b[1][1], b[2][0])  # From top right to bottom left
    return [tc_1, tc_2, tc_3, tc_4, tc_5, tc_6, tc_7, tc_8]

def winner(a,b,c):
    if a == 1 and b == 1 and c == 1: return 1  # If equal to 1 = X
    elif a == 2 and b == 2 and c == 2: return 2  # If equal to 2 = O
    else: return None  # No one win the testcase

print isSolved([[0,0,2],[0,0,2],[0,0,2]])  #Wins: 2
print isSolved([[1,2,1],[1,1,2],[2,1,2]])  #Cat's game: 0
print isSolved([[0,0,0],[0,0,0],[0,0,0]])  #Unsolved: -1