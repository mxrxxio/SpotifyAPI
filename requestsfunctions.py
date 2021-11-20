import requests, os
from dotenv import load_dotenv
import json

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json() # request to JSON
access_token = auth_response_data['access_token'] # save the access token

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'
RADIOHEAD = '4Z8W4fKeB5YxbusRsdQVPb'
LED_ZEPPELIN = '36QJpDe2go2KgaRleHCDTp'

def test_artist(artist_id, BASE_URL_SPOTIFY, header):
    r = requests.get(BASE_URL_SPOTIFY + 'artists/' + artist_id + '/albums', 
                 headers=header, 
                 params={'include_groups': 'album', 'limit': 50})
    return r.json()

def print_albums(artist_json):
    for album in artist_json['items']:
        print(album['name'], ' - - ', album['release_date'])