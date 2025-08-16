def format_city(city, country, population=None):
    if population:
        formatted_city = f'{city.title()}, {country.title()} - population {population}'
    else:
        formatted_city = f'{city.title()}, {country.title()}'
    return formatted_city