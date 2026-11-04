"""
Lab 2.1 – Simple Datasets and Aggregates
Practice lists, dictionaries and tuples by computing simple aggregates.

>>> average([1, 2, 3])
2.0
>>> average([])
0.0
>>> largest_city({"Riga": 600, "Liepaja": 60})
('Riga', 600)
>>> smallest_city({"Riga": 600, "Liepaja": 60})
('Liepaja', 60)
>>> total_population({"Riga": 600, "Liepaja": 60})
660
>>> largest_city({})
('', 0)
>>> smallest_city({})
('', 0)
"""


def average(values: list[float]) -> float:
    """Return the average of values, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the largest population."""
    if not populations:
        return ("", 0)
    city = max(populations, key=populations.get)
    return (city, populations[city])


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the smallest population."""
    if not populations:
        return ("", 0)
    city = min(populations, key=populations.get)
    return (city, populations[city])


def total_population(populations: dict[str, int]) -> int:
    """Return the sum of all populations."""
    return sum(populations.values())


if __name__ == "__main__":
    temperatures = [3.5, 4.0, 5.5, 2.0, 6.5, 3.0, 5.0]

    city_population = {
        "Riga": 605000,
        "Daugavpils": 78000,
        "Liepaja": 67000,
        "Jelgava": 55000,
        "Jurmala": 50000,
    }

    print(f"Average temperature: {average(temperatures):.1f}")

    largest = largest_city(city_population)
    print(f"Largest city: {largest[0]} - {largest[1]}")

    smallest = smallest_city(city_population)
    print(f"Smallest city: {smallest[0]} - {smallest[1]}")

    print(f"Total population: {total_population(city_population)}")
