from flask import Flask, request, redirect, session
import twilio.twiml, random, re

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/", methods=['GET', 'POST'])
def replyMethod():
    
    #isbn = re.compile(^(97(8|9))?\d{9}(\d|X)$)
    
    number = request.form['From']
    message_body = request.form['Body']
    
    #isbnNumbers = isbn.findall(message_body)
    
    #message = ''
    
    #if isbnNumbers.amount() == 0:
    #    message = 'found isbn number'

    greetings = ['Hello! ', 'Hi! ', 'Hey! ']

    questions = ['How are you? ', 'Whats up? ', 'Hows it going? ', 'Wanna buy a book? ']

    resp = twilio.twiml.Response()

    greeting = random.choice(greetings)

    question = random.choice(questions)

    message = greeting + 'Im Tricia! ' + question

    resp.sms(message)

    return str(resp)

if __name__ == "__main__":
    app.run()
