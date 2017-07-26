import requests
from pylab import show
from bs4 import BeautifulSoup
res = requests.get('https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E4%BB%A5%E5%A4%AA%E5%9D%8A/usd/30%E5%A4%A9')
soup = BeautifulSoup(res.text, 'html.parser')

data_prices = soup.select('#coin_30d_historical_price_chart')[0].prettify('utf-8').decode('utf-8')

import re
m = re.search('<div data-prices="(.*?)"', data_prices)

import json
jd = json.loads(m.group(1))
#jd


import pandas
df = pandas.DataFrame(jd)
#df

df.columns = ['datetime', 'USD']

df['datetime'] = pandas.to_datetime(df['datetime'], unit='ms')

#df.head()

df.index = df['datetime']

df['USD'].plot(kind = 'line', figsize = [10,5])

show()