#firstDuplicate
#values must be between 1 - N, where N is length of the array
#must find first completed duplicate, so first time you find a second number
#[1,2,1,2,3,3] = 1 | [2,1,3,5,3,2] = 3 | [1,2,3,4,5,6] = -1

input = [2, 1, 3, 5, 3, 2]

def firstDuplicate():

    seen = []
    for number in input:
        if number < 1 or number > len(input):
            return "invalid array, values must be between 1 and N, where N is the length of the array"
        if number in seen:
            return number
        else:
            seen.append(number)
            
    return -1
            
def main():
    
    print(firstDuplicate())
    
main()
