import requests

API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRiODhlYWI2LTdkNGMtNGJlOC05MDYxLWM5ZmZhMzQ0NGFkZiIsImlhdCI6MTcxNzQxMzI5OSwic3ViIjoiZGV2ZWxvcGVyLzQzNzNlZjg0LWEwMWYtYTk5YS0yNGRhLWYyYzk5NWQ5ZTcwYiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTgxLjEwLjMxLjExNCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.MNffIoqgRS7MAhEHrrpJijO4EwWlBRiyEbZT34jWjcyH-ORn11e8RadFhrrIT_ZpAZexUzaRxS88LAhsYaAjbw'
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