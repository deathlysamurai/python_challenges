vowels = "aeiou"
letters = []
again = "yes"
while again == "yes":
    word = input("Enter word: ")
    while not word.isalpha():
        print("Please enter a word.")
    for letter in word:
        letters.append(letter)
    consonants = 0
    for index in range(len(letters)):
        if letters[index].lower() not in vowels:
            consonants += 1
        elif letters[index].lower() in vowels:
            if index == 0:
                letters.append("y")
                letters.append("a")
                letters.append("y")
                break
            elif index > 0:
                for index in range(consonants):
                    letters.append(letters[index])
                del letters[0:consonants]
                letters.append("a")
                letters.append("y")
                break
    for letter in letters:
        print(letter, end="")
    del letters[0:len(letters)]
    again = input("\nWould you like to enter another word? yes or no.\n")
    while (again != "yes") and (again != "no"):
        again = input("Please enter yes or no.\n")
