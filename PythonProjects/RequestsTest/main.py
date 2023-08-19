import requests
token = '51d1d32d17927883c7e8bdd99d488c8a' # токен тренера
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов

response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {    # тренер уже создан
    "trainer_token": token,
    "email": "nasimasarsekenova@qastudio.me",
    "password": "Capricorn3488"
}, headers = {'Content-Type' : 'application/json'})

print(response.text)
print (response.status_code)

response_activation = requests.post(f'{host}/trainers/confirm_email', json = {     #активация прошла
    "trainer_token": token
}, headers = {'Content-Type' : 'application/json'})

print(response_activation.text)
print (response.status_code)

'''if response.status_code == 200:
    print('OK!')
else:
    print('Not OK!')'''

response_change_trainer = requests.put(f'{host}/trainers', json =  {
    "name": "Ash",
    "city": "California"
}, headers = {'Content-Type' : 'application/json', 
              'trainer_token': token})

print(response_change_trainer.text)

response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Shadow",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_add_pokemon.text)

response_change_pokemon = requests.put(f'{host}/pokemons', json =  {
    "pokemon_id": "1820",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_change_pokemon.text)

response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6294"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_add_pokemon.text)

'''if response.status_code ==200:
    print('OK!')
else:
    print('Not OK!')'''