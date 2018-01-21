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
        fromID = parts[0]
        toID = parts[1]
        amount = parts[2]
        ledger.transfer(fromID, toID, amount)
        try:
            ledger.transfer(fromID, toID, amount)
            m = '{0} -> {1} -> ${2}'.format(fromID,
                                            toID,
                                            amount)
        except:
            m = ':('
        resp.message(m)
    elif len(parts) == 4:
        m = 'Error'
        if parts[1] == '->':
            fromID = parts[0]
            toID = parts[2]
            amount = parts[3]
            try:
                ledger.transfer(fromID, toID, amount)
                m = '{0} -> {1} -> ${2}'.format(fromID,
                                                toID,
                                                amount)
            except:
                m = ':('
        resp.message(m)
    elif len(parts) == 1:
        #try balance
        #send back balance
        bal = ledger.balance(parts)
        resp.message(bal)
    else:
        resp.message("Error")
    return str(resp)

@app.route("/")
def hello():
    return "Default Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
