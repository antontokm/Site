from bs4 import BeautifulSoup
import requests
from .models import Driver

def add_drivers(year):
    Driver.objects.filter(year = year).delete()
    url = f"https://www.f1news.ru/Championship/{year}/personpoints.shtml"
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
    )
    r = requests.get(url, headers=headers)
    page = BeautifulSoup(r.text,"html.parser")
    table = page.findAll(onmouseover="this.className='lineSelected';")
    drivers_score_list = [i.text.strip().replace("\xa0", " ").split("\n") for i in table]
    for driver_info in drivers_score_list:
        driver = Driver()
        driver.first_name = driver_info[0][driver_info[0].index(" "):driver_info[0].index(" ")+3]
        driver.last_name = driver_info[0][driver_info[0].index(" ")+3:].strip()
        driver.score = float(int(driver_info[2]))
        driver.year = year
        driver.save()