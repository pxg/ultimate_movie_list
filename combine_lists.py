import sys
from pprint import pprint

# TODO: have extra function for reading the lines into a list
def get_imdb_list():
    """
    Read the imdb file and return a list
    """
    #TODO: read the whole file and just get the line we want
    list_file = 'imdb.txt'
    name_column = 26
    f = open(list_file, 'r')
    list = []
    pos = 0

    for line in f:
        pos += 1
        words = line.split()
        film = {'pos': pos, 'score': words[2], 'name': line[name_column:-1]}
        list.append(film)
    f.close()
    return list

def get_bfi_list():
    """
    Read the imdb file and return a list
    """
    list_file = 'bfi_sight_and_sound_2012.txt'
    f = open(list_file, 'r')
    list = []
    for line in f:
        words = line.split('    ')
        film = {'pos': words[0], 'name': words[1][:-1]}
        list.append(film)
    f.close()
    return list


imdb_list = get_imdb_list()
bfi_list = get_bfi_list()
#calc scores for the bfi_list based of the imdb_list scores
#bfi_list = calc_scores(bfi_list, imdb_list)

pprint(bfi_list)
#pprint(imdb_list)

# calculate points for each movie:
# - get weight for each lists
# - place_points = invert place?
# - points = weight * place_points
# - combine the lists
