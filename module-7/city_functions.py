
# CSD-325 Module 7 - Test Cases
# City and Country Function

def city_country(city, country):
    """Return a city and country in a formatted string."""
    location = f"{city}, {country}"
    return location.title()


# Call the function three times
print(city_country("santiago", "chile"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))
