#https://console.twilio.com/
from twilio.rest import Client

account_sid = "ACacfe8e62e9858603b28c065d0fc01b11"
auth_token = "f412020eb4090b361cc0aeda6c63b700"
client = Client(account_sid,auth_token)

call = client.messages.create(
    to="+60182060368",
    from_="+19896144687",
    body="Hi, This is text message"
)

print(call.date_created)
print(call.date_sent)
# messages
# chat
# calls
# video
# fax