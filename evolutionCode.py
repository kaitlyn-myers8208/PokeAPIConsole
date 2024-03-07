import requests

def get_pokemon_evolution_chain(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        species_data = response.json()
        evolution_chain_url = species_data["evolution_chain"]["url"]
        return evolution_chain_url
    else:
        return None

def get_evolution_chain_details(evolution_chain_url):
    response = requests.get(evolution_chain_url)
    if response.status_code == 200:
        evolution_chain_data = response.json()
        return evolution_chain_data
    else:
        return None
    
def print_chain(chain, level=0):
    print("  " * level + "- " + chain["species"]["name"].capitalize())
    if chain["evolves_to"]:
        for evolve in chain["evolves_to"]:
            print_chain(evolve, level + 1)

pokemon_name = "pikachu"
evolution_chain_url = get_pokemon_evolution_chain(pokemon_name)
if evolution_chain_url:
    evolution_chain_data = get_evolution_chain_details(evolution_chain_url)
    if evolution_chain_data:
        chain = evolution_chain_data["chain"]
        print(f"{pokemon_name.capitalize()} evolves into:")
        print_chain(chain)
    else:
        print("Failed to get evolution chain details.")
else:
    print("Failed to get species data.")

