import sys
from pprint import pprint
from decimal import Decimal


# TODO: have extra function for reading the lines into a list
def get_imdb_list():
    """
    Read the imdb file and return a list of dicts
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
        film = {'pos': pos, 'score': Decimal(words[2]), 'name': line[name_column:-1]}
        list.append(film)
    f.close()
    return list


def get_bfi_list():
    """
    Read the bfi file and return a list of dicts
    """
    list_file = 'bfi_sight_and_sound_2012.txt'
    f = open(list_file, 'r')
    list = []

    for line in f:
        words = line.split('    ')
        #NOTE: pos is not the position in the pyton list but in the original
        # list so is not always an integer due to joint places
        film = {'pos': words[0], 'name': words[1][:-1]}
        list.append(film)
    f.close()
    return list


def calc_bfi_scores(bfi_list, imdb_list):
    """
    Calculate the BFI scores from their position and the IMDB scores
    """
    num_scores = len(bfi_list)
    best_score = imdb_list[0]['score']
    worst_score = imdb_list[num_scores]['score']
    score_interval = (best_score - worst_score) / num_scores
    score = best_score

    for film in bfi_list:
        film['score'] = score
        score -= score_interval
    return bfi_list

imdb_list = get_imdb_list()
bfi_list = get_bfi_list()
# calc scores for the bfi_list based of the imdb_list scores
bfi_list = calc_bfi_scores(bfi_list, imdb_list)
pprint(bfi_list)
#pprint(imdb_list)

# calculate points for each movie:
# - get weight for each lists
# - place_points = invert place?
# - points = weight * place_points
# - combine the lists
