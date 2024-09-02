import requests

API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhiM2YzZjhhLWI4YzYtNGZmOC05ZGQ2LWE5MDQ2ODFlYmQ4NSIsImlhdCI6MTcxNzQxMjc3MCwic3ViIjoiZGV2ZWxvcGVyLzY4ZDFjODkzLWFjNWYtNWI0My05NTA1LTFmODhjZjI0MWM4NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTgxLjEwLjMxLjExNCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.z6abHS-SLjSLecHB1-Eb4WId79cr7V7GDl1uin_mN9PUmzIYozijKUns6Fj1LPC-vwsCtkqzzc6RQQY_K7rE6A'
BASE_URL = 'https://api.brawlstars.com/v1/brawlers'

def fetch_brawler_data(brawler_name):
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code == 200:
        brawlers = response.json()['items']
        for brawler in brawlers:
            if brawler['name'].lower() == brawler_name.lower():
                return brawler