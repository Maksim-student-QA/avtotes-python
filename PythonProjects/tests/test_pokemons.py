import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b4ac10c994145580f13c4327598a62b2'
HEADER = {'content-type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '4202' 

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'),('trainer_id', TRAINER_ID),('id', '42359')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value