import requests
import json

# Open Notify API from the course reading
url = "http://api.open-notify.org/astros.json"

try:
    # Test the connection
    response = requests.get(url, timeout=10)
    print("Connection Status:", response.status_code)

    response.raise_for_status()

    # Display the original response
    print("\nOriginal API Response:")
    print(response.text)

    # Format the JSON response
    data = response.json()

    print("\nFormatted API Response:")
    print(json.dumps(data, indent=4))

    # Display the astronaut information
    print("\nAstronauts Currently in Space:")

    for astronaut in data["people"]:
        print("Name:", astronaut["name"])
        print("Spacecraft:", astronaut["craft"])
        print()

    print("Total Astronauts:", data["number"])

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
except (ValueError, KeyError, TypeError) as error:
    print("Unable to process the response:", error)