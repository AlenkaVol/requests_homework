import requests

list_superheroes = ['Hulk', 'Captain America', 'Thanos']


def most_intelligent_superhero(list_superheroes):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    superheroes = response.json()

    super_dict = {}
    for super in superheroes:
        name = super["name"]
        if name in list_superheroes:
            intelligence = super["powerstats"]["intelligence"]
            super_dict[name] = intelligence

    sorted_super_dict = {}
    sorted_super_keys = sorted(super_dict, key=super_dict.get, reverse=True)
    for key in sorted_super_keys:
        sorted_super_dict[key] = super_dict[key]

    name_top = list(sorted_super_dict.items())[0][0]
    intelligence_top = list(sorted_super_dict.items())[0][1]

    print(f'Самый умный супергерой: {name_top}. Его интеллект равен: {intelligence_top}.')


most_intelligent_superhero(list_superheroes)