import requests
from .models import Driver

def add_drivers():
    url = "http://ergast.com/api/f1/2022/driverStandings.json"
    headers = {}
    r = requests.get(url, headers=headers)
    response_dict = r.json()
    list_score = response_dict['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    drivers_count = Driver.objects.count()
    if len(list_score)!= drivers_count:
        for i in range(len(list_score)):
            driver = Driver()
            driverIndex = list_score[i]
            driver.first_name = driverIndex["Driver"]['givenName']
            driver.last_name = driverIndex["Driver"]['familyName']
            driver.score = float(driverIndex['points'])
            driver.save()
            print('test2')

