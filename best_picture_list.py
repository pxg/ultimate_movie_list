from pprint import pprint

list_file = 'oscar_best_picture_list.txt'
f = open(list_file, 'r')
film_list = []

for line in f:
    words = line.split('-')
    film = {
        'year': words[0][:-1],
        'name': words[1][2:-2]
    }
    film_list.append(film)
f.close()

pprint(film_list)

# is film in existing list?
# yes add the awards number, increment score by 1
# no then add to the bottom of the list (how many nos?)
