import collections
from ordered_set import OrderedSet


def cities_without_gas(
        cities: list[str], gas_stores: list[str], active_pipes: list[list[str]]
) -> list[list[str, list[str]]]:
    city_stores = {}
    cities_in_set = OrderedSet(
        cities
    )  # I use set for complexity of operation differance O(num_of_elem)
    # complexity = O(cities)
    result = []
    for city in cities + gas_stores:
        city_stores[city] = []
    # complexity = O(2 * cities + gas_stores)

    for [source_city, entry_city] in active_pipes:
        city_stores[source_city].append(entry_city)
    # complexity = O(2 * cities + gas_stores + active_pipes)

    for store in gas_stores:
        city_to_visit = collections.deque(
            city_stores[store]
        )  # I use deque for complexity popleft O(1) and extend O(k)
        visited_city = (
            set()
        )  # I use set for complexity of operation \\ x in y // be O(1)
        while city_to_visit:
            city = city_to_visit.popleft()
            if city not in visited_city:
                visited_city.add(city)
                city_to_visit.extend(city_stores[city])
        inaccessible_cities = (
                cities_in_set - visited_city
        )  # O(cities) -> difference of sets
        result.append(
            [store, list(inaccessible_cities)]
        )
    # complexity = O(2 * cities + gas_stores + active_pipes + gas_stores * (visited_city + 2 * cities))
    return result
