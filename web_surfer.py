import bs4 as bs
import urllib.request

sause = urllib.request.urlopen('https://en.wikipedia.org/wiki/Carbon').read()
#print(sause)
bsoup = bs.BeautifulSoup(sause,'lxml')
print(bsoup.find_all('p'))
