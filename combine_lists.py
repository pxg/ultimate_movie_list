import sys
from BeautifulSoup import BeautifulSoup
from decimal import Decimal
from pprint import pprint


def get_oscars_list():
    """
    Read the oscars file and return a list of dicts
    """
    file = 'oscars.html'
    handler = open(file).read()
    soup = BeautifulSoup(handler)
    film_list = []

    for row in soup.findAll('tr'):
        #TODO: add more elegant check instead of dirty try catch
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
    return film_list


def get_imdb_list():
    """
    Read the imdb file and return a list of dicts
    """
    list_file = 'imdb.txt'
    name_column = 26
    f = open(list_file, 'r')
    film_list = []
    pos = 0

    for line in f:
        pos += 1
        words = line.split()
        film = {'pos': pos, 'score': Decimal(words[2]), 'name': line[name_column:-1]}
        film_list.append(film)
    f.close()
    return film_list


def get_bfi_list():
    """
    Read the bfi file and return a list of dicts
    """
    list_file = 'bfi_sight_and_sound_2012.txt'
    f = open(list_file, 'r')
    film_list = []

    for line in f:
        words = line.split('    ')
        #NOTE: pos is not the position in the pyton list but in the original
        # list so is not always an integer due to joint places
        film = {'pos': words[0], 'name': words[1][:-1]}
        film_list.append(film)
    f.close()
    return film_list


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


#TODO: just accept a list of lists and combine so we don't have to keep adding
# new parameters for the function
def combine_lists(bfi_list, imdb_list):
    """
    Combine the lists and order by the score
    """
    combined_list = bfi_list + imdb_list
    #NOTE: do we need to deal with duplicates here? (could manually fix bfi)
    combined_list = sorted(combined_list, key=lambda k: k['score'])
    combined_list.reverse()
    return combined_list

bfi_list = calc_bfi_scores(bfi_list, imdb_list)
combined_list = combine_lists(bfi_list, imdb_list)

pos = 0
for film in combined_list:
    pos += 1
    print '%s %s. Score %s' % (pos, film['name'], film['score'])
