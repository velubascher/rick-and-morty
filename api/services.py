import requests
from .constants import API_URL

def get_episodes():
    data = requests.get('{}/episode/'.format(API_URL)).json()
    episodes = pagination(data)
    return episodes

def get_episode(id):
    data = requests.get('{}/episode/{}'.format(API_URL, id)).json()
    characters_id = []
    for url in data['characters']:
        _id = url.rsplit('/', 1).pop()
        characters_id.append(int(_id))
    characters = get_characters(str(characters_id))

    episode = {
        'name': data['name'],
        'air_date': data['air_date'],
        'episode': data['episode'],
        'characters': characters
        }
    return episode

def get_characters(id_list):
    data = requests.get('{}/character/{}'.format(API_URL, id_list)).json()
    return data

def get_character(id):
    data = requests.get('{}/character/{}'.format(API_URL, id)).json()
    episodes_id = []
    for url in data['episode']:
        _id = url.rsplit('/', 1).pop()
        episodes_id.append(int(_id))
    episodes = requests.get('{}/episode/{}'.format(API_URL, str(episodes_id))).json()
    data['episodes'] = episodes
    data['location']['id'] = data['location']['url'].rsplit('/', 1).pop() if data['location']['url'] else ""
    data['origin']['id'] = data['origin']['url'].rsplit('/', 1).pop() if data['origin']['url'] else ""
    return data

def get_location(id):
    data = requests.get('{}/location/{}'.format(API_URL, id)).json()
    characters_id = list(map(lambda url: int(url.rsplit('/', 1).pop()), data['residents']))
    characters = get_characters(characters_id) if characters_id else []
    data['characters'] = characters
    return data

def make_search(term):
    characters = requests.get('{}/character/?name={}'.format(API_URL, term)).json()
    print(characters)
    locations = requests.get('{}/location/?name={}'.format(API_URL, term)).json()
    episodes = requests.get('{}/episode/?name={}'.format(API_URL, term)).json()
    results = {'characters': pagination(characters), 'locations': pagination(locations), 'episodes': pagination(episodes)}
    results['total'] = sum(len(i) for i in results.values())
    results['term'] = term
    return results

def pagination(object):
    if 'error' in object.keys():
        return []

    results = object['results']
    _next = object['info']['next']
    while _next:
        data = requests.get(_next).json()
        results.extend(data['results'])
        _next = data['info']['next']
    return results