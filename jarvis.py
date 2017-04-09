from wit import Wit
import random
import pickle
from datetime import datetime, timedelta

sender_db = pickle.load(open('database.db', 'rb'))
timetable_db = pickle.load(open('new_timetable.db', 'rb'))

greetings = ['Hello there!',
             'Hi!',
             'Hello!']

times = [['8:00AM','9:00AM'], ['9:00AM', '10:00AM'], ['10:00AM', '11:00AM'], ['11:00AM', '12:00PM'], ['12:00PM', '1:15PM'], ['1:15PM', '2:15PM'], ['2:15PM', '3:15PM'], ['3:15PM', '4:15PM'], ['4:15PM', '5:15PM']]

questions = ['I am fine. What about you ?']

devs = ['Nikhil and Chetas created me :D']

profs = ['Prof. Pabitra Mohan Khilar']

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
        return 'You\'re in the database!'
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
            time = datetime.strptime(entities['datetime'], '%Y-%m-%dT%H:%M:%S.000-07:00')
            tstr = time.strftime('%A %H %M').split()
            sec = sender_db[send][0]
            day_tt = timetable_db[tstr[0]][sec]
            for x in day_tt:
                a = time.strptime(x[0], '%H:%M%p')
                a = timedelta(hours=a.hour, minutes=a.minute)
                b = time.strptime(x[1], '%H:%M%p')
                b = timedelta(hours=b.hour, minutes=b.minute)
                y = time - datetime(1900, 1, 1)
                if y>=a or b>=y:
                    return 'You have ' + x[2].title()
        except KeyError:
            return 'No class'
    elif intent == 'greeting':
        return random.choice(greetings)
    elif intent == 'question':
        return questions[0]
    elif intent == 'dev':
        return devs[0]
    elif intent == 'prof':
        return prof[0]
    else:
        return 'I did not understand what you said'
