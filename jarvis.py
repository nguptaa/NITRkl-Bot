from wit import Wit
import random
import pickle
from datetime import datetime, timedelta
import transfer
import heroku3, os

heroku_conn = heroku3.from_key('cebe5a07-6ded-4700-a6f7-91455a65fc0c')
app = heroku_conn.app('nitrkl-bot')
config = app.config()
fileurl = config['FILE_URL']
transfer.downloadFile(fileurl, 'database.db')
sender_db = pickle.load(open('database.db', 'rb'))
timetable_db = pickle.load(open('new_timetable.db', 'rb'))

greetings = ['Hello there!',
             'Hi!',
             'Hello!']

devs = ['Nikhil and chetas created me :D']

def extract_entities(response):
    # Extract entites from NLP response
    entities = {}
    for x in response['entities']:
        if x == 'intent':
            pass
        else:
            entities[x] = response['entities'][x][0]['value']

    return entities

def do(text, send):
    sec = text.split()
    if sec[0] in ['H'] and sec[1] in ['9']:
        sender_db[send] = sec
        pickle.dump(sender_db, open('database.db', 'wb'))
        url = transfer.uploadFile('database.db')
        config['FILE_URL'] = url
        return 'You\'re in the database'
    witClient = Wit(access_token='LFS4A4JKLBRIOCPTPNSFGBT6QR475VIG')
    response = witClient.message(text)
    try:
        intent = response['entities']['intent'][0]['value']
    except KeyError:
        intent = ''
    entities = extract_entities(response)
    print entities, intent
    if intent == 'timetable':
        try:
            time = datetime.strptime(entities['datetime'], '%Y-%m-%dT%H:%M:%S.000+05:30')
            tstr = time.strftime('%A %H %M -%Y-%m-%d').split()
            sec = sender_db[send][0]
            day_tt = timetable_db[tstr[0]][sec]
            for x in day_tt:
                a = time.strptime(x[0] + tstr[3], '%I:%M%p-%Y-%m-%d')
                b = time.strptime(x[1] + tstr[3], '%I:%M%p-%Y-%m-%d')
                if a <= time < b:
                    return 'You have ' + x[2].title()
        except KeyError:
            return 'No class'
    elif intent == 'greeting':
        return random.choice(greetings)
    elif intent == 'dev':
        return devs[0]
    else:
        return 'I did not understand what you said'
