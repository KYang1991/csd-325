import requests
import json

# PokéAPI URL from the course reading
url = "https://pokeapi.co/api/v2/generation/?limit=2"

try:
    # Test the API connection
    response = requests.get(url, timeout=10)
    print("Connection Status:", response.status_code)

    response.raise_for_status()

    # Display the original response without formatting
    print("\nOriginal API Response:")
    print(response.text)

    # Convert the response into JSON data
    data = response.json()

    # Display the response with formatting
    print("\nFormatted API Response:")
    print(json.dumps(data, indent=4))

    # Display the Pokémon generation information
    print("\nPokemon Generations:")

    for generation in data["results"]:
        print("Generation:", generation["name"])
        print("URL:", generation["url"])
        print()

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
except (ValueError, KeyError, TypeError) as error:
    print("Unable to process the response:", error)