from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date


def get_topic_page(topic, page_number=1):
    topic_with_page = topic + '/page=' + str(page_number)
    response = requests.get(topic)
    if not response.ok:
        print('Status code:', response.status_code)
        raise Exception('Failed to fetch web page' + topic)

    return BeautifulSoup(response.text, features="html.parser")


# get the date array first for the last year
day_count = 365
dates = []
for i in range(day_count, 0, -1):
    dates.append((date.today() + relativedelta(days=-day_count)).strftime('%Y%m%d'))

# historical daturl format: https://coinmarketcap.com/historical/20210103/

url_base = "https://coinmarketcap.com/historical/"
url = url_base+dates[0]+'/'
content = requests.get(url).content
soup = BeautifulSoup(content,'html.parser')
doc = get_topic_page(url)

tr_tags = doc.tbody.find_all('tr')
td_tags = tr_tags[0].find_all('td')
print(td_tags[0].div.text)   # 0: rank 2: symbol, 3: market cap
# tr_tags indices give the nth crypto
# td_tags indices give the info about the selected crypto
