from string import ascii_lowercase as smallLetters
from string import ascii_uppercase as bigLetters

def verifyInput(userInput):
    if userInput == '1' or userInput == '2' or userInput == '3':
        return True
    return False

def primaryLoop():
    print("What would you like to do?")
    print("1. Encode a statement")
    print("2. Decode a statement (must have key ready to enter)")
    print("3. Print all possible decoded statements associated with an \
    encoded statement")
    command = raw_input("Please enter a number associated with \
    one of the above: ")
    if(veryifyInput(command)):
        if command == '4':
            print("Thanks for using the program. Have a good day!")
            exit()
        elif command == '1':
            rotationKey = raw_input("Please enter the key associated with this\
            cipher: ")
            statement
    else:
        print("You entered an invalid input")

def main():
    print("Welcome to Trey's Caesar Cipher program.\n")
    while(True):
        primaryLoop()

if __name__== "__main__":
  main()
