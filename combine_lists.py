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
            awards = int(cells[2].contents[0])

            # Filter only nominations
            if awards > 0:
                film = {
                    'name': links[0].contents[0],
                    'year': links[1].contents[0],
                    'awards': awards,
                    'nominations': cells[3].contents
                }
                film_list.append(film)
        except Exception, e:
            pass

    film_list = sorted(film_list, key=lambda k: k['awards'])
    film_list.reverse()
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
        #TODO: get list from name
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


def calc_scores(unscored_list, master_list):
    """
    Calculate the BFI scores from their position and the IMDB scores
    """
    num_scores = len(unscored_list)
    best_score = master_list[0]['score']
    worst_score = master_list[num_scores]['score']
    score_interval = (best_score - worst_score) / num_scores
    score = best_score

    for item in unscored_list:
        item['score'] = score
        score -= score_interval
    return unscored_list


#TODO? just accept a list of lists and combine so we don't have to keep adding
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

imdb_list = get_imdb_list()
bfi_list = get_bfi_list()
bfi_list = calc_scores(bfi_list, imdb_list)
oscars_list = get_oscars_list()
oscars_list = calc_scores(oscars_list, imdb_list)

pprint(oscars_list)
sys.exit()

combined_list = combine_lists(bfi_list, imdb_list)

pos = 0
for film in combined_list:
    pos += 1
    print '%s %s. Score %s' % (pos, film['name'], film['score'])
