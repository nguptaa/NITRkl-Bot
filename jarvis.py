import wolframalpha
from wit import Wit
import simplejson as json
import forecastio
from geopy.geocoders import Nominatim
import random
import wikipedia
import pickle

sender_db = pickle.load(open('database.db', 'rb'))

modules = []
client_token = 'f80b5418eb374680af54afaca60137e4'
subscription_key = '1b65219b-2acc-437b-a76a-e5e471ea4697'

greetings = ['Hello there!',
             'Hi!',
             'Hello!',
             'Greetings!']

curses = ['Hey! I don\'t think I deserve that',
          'I\'d never speak to you that way']

def do(text, send):
    witClient = Wit(access_token='Z2M5NG4DUAOD3IH24BNQSXGM4LGIK4PU')
    wolframClient = wolframalpha.Client('5G696A-TT6AEK7L74')
    response = witClient.message(text)
    intent = response['entities']['intent'][0]['value']
    if intent == 'weather':
        loc = Nominatim()
        loc = loc.geocode(response['entities']['location'][0]['value'])
        forecast = forecastio.load_forecast('17e86a360729736b727899a8135e33ad',loc.latitude, loc.longitude)
        return forecast.hourly().summary
    elif intent == 'greeting':
        return random.choice(greetings)
    elif intent == 'wikipedia':
        return wikipedia.summary(response['entities']['contact'][0]['value'], sentences=1)
    elif intent == 'curse':
        return random.choice(curses)
    else:
        return 'I did not understand what you said.'
