import random
import json
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
list_quote_info = []
categories = set()
#URLS NEEDED
API_WIKI = 'http://fr.wikiquote.org/w/api.php?action='
WIKI_QUERY = (
    '{api}query&continue=-||&cmcontinue={cmcontinue}'
    '&list=categorymembers&format=json&cmtitle={page}&cmtype={command}')
WIKI_PARSE = '{api}parse&format=json&page={page}&prop=text'

def json_from_url(url):
    'Stolen from python-wikiquote'
    res = urllib.request.urlopen(url)
    body = res.read().decode()
    return json.loads(body)


def category_members(category, command='subcat'):
    'Function used to list all member of a category (subcategory xor page)'
    category = urllib.parse.quote(category)
    page = WIKI_QUERY.format(api=API_WIKI,
                             cmcontinue='{cmcontinue}',
                             page=category,
                             command=command)
    cmcontinue = ''
    while_end = True
    while while_end:
        # Wikiquote doesn't give you al member, you need to ask for the next page
        current_page = page.format(cmcontinue=cmcontinue)
        my_json = json_from_url(current_page)
        try:
            cmcontinue = my_json['continue']['cmcontinue']
        except KeyError:
            while_end = False
        for item in my_json['query']['categorymembers']:
            yield item['title']

#Get all quote of a page
def get_quotes_page(page):
    page = urllib.parse.quote(page)
    url = WIKI_PARSE.format(api=API_WIKI, page=page)
    my_json = json_from_url(url)
    soup = BeautifulSoup(my_json['parse']['text']['*'])
    spans = soup.find_all('span')
    citations = [{'span': span, 'vf': span.text}
                 for span in spans
                 if 'class' in span.attrs and 'citation' in span['class']]
    #get english
    for citation in citations:
        try:
            citation['vo'] = next(
                span.text for span in list(
                    citation['span'].parent.next_siblings)[1].find_all('span')
                if 'class' in span.attrs and 'original' in span['class'])
        except IndexError:
            pass
        except StopIteration:
            pass
    return citations

def get_quote(page,number):
    quote = get_quotes_page(page)[number]
    return quote




def explore_category(category):
    #Do this at the start of the program
    subs = set(category_members(category, command='subcat'))
    new_categories = set(sub for sub in subs if sub not in categories)
    for sub in new_categories:
        explore_category(sub)
    categories.update(new_categories)
    pages = set(category_members(category, command='page'))
    for page in pages:
        for index, quote in enumerate(get_quotes_page(page)):
            list_quote_info.append({'path': page, 'id': index})


def random_quote():
    my_id = random.randint(0, len(list_quote_info))
    page = list_quote_info[my_id]['path']
    quote = get_quote(page,list_quote_info[my_id]['id'])
    return quote, page


if __name__ == '__main__':
    #print(set(category_members(urllib.parse.quote('Catégorie:Kaamelott'))))
    #print(set(category_members(urllib.parse.quote('Catégorie:Kaamelott'),
                               #command='page')))
    explore_category('Catégorie:Film')
    explore_category('Catégorie:Anime')
    explore_category('Catégorie:Série télévisée')


    print(random_quote())
