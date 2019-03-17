<<<<<<< HEAD
import nexmo
import json
from spenny_back import spenny_back
from flask import Flask, request, jsonify
from pprint import pprint

link = "https://077ba7d7.ngrok.io"
region = "London"
employement = "Student"
income = 20
rent = 0
adults = 0
children = 0
smoke = False
alcohol = True


client = nexmo.Client(application_id="d03098d1-54c0-44db-96f0-05bbe2efcaa7", private_key=''.join(open('private.key', 'r').readlines()))

def welcomeCall():
    response = client.create_call({
        'to': [{'type': 'phone', 'number': '447886599886'}],
        'from': {'type': 'phone', 'number': '447520660976'},
        'answer_url': [link + "/webhooks/firstWelcome"]
    })

app = Flask(__name__)

@app.route("/webhooks/firstWelcome")
def answer_call():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/welcome"
    ncco =[{
            "action": "talk",
            "text": "Hello, welcome to Spenny! We help you fly to financial freedom. Press any key to get started."
        },
        {
            "action": "input",
            "maxDigits": 1,
            "eventUrl": [link + "/webhooks/answer3"]
        }]
    return jsonify(ncco)

# @app.route("/webhooks/answer1")
# def q1():
#     for param_key, param_value in request.args.items():
#         print("{}: {}".format(param_key, param_value))
#     input_webhook_url = request.url_root + "webhooks/dtmf"
#     ncco =[{
#             "action": "talk",
#             "text": """ To begin, we just need to know where you are currently residing in.
#                     Please choose from the following; and press the hash key when you're done.
#                     Press 1 for England, 2 for The North East, 3 for The North West,
#                     4 for Yorkshire and The Humber, 5 for the East Midlands, 6 for the west Midlands, 7 for the East,
#                     8 for London, 9 for the South East, 10 for the South West, 11 for Wales or 12 for Scotland, or 13 for northern ireland"""
#         },
#         {
#             "action": "input",
#             "maxDigits": 2,
#             "eventUrl": [link + "/webhooks/answer2"]
#         }]
#     return jsonify(ncco)
        
# @app.route("/webhooks/answer2")
# def q2():
#     for param_key, param_value in request.args.items():
#         print("{}: {}".format(param_key, param_value))
#     input_webhook_url = request.url_root + "webhooks/dtmf"
#     ncco =[{
#             "action": "talk",
#             "text": """Okay! Now we need to know what your current employment status is? 
#                         Are you 1, working full time, 2, working part time, 3, a student, 
#                         4, retired, or 5, unemployed?""" 
#         },
#         {
#             "action": "input",
#             "maxDigits": 1,
#             "eventUrl": [link + "/webhooks/answer3"]
#         }]
#     return jsonify(ncco)

@app.route("/webhooks/answer3")
def q3():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[{
            "action": "talk",
            "text": "Great! we need your annual disposable income (after taxes, and including benefits). Please round up. Press the hash key once you're done." 
        },
        {
            "submitOnHash": True,
            "action": "input",
            "maxDigits": 8,
            "eventUrl": [link + "/webhooks/answer4"]
        }]
    return jsonify(ncco)

@app.route("/webhooks/answer4")
def q4():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[{
            "action": "talk",
            "text": "How much is your rent/mortage per month? Please round up. Press the hash key when you are done" 
        },
        {
            "submitOnHash": True,
            "action": "input",
            "maxDigits": 8,
            "eventUrl": [link + "/webhooks/answer5"]
        }]
    return jsonify(ncco)

@app.route("/webhooks/answer5")
def q5():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[
        {
            "action": "talk",
            "text": "How many adults are currently living in your household? Press the hash key when you're done" 
        },
        {
            "submitOnHash": True,
            "action": "input",
            "maxDigits": 2,
            "eventUrl": [link + "/webhooks/answer6"]
        }]
    return jsonify(ncco)

@app.route("/webhooks/answer6")
def q6():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[{
            "action": "talk",
            "text": "How many children are currently living in your household? Press the hash key when you're done" 
        },
        {
            "submitOnHash": True,
            "action": "input",
            "maxDigits": 2,
            "eventUrl": [link + "/webhooks/dtmf"]
        }]
    return jsonify(ncco)

# @app.route("/webhooks/answer7")
# def q7():
#     for param_key, param_value in request.args.items():
#         print("{}: {}".format(param_key, param_value))
#     input_webhook_url = request.url_root + "webhooks/dtmf"
#     ncco =[{
#             "action": "talk",
#             "text": "Do you smoke? Press 1 for yes and 2 for no." 
#         },
#         {
#             "action": "input",
#             "maxDigits": 1,
#             "eventUrl": [link + "/webhooks/answer8"]
#         }]
#     return jsonify(ncco)

# @app.route("/webhooks/answer8")
# def q8():
#     for param_key, param_value in request.args.items():
#         print("{}: {}".format(param_key, param_value))
#     input_webhook_url = request.url_root + "webhooks/dtmf"
#     ncco =[{
#             "action": "talk",
#             "text": "Finally, do you drink? Press 1 for yes and 2 for no." 
#         },
#         {
#             "action": "input",
#             "maxDigits": 1,
#             "eventUrl": [link]
#             }]
#     return jsonify(ncco)

# @app.route("/webhooks/answer1", methods=['POST'])
# def region():
#     data = request.get_json()
#     pprint(data)
#     num = (data['dtmf'])
#     if(num == 1):
#         region = "England"
#     elif(num == 2):
#         region = "North East"
#     elif(num == 3):
#         region = "North West"
#     elif(num == 4):
#         region = "Yorkshire and The Humber"
#     elif(num == 5):
#         region = "East Midlands"
#     elif(num == 6):
#         region = "West Midlands"
#     elif(num == 7):
#         region = "East"
#     elif(num == 8):
#         region = "London"
#     elif(num == 9):
#         region = "South East"
#     elif(num == 10):
#         region = "South West"
#     elif(num == 11):
#         region = "Wales"
#     elif(num == 12):
#         region = "Scotland"
#     elif(num == 13):
#         region = "North Ireland"

# @app.route("/webhooks/answer2", methods=['POST'])
# def employment():
#     data = request.get_json()
#     pprint(data)
#     num = (data['dtmf'])
#     if(num == 1):
#         employement = "Full Time Employed"
#     elif(num == 2):
#         employement = "Part Time Employed"
#     elif(num == 3):
#         employement = "Student"
#     elif(num == 4):
#         employement = "Retired"
#     elif(num == 5):
#         employement = "Unemployed"
  
@app.route("/webhooks/answer3", methods=['POST'])
def income():
    data = request.get_json()
    pprint(data)
    income = (data['dtmf'])

@app.route("/webhooks/answer4", methods=['POST'])
def rent():
    data = request.get_json()
    pprint(data)
    rent = (data['dtmf'])

@app.route("/webhooks/answer5", methods=['POST'])
def adults():
    data = request.get_json()
    pprint(data)
    adults = (data['dtmf'])

@app.route("/webhooks/answer6", methods=['POST'])
def children():
    data = request.get_json()
    pprint(data)
    children = (data['dtmf'])

# @app.route("/webhooks/answer7", methods=['POST'])
# def smoke():
#     data = request.get_json()
#     pprint(data)
#     num = (data['dtmf'])
#     if(num == 1):
#         smoke = True

# @app.route("/webhooks/answer8", methods=['POST'])
# def alcohol():
#     data = request.get_json()
#     pprint(data)
#     num = (data['dtmf'])
#     if(num == 1):
#         alcohol = True

budget = spenny_back(region, 0, "Moderate", alcohol, smoke, rent, 0, 0, 10, 10, 10)

@app.route("/webhooks/dtmf", methods=['POST'])
def dtmf():
    data = request.get_json()
    pprint(data)
    ncco =[
        {
            "action": "talk",
            "text": """ Here is your weekly budget breakdown. Food £{}. Alcohol £.{}
                        Clothing £{}. Utilities £{}. Health: £{}. Transport: £{}. Communication £{}.
                        Recreation £{}. Education £{}. Catering £{}. Toiletries £{} """.format(budget["food"], budget["alcohol"], budget["clothing"], budget["utilities"], budget["health"], budget["transport"], budget["communication"], budget["recreation"], budget["education"], budget["catering"], budget["toiletries"])
        },           
        {
            "eventUrl": [link + "/webhooks/goodbye"]
        }
    ]
    return jsonify(ncco)
    
@app.route("/webhooks/goodbye")
def goodbye():
    ncco =[
        {
            "action": "talk",
            "text": "Thank you for using spenny. Goodbye!"
        }
    ]
    return jsonify(ncco)

def main():
    welcomeCall()
    app.run(port=5000)


=======
import nexmo
import json
from spenny_back import spenny_back
from flask import Flask, request, jsonify
from pprint import pprint

link = "https://077ba7d7.ngrok.io"
region = "London"
employement = "Student"
income = 20
rent = 0
adults = 0
children = 0
smoke = False
alcohol = True


client = nexmo.Client(application_id="d03098d1-54c0-44db-96f0-05bbe2efcaa7", private_key=''.join(open('private.key', 'r').readlines()))

def welcomeCall():
    response = client.create_call({
        'to': [{'type': 'phone', 'number': '447886599886'}],
        'from': {'type': 'phone', 'number': '447520660976'},
        'answer_url': [link + "/webhooks/firstWelcome"]
    })

app = Flask(__name__)

@app.route("/webhooks/firstWelcome")
def answer_call():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/welcome"
    ncco =[{
            "action": "talk",
            "text": "Hello, welcome to Spenny! We help you fly to financial freedom. Press any key to get started."
        },
        {
            "action": "input",
            "maxDigits": 1,
            "eventUrl": [link + "/webhooks/answer3"]
        }]
    return jsonify(ncco)

# @app.route("/webhooks/answer1")
# def q1():
#     for param_key, param_value in request.args.items():
#         print("{}: {}".format(param_key, param_value))
#     input_webhook_url = request.url_root + "webhooks/dtmf"
#     ncco =[{
#             "action": "talk",
#             "text": """ To begin, we just need to know where you are currently residing in.
#                     Please choose from the following; and press the hash key when you're done.
#                     Press 1 for England, 2 for The North East, 3 for The North West,
#                     4 for Yorkshire and The Humber, 5 for the East Midlands, 6 for the west Midlands, 7 for the East,
#                     8 for London, 9 for the South East, 10 for the South West, 11 for Wales or 12 for Scotland, or 13 for northern ireland"""
#         },
#         {
#             "action": "input",
#             "maxDigits": 2,
#             "eventUrl": [link + "/webhooks/answer2"]
#         }]
#     return jsonify(ncco)
        
# @app.route("/webhooks/answer2")
# def q2():
#     for param_key, param_value in request.args.items():
#         print("{}: {}".format(param_key, param_value))
#     input_webhook_url = request.url_root + "webhooks/dtmf"
#     ncco =[{
#             "action": "talk",
#             "text": """Okay! Now we need to know what your current employment status is? 
#                         Are you 1, working full time, 2, working part time, 3, a student, 
#                         4, retired, or 5, unemployed?""" 
#         },
#         {
#             "action": "input",
#             "maxDigits": 1,
#             "eventUrl": [link + "/webhooks/answer3"]
#         }]
#     return jsonify(ncco)

@app.route("/webhooks/answer3")
def q3():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[{
            "action": "talk",
            "text": "Great! we need your annual disposable income (after taxes, and including benefits). Please round up. Press the hash key once you're done." 
        },
        {
            "submitOnHash": True,
            "action": "input",
            "maxDigits": 8,
            "eventUrl": [link + "/webhooks/answer4"]
        }]
    return jsonify(ncco)

@app.route("/webhooks/answer4")
def q4():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[{
            "action": "talk",
            "text": "How much is your rent/mortage per month? Please round up. Press the hash key when you are done" 
        },
        {
            "submitOnHash": True,
            "action": "input",
            "maxDigits": 8,
            "eventUrl": [link + "/webhooks/answer5"]
        }]
    return jsonify(ncco)

@app.route("/webhooks/answer5")
def q5():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[
        {
            "action": "talk",
            "text": "How many adults are currently living in your household? Press the hash key when you're done" 
        },
        {
            "submitOnHash": True,
            "action": "input",
            "maxDigits": 2,
            "eventUrl": [link + "/webhooks/answer6"]
        }]
    return jsonify(ncco)

@app.route("/webhooks/answer6")
def q6():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))
    input_webhook_url = request.url_root + "webhooks/dtmf"
    ncco =[{
            "action": "talk",
            "text": "How many children are currently living in your household? Press the hash key when you're done" 
        },
        {
            "submitOnHash": True,
            "action": "input",
            "maxDigits": 2,
            "eventUrl": [link + "/webhooks/dtmf"]
        }]
    return jsonify(ncco)

# @app.route("/webhooks/answer7")
# def q7():
#     for param_key, param_value in request.args.items():
#         print("{}: {}".format(param_key, param_value))
#     input_webhook_url = request.url_root + "webhooks/dtmf"
#     ncco =[{
#             "action": "talk",
#             "text": "Do you smoke? Press 1 for yes and 2 for no." 
#         },
#         {
#             "action": "input",
#             "maxDigits": 1,
#             "eventUrl": [link + "/webhooks/answer8"]
#         }]
#     return jsonify(ncco)

# @app.route("/webhooks/answer8")
# def q8():
#     for param_key, param_value in request.args.items():
#         print("{}: {}".format(param_key, param_value))
#     input_webhook_url = request.url_root + "webhooks/dtmf"
#     ncco =[{
#             "action": "talk",
#             "text": "Finally, do you drink? Press 1 for yes and 2 for no." 
#         },
#         {
#             "action": "input",
#             "maxDigits": 1,
#             "eventUrl": [link]
#             }]
#     return jsonify(ncco)

# @app.route("/webhooks/answer1", methods=['POST'])
# def region():
#     data = request.get_json()
#     pprint(data)
#     num = (data['dtmf'])
#     if(num == 1):
#         region = "England"
#     elif(num == 2):
#         region = "North East"
#     elif(num == 3):
#         region = "North West"
#     elif(num == 4):
#         region = "Yorkshire and The Humber"
#     elif(num == 5):
#         region = "East Midlands"
#     elif(num == 6):
#         region = "West Midlands"
#     elif(num == 7):
#         region = "East"
#     elif(num == 8):
#         region = "London"
#     elif(num == 9):
#         region = "South East"
#     elif(num == 10):
#         region = "South West"
#     elif(num == 11):
#         region = "Wales"
#     elif(num == 12):
#         region = "Scotland"
#     elif(num == 13):
#         region = "North Ireland"

# @app.route("/webhooks/answer2", methods=['POST'])
# def employment():
#     data = request.get_json()
#     pprint(data)
#     num = (data['dtmf'])
#     if(num == 1):
#         employement = "Full Time Employed"
#     elif(num == 2):
#         employement = "Part Time Employed"
#     elif(num == 3):
#         employement = "Student"
#     elif(num == 4):
#         employement = "Retired"
#     elif(num == 5):
#         employement = "Unemployed"
  
@app.route("/webhooks/answer3", methods=['POST'])
def income():
    data = request.get_json()
    pprint(data)
    income = (data['dtmf'])

@app.route("/webhooks/answer4", methods=['POST'])
def rent():
    data = request.get_json()
    pprint(data)
    rent = (data['dtmf'])

@app.route("/webhooks/answer5", methods=['POST'])
def adults():
    data = request.get_json()
    pprint(data)
    adults = (data['dtmf'])

@app.route("/webhooks/answer6", methods=['POST'])
def children():
    data = request.get_json()
    pprint(data)
    children = (data['dtmf'])

# @app.route("/webhooks/answer7", methods=['POST'])
# def smoke():
#     data = request.get_json()
#     pprint(data)
#     num = (data['dtmf'])
#     if(num == 1):
#         smoke = True

# @app.route("/webhooks/answer8", methods=['POST'])
# def alcohol():
#     data = request.get_json()
#     pprint(data)
#     num = (data['dtmf'])
#     if(num == 1):
#         alcohol = True

budget = spenny_back(region, 0, "Moderate", alcohol, smoke, rent, 0, 0, 10, 10, 10)

@app.route("/webhooks/dtmf", methods=['POST'])
def dtmf():
    data = request.get_json()
    pprint(data)
    ncco =[
        {
            "action": "talk",
            "text": """ Here is your weekly budget breakdown. Food £{}. Alcohol £.{}
                        Clothing £{}. Utilities £{}. Health: £{}. Transport: £{}. Communication £{}.
                        Recreation £{}. Education £{}. Catering £{}. Toiletries £{} """.format(budget["food"], budget["alcohol"], budget["clothing"], budget["utilities"], budget["health"], budget["transport"], budget["communication"], budget["recreation"], budget["education"], budget["catering"], budget["toiletries"])
        },           
        {
            "eventUrl": [link + "/webhooks/goodbye"]
        }
    ]
    return jsonify(ncco)
    
@app.route("/webhooks/goodbye")
def goodbye():
    ncco =[
        {
            "action": "talk",
            "text": "Thank you for using spenny. Goodbye!"
        }
    ]
    return jsonify(ncco)

def main():
    welcomeCall()
    app.run(port=5000)


>>>>>>> 714460cbaf882d9cf6daea2e6e04db5be8de05d0
main()