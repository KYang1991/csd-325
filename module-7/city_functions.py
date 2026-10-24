
# CSD-325 Module 7 - Test Cases
# City, Country, Population, and Language

def city_country(city, country, population=None, language=None):
    """Return a formatted city, country, population, and language."""
    location = f"{city}, {country}"

    if population is not None:
        location += f" - population {population}"

    if language is not None:
        location += f", {language}"

    return location.title()


if __name__ == "__main__":
    # Call the function three times
    print(city_country("santiago", "chile", 5000000, "spanish"))
    print(city_country("paris", "france", 2100000, "french"))
    print(city_country("tokyo", "japan", 14000000, "japanese"))
