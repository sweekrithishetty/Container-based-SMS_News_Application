from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACda580fcc3fc654fabfee3fe3a1c40244"
# Your Auth Token from twilio.com/console
auth_token  = "936f9d5102f38eb51014f68bd0d11c13"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16073749303", 
    from_="XXXXXXXXXXXXX",
    body="Hello from Python!")

