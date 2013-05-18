from BeautifulSoup import BeautifulSoup
from pprint import pprint

# Data from  http://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films
# Alternative data source http://awardsdatabase.oscars.org/ampas_awards/DisplayMain.jsp?curTime=1368749378221 http://scrapy.org/

file = 'oscars.html'
handler = open(file).read()
soup = BeautifulSoup(handler)

film_list = []
for row in soup.findAll('tr'):
    try:
        links = row.findAll('a')
        cells = row.findAll('td')
        film = {
            'name': links[0].contents,
            'year': links[1].contents,
            'awards': cells[2].contents,
            'nominations': cells[3].contents
        }
        film_list.append(film)
    except:
        pass

pprint(film_list)
