import requests
from .models import Driver

def add_drivers(year):
    Driver.objects.filter(year = year).delete()
    url = f"http://ergast.com/api/f1/{year}/driverStandings.json"
    headers = {}
    r = requests.get(url, headers=headers)
    response_dict = r.json()
    list_driver_info = response_dict['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    list_season = response_dict['MRData']['StandingsTable']['StandingsLists'][0]
    for i in range(len(list_driver_info)):
        driver = Driver()
        driver.first_name = list_driver_info[i]["Driver"]['givenName']
        driver.last_name = list_driver_info[i]["Driver"]['familyName']
        driver.score = float(list_driver_info[i]['points'])
        driver.year = list_season["season"]
        driver.save()
        # print('test2')

