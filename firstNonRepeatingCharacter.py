#firstNonRepeatingCharacter

input = input("What word would you like to test?\n")

def firstNonRepeatingCharacter():

    dict = {}
    for letter in input:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
        

    for letter in dict:
        if dict[letter] == 1:
            return letter
        
    return "_"

def main():
    
    print(firstNonRepeatingCharacter())
    
main()
    