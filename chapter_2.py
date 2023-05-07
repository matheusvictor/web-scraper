from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('This server could not be found!')
else:
    print('It worked!')
    bs = BeautifulSoup(html.read(), 'html.parser')
    nameList = bs.findAll(name='span', attrs={'class': 'green'})

    for name in nameList:
        print(name.get_text())
