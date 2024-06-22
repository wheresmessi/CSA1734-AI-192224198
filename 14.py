import random

COMPUTER = 1
HUMAN = 2

class Move:
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
        non_zero_indices = [i for i in range(n) if piles[i] > 0]
        move_index = random.choice(non_zero_indices)
        moves.pile_index = move_index
        moves.stones_removed = 1 + int(random.random() * piles[move_index])
        piles[move_index] -= moves.stones_removed
        if piles[move_index] < 0:
            piles[move_index] = 0

def minimax(piles, n, depth, is_maximizing, alpha, beta):
    if gameOver(piles, n):
        if is_maximizing:
            return -1  # Assuming COMPUTER is maximizing
        else:
            return 1   # Assuming HUMAN is minimizing

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(n):
            if piles[i] > 0:
                for stones_removed in range(1, piles[i] + 1):
                    piles[i] -= stones_removed
                    eval = minimax(piles, n, depth + 1, False, alpha, beta)
                    piles[i] += stones_removed
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(n):
            if piles[i] > 0:
                for stones_removed in range(1, piles[i] + 1):
                    piles[i] -= stones_removed
                    eval = minimax(piles, n, depth + 1, True, alpha, beta)
                    piles[i] += stones_removed
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def playGame(piles, n, whoseTurn):
    print("\nGAME STARTS")
    moves = Move()
    while not gameOver(piles, n):
        showPiles(piles, n)
        if whoseTurn == COMPUTER:
            max_eval = -float('inf')
            best_move = Move()
            for i in range(n):
                if piles[i] > 0:
                    for stones_removed in range(1, piles[i] + 1):
                        piles[i] -= stones_removed
                        eval = minimax(piles, n, 0, False, -float('inf'), float('inf'))
                        piles[i] += stones_removed
                        if eval > max_eval:
                            max_eval = eval
                            best_move.pile_index = i
                            best_move.stones_removed = stones_removed
            moves = best_move
            print("COMPUTER removes", moves.stones_removed, "stones from pile at index ", moves.pile_index)
            whoseTurn = HUMAN
        else:
            makeMove(piles, n, moves)
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
