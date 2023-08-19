import requests
import pytest

token = '51d1d32d17927883c7e8bdd99d488c8a' # токен тренера
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': 1339})
    assert response.status_code == 200