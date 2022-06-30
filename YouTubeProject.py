from googleapiclient.discovery import build
import pandas as pd
import sqlalchemy as db

url = 'https://www.googleapis.com/youtube/v3/channels'

youtube = build('youtube', 'v3', developerKey = 'AIzaSyCKaLfaVA-hOcZXx1dnrPdGaB1nKCe0vOE')
request = youtube.channels().list(part = 'Statistics', id = 'UCcA2BAZFc6RsG0D6zzLAJ8Q')
response = request.execute()
#note: my sql doesnt work with nested dictionaries that is why you where getting so many errors.
selecteddata = response['items'][0]['statistics']
print(selecteddata)
sleecteddata['items'][0]['statistics']['videocount'] = 500
df = pd.DataFrame.from_dict([selecteddata])
print(df)
engine = db.create_engine('sqlite:///SEOYTDatabase.db')
df.to_sql('YTProject', con=engine, if_exists='replace', index=False)
query_result = engine.execute("SELECT * FROM YTProject;").fetchall()
print(pd.DataFrame(query_result))

youtube.close()
