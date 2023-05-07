from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/page3.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('This server could not be found!')
else:
    bs = BeautifulSoup(html.read(), 'html.parser')

    print('CHILDREN')
    for child in bs.find('table', {'id': 'giftList'}).children:
        print(child)

    print('descendant'.upper())
    for descendant in bs.find('table', {'id': 'giftList'}).descendants:
        print(descendant)
