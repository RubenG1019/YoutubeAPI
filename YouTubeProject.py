from googleapiclient.discovery import build

url = 'https://www.googleapis.com/youtube/v3/channels'

youtube = build('youtube', 'v3', developerKey = 'AIzaSyCKaLfaVA-hOcZXx1dnrPdGaB1nKCe0vOE')
request = youtube.channels().list(part = 'Statistics', id = 'UCcA2BAZFc6RsG0D6zzLAJ8Q')
response = request.execute()
print(response)
youtube.close()