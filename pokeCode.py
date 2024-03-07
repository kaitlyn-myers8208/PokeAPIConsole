import requests
import json

TOP_API_URL = "https://pokeapi.co/api/v2/"

def printMenu():
    print("--Menu--")
    print("1. Generate list")
    print("2. Test your knowledge")
    print("3. Quit")

    userResponse = int(input("What do you want to do? "))
    return userResponse

def get_all_data(urls):
    results = []
    # url = "https://pokeapi.co/api/v2/evolution-chain/chain/"

    for url in urls:
        response = requests.get("{TOP_API_URL}/evolution-chain/chain/")
        if response.status_code == 200:
            print(response)
            data = response.json()
            data["name"].append(results)

    return results


def main():
    print("Welcome to the Pokemon List Generator Program!")

    userResponse = printMenu()

    while userResponse != 3:

        if userResponse == 1: #generate list
            print("What are the specs of you list? ")
            sortBy = input("  Evolution of a specific pokemon, generation, or type (evolution/generation/type) ")
            if sortBy == "evolution": #evolution of specific pokemon
                # pokemon = input("What pokemon do you want to see the evolutions of? ")
                # get_all_data(evolution-chain)
                response = requests.get("https://pokeapi.co/api/v2/evolution-chain/7/")
                if response.status_code == 200:
                    print(response.json()['chain', 'evolves_to'])
            elif sortBy == "generation": #generation
                generation = input("What generation do you want to generate a list of? ")
                print("Here's the first 20")
                more = input("Do you want to print the next 20? (y/n) ")
                if more == "y":
                    print("more")
                elif more == "n":
                    return
                else:
                    print("That's an incorrect response")
            elif sortBy == "type": #type
                type = input("What type do you want to generate a list of? ")
            else:
                print("That's an incorrect option")

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
    # to generate list of pokemon matching user's specs
    # possible specs -> evolution of specific pokemon, generation, type
    # https://pokeapi.co/api/v2/evolution-chain/chain/
    # https://pokeapi.co/api/v2/generation/pokemon_species/
    # https://pokeapi.co/api/v2/type/pokemon/pokemon/name
# test knowledge -> get a category of pokemon then the user types
    # as many pokemon they know and program tests to see if correct
    # or not and shows them which ones they got right
# maybe add a two player mode of testing knowledge for who can get the most
