def printMenu():
    print("")
    print("1. Generate list")
    print("2. Test your knowledge")
    print("3. Quit")

    userResponse = int(input("What do you want to do? "))
    return userResponse


def main():
    url = "https://pokeapi.co/"
    print("Welcome to the Pokemon List Generator Program!")

    userResponse = printMenu()

    while userResponse != 3:

        if userResponse == 1: #generate list
            print("Generating list")
        elif userResponse == 2: #test your knowledge
            print("Are you ready to test your knowledge?")
            print("Let's go")
        else:
            print("That's an incorrect option")

        continueVar = input("\n Do you want to go again? (y/n) ")
        if continueVar.lower() == "y":
            userResponse = printMenu()
        elif continueVar.lower() == "n":
            userResponse = 3
        else:
            print("That's an incorrect option")

    print("\nThank you for playing!\n")

if __name__ == "__main__":
    main()

# generate list -> ask for specifications and make API calls 
    #to generate list of pokemon matching user's specs
# test knowledge -> get a category of pokemon then the user types
    # as many pokemon they know and program tests to see if correct
    # or not and shows them which ones they got right
# maybe add a two player mode of testing knowledge for who can get the most
