# This program makes HHTP GET request in order to retrieve information about countries. 
# The task is to pull counties based on a specific filter (country name) and then sum up coutries' popultaion for countries which area is equal or
# greater than N square km.
# The response is in JSON format. Country name is in 'name' field. Area is in 'area' field.
# The URL is https://jsonmock.hackerrank.com/api/countries/search?name=<name>
# where 'name' can be equal to any string, for example name=uk:
# https://jsonmock.hackerrank.com/api/countries/search?name=uk
# The response can be paginated, thus to access next pages the following parameter should be used: &page=<n>.
# The number of total pages in stored in 'total_pages' field.
# For example, if total_pages field = 2 then to accees the second page the following url should be used: 
# https://jsonmock.hackerrank.com/api/countries/search?name=uk&page=2


import requests
import json

# this function performs HTTP GET request and returns the data from the response
def getRequest(URL):
    print URL

    PARAMS = {}
    r = requests.get(url = URL, params = PARAMS)
    js = r.json()

    return js

# this function retrieves the area and the population from the data
def getCountryPopulation(js, area):

    total_population = 0

    if 'data' in js:
        
        data = js['data']

        for d in data:
            res = ''
            if 'area' in d and 'population' in d:
                if d['area'] >= area:
                    res = '-=Selected=-'
                    total_population += d['population']
                print('Country: %s, Area: %s, Population: %s %s' % (d['name'], d['area'], d['population'], res))

    return total_population

def getTotalPopulation(s, area):

    URL = "https://jsonmock.hackerrank.com/api/countries/search?name=%s" % s

    js = getRequest(URL)

    total_population = 0
    total_pages = js['total_pages']
    print('Total pages: %s' % total_pages)

    total_population = getCountryPopulation(js, area)

    if total_pages > 1: # if there are multiple pages then iterate through them
        for p in range(2, total_pages + 1):
            URL = "https://jsonmock.hackerrank.com/api/countries/search?name=%s&page=%s" % (s, p)
            js = getRequest(URL)
            total_population += getCountryPopulation(js, area)

    return total_population

print('Total population: %s' % getTotalPopulation('un',100000))
