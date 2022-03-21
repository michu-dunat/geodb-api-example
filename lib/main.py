from geodb_lib import geodb_handler

if __name__ == '__main__':
    handler = geodb_handler.GeodbHandler()
    #print(handler.get_city_time("Q61"))
    #print(handler.get_city_population("Q61"))
    #print(handler.get_city_count_in_region_with_min_population("Q36", "Q54181", 130000))
    #print(handler.get_city_details("Q60"))
    print(handler.get_distance_between_tychy_and_city("Q60"))

