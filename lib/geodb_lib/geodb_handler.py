import requests
import json
from geodb_lib import city


class GeodbHandler:

    def __init__(self, token):
        self.headers = {
            'x-rapidapi-key': token,
            'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }

    def get_city_time(self, city_code):
        url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities/{city_code}/time"
        response = requests.request("GET", url, headers=self.headers)

        data = json.loads(response.text)
        time = data['data'][:8]

        return time

    def get_city_population(self, city_code):
        url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities/{city_code}"
        response = requests.request("GET", url, headers=self.headers)

        data = json.loads(response.text)
        population = data['data']['population']

        return population

    def get_city_count_in_region_with_min_population(self, country_code, region_code, min_population):
        url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/countries/{country_code}/regions/{region_code}/cities"
        querystring = {"minPopulation": f"{min_population}"}
        response = requests.request("GET", url, headers=self.headers, params=querystring)

        data = json.loads(response.text)
        count = data['metadata']['totalCount']

        return count

    def get_city_details(self, city_code):
        url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities/{city_code}"
        response = requests.request("GET", url, headers=self.headers)

        data = json.loads(response.text)
        city_object = city.City(data['data']['name'], data['data']['country'], data['data']['region'],
                                data['data']['latitude'], data['data']['longitude'],
                                data['data']['population'], data['data']['timezone'])

        return city_object

    def get_distance_between_tychy_and_city(self, city_code):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q11977/distance"
        querystring = {"fromCityId": f"{city_code}", "distanceUnit": "KM"}
        response = requests.request("GET", url, headers=self.headers, params=querystring)

        data = json.loads(response.text)
        distance = data['data']

        return distance
