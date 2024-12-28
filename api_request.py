import requests


str_base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(str_name):
    print(f"{str_base_url}/pokemon/{str_name}")
    str_url = f"{str_base_url}/pokemon/{str_name}"
    # calling get api to retrive data
    response = requests.get(str_url)
    print(response)
    
    if response.status_code == 200:
        print("Data retrived")
        print(response.json())
        return response.json()
    else:
        print(f"Failed to retrive data {response.status_code}")
        
    
    
    
    
    
str_name = "pikachu"
dict_pokemon = get_pokemon_info(str_name)

if dict_pokemon:
    print(dict_pokemon["name"])
    print(dict_pokemon["id"])
    print(dict_pokemon["height"])
    print(dict_pokemon["weight"])
