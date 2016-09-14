# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

url ='http://www.ziroom.com/z/nl/sub/z2.html'
wb_data = requests.get(url)
Soup = BeautifulSoup(wb_data.text,'lxml')
Strsoup =str(Soup)
rel = re.compile('href="(.*)" ')
for item in rel.finditer(Strsoup):
    print(item.group(1))