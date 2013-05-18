from BeautifulSoup import BeautifulSoup

# use scrapy on http://awardsdatabase.oscars.org/ampas_awards/DisplayMain.jsp?curTime=1368749378221 http://scrapy.org/
# http://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films
#url = "http://weather.yahoo.com/"
file = 'oscars.html'
handler = open(file).read()
soup = BeautifulSoup(handler)
#print soup.prettify()

#soup.contents[0].name
#rows = soup.findAll('tr')
for link in soup.findAll('a'):
    #print link.contents[0]
    try:
        if link.contents[0].isdigit() is False:
            print link.contents
    except:
        pass
