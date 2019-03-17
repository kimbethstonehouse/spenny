import nexmo
import json
from flask import Flask, request, jsonify
from pprint import pprint

client = nexmo.Client(application_id="d03098d1-54c0-44db-96f0-05bbe2efcaa7", private_key=''.join(open('private.key', 'r').readlines()))

def welcomeCall(number):
    response = client.create_call({
        'to': [{'type': 'phone', 'number': number}],
        'from': {'type': 'phone', 'number': '447520660976'},
        'answer_url': ['https://developer.nexmo.com/ncco/tts.json']
    })

    response = client.send_speech(uuid, text='Hello')

app = Flask(__name__)

@app.route("/webhooks/answer")
def answer_call():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[
        {
            "action": "talk",
            "text": "Hello, welcome to Spenny! We help you fly to financial freedom. Press any key to get started."
        },
        {
            "action": "input",
            "maxDigits": 1,
            "eventUrl": ["http://example.com"]
        },
        {
            "action": "talk",
            "text": """ To begin, we just need to know where you are currently residing in.
                    Please choose from the following; and press the hash key when you're done.
                    Press 1 for England, 2 for The North East, 3 for The North West,
                    4 for Yorkshire and The Humber, 5 for the East Midlands, 6 for the west Midlands, 7 for the East,
                    8 for London, 9 for the South East, 10 for the South West, 11 for Wales or 12 for Scotland"""
        },
        {
            "action": "input",
            "maxDigits": 2,
            "eventUrl": ["http://example.com"]
        },
        {
            "action": "talk",
            "text": """Okay! Now we need to know what your current employment status is? 
                        Are you 1, working full time, 2, working part time, 3, a student, 
                        4, retired, or 5, unemployed?""" 
        },
        {
            "action": "input",
            "maxDigits": 1,
            "eventUrl": ["http://example.com"]
        },
        {
            "action": "talk",
            "text": "Great! Now we need your annual disposable income (after taxes, and including benefits). Press the hash key once you're done." 
        },
        {
            "action": "input",
            "maxDigits": 8,
            "eventUrl": ["http://example.com"]
        }, 
        {
            "action": "talk",
            "text": "How much is your rent per month? Press the hash key when you are done" 
        },
        {
            "action": "input",
            "maxDigits": 8,
            "eventUrl": ["http://example.com"]
        },
        {
            "action": "talk",
            "text": "How many adults are currently living in your household? Press the hash key when you're done" 
        },
        {
            "action": "input",
            "maxDigits": 2,
            "eventUrl": ["http://example.com"]
        },
        {
            "action": "talk",
            "text": "How many children are currently living in your household? Press the hash key when you're done" 
        },
        {
            "action": "input",
            "maxDigits": 2,
            "eventUrl": ["http://example.com"]
        },
        {
            "action": "talk",
            "text": "Do you smoke? Press 1 for yes and 2 for no." 
        },
        {
            "action": "input",
            "maxDigits": 1,
            "eventUrl": ["http://example.com"]
        },
        {
            "action": "talk",
            "text": "Finally, do you drink? Press 1 for yes and 2 for no." 
        },
        {
            "action": "input",
            "maxDigits": 1,
            "eventUrl": ["http://example.com"]
        }
    ]
    return jsonify(ncco)

@app.route("/webhooks/dtmf", methods=['POST'])
def dtmf():
    data = request.get_json()
    pprint(data)
    ncco =[
        {
            "action": "talk",
            "text": "You pressed {}, goodbye".format(data['dtmf'])
        }
    ]
    return jsonify(ncco)

def main():
    pp.run(port=3000)


main()
    

        
