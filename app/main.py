from geodb_lib import geodb_handler
import sys


if __name__ == '__main__':
    handler = geodb_handler.GeodbHandler(sys.argv[1])
    print("Hello, here's a demonstration of the sample capabilities of the GeoDB API.")
    while True:
        key_pressed = input("What do you want to do?"
                            "\n   1. Check the time in a particular city."
                            "\n   2. Check the population of a given city."
                            "\n   3. Check the number of cities in a region of a country with a population greater than the specified population."
                            "\n   4. Check the information about a particular city."
                            "\n   5. Check the distance between Tychy and the given city."
                            "\n   0. Exit."
                            "\n")
        if key_pressed == '1':
            time = handler.get_city_time(input("Enter the city code: "))
            print(f"\nIt's {time}!\n")
        elif key_pressed == '2':
            population = handler.get_city_population(input("Enter the city code: "))
            print(f"\n{population} people live there!\n")
        elif key_pressed == '3':
            try:
                handler.get_city_count_in_region_with_min_population("Q36", "Q54181", 100000)
                country_code = input("Enter the country code: ")
                region_code = input("Enter the region code: ")
                min_population = input("Enter minimal population: ")
                count = handler.get_city_count_in_region_with_min_population(country_code, region_code, min_population)
                print(f"\nThere are {count} cities with population over {min_population}!\n")
            except AttributeError:
                print("\nUpgrade GeoDB API Consume library!\n")
        elif key_pressed == '4':
            try:
                city = handler.get_city_details(input("Enter the city code: "))
                print(f"\n{city}\n")
            except AttributeError:
                print("\nUpgrade GeoDB API Consume library!\n")
        elif key_pressed == '5':
            try:
                distance = handler.get_distance_between_tychy_and_city(input("Enter the city code: "))
                print(f"\nThis city is located {distance} km from Tychy.\n")
            except AttributeError:
                print("\nUpgrade GeoDB API Consume library!\n")
        elif key_pressed == '0':
            print("See ya!")
            break
        else:
            print("Select the correct option!")

