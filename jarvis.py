from wit import Wit
import random
import pickle

sender_db = pickle.load(open('database.db', 'rb'))

greetings = ['Hello there!',
             'Hi!',
             'Hello!']

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
        return 'You\'re in the database!'
    witClient = Wit(access_token='LFS4A4JKLBRIOCPTPNSFGBT6QR475VIG')
    response = witClient.message(text)
    try:
        intent = response['entities']['intent'][0]['value']
    except KeyError:
        intent = ''
    entities = extract_entities(response)
    if intent == 'timetable':
        return 'I understand you want the timetable for' + entities['datetime']
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
