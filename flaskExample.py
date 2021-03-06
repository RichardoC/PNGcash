from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import ledger

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    print(request)
    print(request.values)
    body = request.values.get('Body', None)
    print(body)
    if body == None:
        body = 'Error'

    # Start our TwiML response
    resp = MessagingResponse()
    parts = body.split()

    # Determine the right reply for this message
    if len(parts) == 3:
        fromID = int(parts[0])
        toID = int(parts[1])
        amount = int(parts[2])
        status = ledger.transfer(fromID, toID, amount)
        if status:
            m = ':) {0} -> {1} -> ${2}'.format(fromID,
                                               toID,
                                               amount)
        else:
            m = ':('
        resp.message(m)
    elif len(parts) == 4:
        m = 'Error'
        if parts[1] == '->':
           fromID = int(parts[0])
           toID = int(parts[2])
           amount = int(parts[3])
           status = ledger.transfer(fromID, toID, amount)
           if status:
               m = '{0} -> {1} -> ${2}'.format(fromID,
                                               toID,
                                               amount)
           else:
               m = ':('
        resp.message(m)
    elif len(parts) == 1:
        # Check balance
        bal = ledger.balance(int(parts[0]))
        resp.message(str(bal))
    else:
        resp.message("Error")
    return str(resp)

@app.route("/")
def hello():
    return "Default Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
