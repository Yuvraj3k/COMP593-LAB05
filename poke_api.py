'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")

    print(poke_info)
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    pokemon_name = str(pokemon_name).strip().lower()
    
    pokemon_url = POKE_API_URL + pokemon_name

    try:
        # Send GET request to API and parse response
        response = requests.get(pokemon_url)
        response.raise_for_status()  # Raise an exception for HTTP errors 

        # If successful, return JSON data as a dictionary
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
    
    return None  # Return None if exception occurs

if __name__ == '__main__':
    main()
