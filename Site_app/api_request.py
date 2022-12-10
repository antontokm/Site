import requests
from .models import Driver

def add_drivers():
    Driver.objects.all().delete()
    url = "http://ergast.com/api/f1/2022/driverStandings.json"
    headers = {}
    r = requests.get(url, headers=headers)
    response_dict = r.json()
    list_score = response_dict['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    for i in range(len(list_score)):
        driver = Driver()
        driver.first_name = list_score[i]["Driver"]['givenName']
        driver.last_name = list_score[i]["Driver"]['familyName']
        driver.score = float(list_score[i]['points'])
        driver.save()
        # print('test2')

