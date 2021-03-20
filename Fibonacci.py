#time complexity = 0(2^N)

fibonacci = []
total_numbers = int(input("Total numbers: "))
while total_numbers <= 0:
        total_numbers = int(input("Please enter a positive number.\n"))
for n in range(total_numbers):
    if n <= 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[n-1] + fibonacci[n-2])
for item in fibonacci:
    print(str(item), end=" ")