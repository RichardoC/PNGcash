from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(body)
    if body == None:
        body = 'error'

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")
    elif body == 'error':
        resp.message("You said nothing")
    elif body.split(' ')[0] == 'send' or body.split(' ')[0] == 'Send':
        b = body.split(' ')
        v = b[1]
        p = b[0]
        s = 'You are now sending {0}: {1}$PNG'.format(v, p)
        resp.message(s)
    else:
        resp.message("another thing")

    return str(resp)

@app.route("/")
def hello():
    return "Default Hello World!"

if __name__ == "__main__":
    app.run(host='http://0.0.0.0:5000/')
