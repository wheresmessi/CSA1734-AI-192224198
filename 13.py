import random

COMPUTER = 1
HUMAN = 2

class move:
    def __init__(self):
        self.pile_index = 0
        self.stones_removed = 0

def showPiles(piles, n):
    print("Current Game Status -> ")
    print(*piles)

def gameOver(piles, n):
    for i in range(n):
        if piles[i] != 0:
            return False
    return True

def declareWinner(whoseTurn):
    if whoseTurn == COMPUTER:
        print("\nHUMAN won")
    else:
        print("\nCOMPUTER won")
    return

def calculateNimSum(piles, n):
    nimsum = piles[0]
    for i in range(1, n):
        nimsum = nimsum ^ piles[i]
    return nimsum

def makeMove(piles, n, moves):
    nim_sum = calculateNimSum(piles, n)

    if nim_sum != 0:
        for i in range(n):
            if (piles[i] ^ nim_sum) < piles[i]:
                moves.pile_index = i
                moves.stones_removed = piles[i] - (piles[i] ^ nim_sum)
                piles[i] = piles[i] ^ nim_sum
                break
    else:
        non_zero_indices = [None] * n
        count = 0
        for i in range(n):
            if piles[i] > 0:
                non_zero_indices[count] = i
                count += 1
        moves.pile_index = int(random.random() * count)
        moves.stones_removed = 1 + int(random.random() * piles[moves.pile_index])
        piles[moves.pile_index] -= moves.stones_removed
        if piles[moves.pile_index] < 0:
            piles[moves.pile_index] = 0

def playGame(piles, n, whoseTurn):
    print("\nGAME STARTS")
    moves = move()
    while not gameOver(piles, n):
        showPiles(piles, n)
        makeMove(piles, n, moves)
        if whoseTurn == COMPUTER:
            print("COMPUTER removes", moves.stones_removed, "stones from pile at index ", moves.pile_index)
            whoseTurn = HUMAN
        else:
            print("HUMAN removes", moves.stones_removed, "stones from pile at index", moves.pile_index)
            whoseTurn = COMPUTER
    showPiles(piles, n)
    declareWinner(whoseTurn)
    return

def knowWinnerBeforePlaying(piles, n, whoseTurn):
    print("Prediction before playing the game -> ", end="")
    if calculateNimSum(piles, n) != 0:
        if whoseTurn == COMPUTER:
            print("COMPUTER will win")
        else:
            print("HUMAN will win")
    else:
        if whoseTurn == COMPUTER:
            print("HUMAN will win")
        else:
            print("COMPUTER will win")
    return

# Test Case 1
piles = [3, 4, 5]
n = len(piles)

knowWinnerBeforePlaying(piles, n, COMPUTER)
playGame(piles, n, COMPUTER)
