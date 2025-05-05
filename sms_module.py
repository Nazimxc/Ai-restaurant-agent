from twilio.rest import Client

def send_sms(contact, message):
    account_sid = 'AC0fb08e4f671cf2fc47a1beeaa4f4b06b'  # 🔁 Replace with actual SID
    auth_token = '98419f0ad1abc54528a08e7fd07e3652'    # 🔁 Replace with actual token
    from_number = '+18317045939' # 🔁 Replace with Twilio number like '+1234567890'


    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=contact
        )
        print("✅ SMS sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")
  