import requests

def get_episodes():
    data = requests.get('https://rickandmortyapi.com/api/episode/').json()
    episodes = data['results']
    pages = data['info']['pages']
    for page in range(2, pages + 1):
        data = requests.get('https://rickandmortyapi.com/api/episode?page={}'.format(page)).json()
        episodes.extend(data['results'])
    return episodes
