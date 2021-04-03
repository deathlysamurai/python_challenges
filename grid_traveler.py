#How many ways can you travel on a grid of m*n dimensions,
#beginning in top-left, moving to bottom-right, and only
#making right or down moves.

#memoization
memo = {}

def main():
    rows = int(input("How many rows would you like?: "))
    columns = int(input("How many columns would you like?: "))
    moves = grid_traveler(rows, columns, memo)
    print(moves)
    
def grid_traveler(r, c, memo):
    n = str(r) + "," + str(c)
    if n in memo:
        return memo[n]
    if (r == 0) or (c == 0):
        return 0
    elif (r == 1) and (c == 1):
        return 1
    else:
        memo[n] = grid_traveler((r-1), c, memo) + grid_traveler(r, (c-1), memo)
        return memo[n]
    
main()
