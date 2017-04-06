from wit import Wit
import random
import pickle

sender_db = pickle.load(open('database.db', 'rb'))

greetings = ['Hello there!',
             'Hi!',
             'Hello!',
             'Greetings!']

questions = ['I am fine. What about you ?']

devs = ['Nikhil and Chetas created me :D']

chutiyas = ['Vatsal Dave 😆']

dozers = ['Vidit Singh 😅']

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
    if sec[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and sec[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        sender_db[send] = sec
        return 'You\'re in the database!'
    witClient = Wit(access_token='LFS4A4JKLBRIOCPTPNSFGBT6QR475VIG')
    response = witClient.message(text)
    intent = response['entities']['intent'][0]['value']
    entities = extract_entities(response)
    if intent == 'timetable':
        return 'I understand you want the timetable for ' + entities['datetime'] + ' but I don\'t have it yet. Sorry!'
    elif intent == 'greeting':
        return random.choice(greetings)
    elif intent == 'question':
        return random.choice(questions)
    elif intent == 'dev':
        return random.choice(devs)
    elif intent == 'chutiya':
        return random.choice(chutiyas)
    elif intent == 'dozer':
        return random.choice(dozers)
    else:
        return 'I did not understand what you said'
