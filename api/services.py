import requests

def get_episodes():
    data = requests.get('https://rickandmortyapi.com/api/episode/').json()
    episodes = data['results']
    pages = data['info']['pages']
    for page in range(2, pages + 1):
        data = requests.get('https://rickandmortyapi.com/api/episode?page={}'.format(page)).json()
        episodes.extend(data['results'])
    return episodes

def get_episode(id):
    data = requests.get('https://rickandmortyapi.com/api/episode/{}'.format(id)).json()
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
    data = requests.get('https://rickandmortyapi.com/api/character/{}'.format(id_list)).json()
    return data

def get_character(id):
    data = requests.get('https://rickandmortyapi.com/api/character/{}'.format(id)).json()
    episodes_id = []
    for url in data['episode']:
        _id = url.rsplit('/', 1).pop()
        episodes_id.append(int(_id))
    episodes = requests.get('https://rickandmortyapi.com/api/episode/{}'.format(str(episodes_id))).json()
    data['episodes'] = episodes
    data['location']['id'] = data['location']['url'].rsplit('/', 1).pop()
    data['origin']['id'] = data['origin']['url'].rsplit('/', 1).pop()
    return data

def get_location(id):
    data = requests.get('https://rickandmortyapi.com/api/location/{}'.format(id)).json()
    characters_id = list(map(lambda url: int(url.rsplit('/', 1).pop()), data['residents']))
    characters = get_characters(characters_id)
    data['characters'] = characters
    return data
