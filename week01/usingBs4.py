import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

movieList = []

def getMovieInfo(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108'
    header = {'user-agent':user_agent}

    response = requests.get(url,headers=header)
    bs_info = bs(response.text, 'html.parser')

    for info in bs_info.find_all('div', attrs={'class': 'classic-movie'}):
        name = info.find('div', attrs={'class': 'title'}).text
        classic = info.find('div', attrs={'class': 'actors'}).text
        date = info.find('div', attrs={'class': 'show-info'}).text
        movieList.append([name, classic, date])


# print(response.text)
# print('===========')
# print(filmList)

myurls = tuple(f'https://m.maoyan.com/ajax/moreClassicList?sortId=1&showType=3&limit=5&offset={ num * 5 }&optimus_uuid=08611400B95511EA97E61368F9F12EB0B674A282971E456585A998518150437C&optimus_risk_level=71&optimus_code=10' for num in range(2))

from time import sleep

for page in myurls:
    getMovieInfo(page)
    sleep(5)

# print(movieList)
movieFile = pd.DataFrame(data = movieList)
movieFile.to_csv('./movieFile_bs4.csv', encoding='utf8', index=False, header=False)