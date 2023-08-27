import pandas as pd

city_region_map = {
    "Portland": "NORAM",
    "Toronto": "NORAM",
    "New York City": "NORAM",
    "Mexico City": "NORAM",
    "Buenos Aires": "LATAM",
    "Santiago": "LATAM",
    "Bogota": "LATAM",
    "Rio de Janeiro": "LATAM",
    "Amsterdam": "EUROPE",
    "Seville": "EUROPE",
    "Nantes": "EUROPE",
    "Warsaw": "EUROPE",
    "Nairobi": "MEA",
    "Johannesburg": "MEA",
    "Marrakech": "MEA",
    "Konya": "MEA",
    "Tokyo": "APAC",
    "Bangalore": "APAC",
    "Melbourne": "APAC",
    "Hangzhou": "APAC",
}


def get_region_from_city(i: pd.Index):
    city_vals = i.values
    region = [city_region_map[c] for c in city_vals]
    return region