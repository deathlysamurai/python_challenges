#time complexity = 0(2^N)

def main():
    total_numbers = int(input("Total numbers: "))
    while total_numbers <= 0:
        total_numbers = int(input("Please enter a positive number.\n"))
    for number in range(total_numbers):
        print(recursive_fibonacci(number), end=" ")
        
def recursive_fibonacci(n):
    if n <= 1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
        
main()