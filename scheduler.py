import sqlalchemy as db
from api import Weather
from sender import Email
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv('OPENWEATHER_ENDPOINT')
openw_api_key = os.getenv('OPENWEATHER_APIKEY')
sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
sender = os.getenv('SENDER_EMAIL')

engine = db.create_engine(os.getenv('DATABASE_URL'), echo=True)
connection = engine.connect()
metadata = db.MetaData()
users = db.Table('User', metadata, autoload=True, autoload_with=engine)

query = db.select([users])
result = connection.execute(query)
result_list = result.fetchall()
result_dict = [{
    'email': row[1],
    'location': row[2],
    'lat': row[3].split(' ')[0],
    'lon': row[3].split(' ')[1]} for row in result_list]

for single in result_dict:
    my_weather = Weather(endpoint, openw_api_key, single['lat'], single['lon'])
    forecast = my_weather.getResponse()
    print(forecast)



