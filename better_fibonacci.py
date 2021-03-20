#time complexity = 0(2^N)

#using memoization
memo = {}

def main():
    total_numbers = int(input("Total numbers: "))
    while total_numbers <= 0:
        total_numbers = int(input("Please enter a positive number.\n"))
    for number in range(total_numbers):
        print(fibonacci(number, memo), end=" ")
        
def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    else:
        memo[n] = fibonacci((n-1), memo) + fibonacci((n-2), memo)
        return memo[n]
        
main()