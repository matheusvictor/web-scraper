from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    # html = urlopen('http://pythonscraping.com/pages/page1.html')
    html = urlopen('http://pythonscraping-thisurldoesnotexist.com/')
except HTTPError as e:
    print(e)
except URLError as e:
    print('This server could not be found!')
else:
    print('It worked!')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
