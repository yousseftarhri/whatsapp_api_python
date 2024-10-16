import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

class Whatsappbot:

    def __init__(self, WHATSAPP_BUSINESS_PHONE_NUMBER_ID, access_token):
        self.WHATSAPP_BUSINESS_PHONE_NUMBER_ID = WHATSAPP_BUSINESS_PHONE_NUMBER_ID
        self.access_token = access_token

    def SendMessage(self):

        url = f"https://graph.facebook.com/v21.0/{self.WHATSAPP_BUSINESS_PHONE_NUMBER_ID}/messages"

        # Headers for the request
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        payload = {
          "messaging_product": "whatsapp",
          "recipient_type": "individual",
          "to": "f",
          "type": "text",
          "text": {
            "body": "Hi we gonna response ASAP"
          }
        }

        # Sending the POST request
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Output the response
        if response.status_code == 200:
            print(response.content)
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status Code: {response.status_code}, Response: {response.text}")

# Replace with your WhatsApp Business Phone Number ID and access token
whatsapp_id = os.getenv("phone_number_id")
access_token = os.getenv("access_token")

bot = Whatsappbot(whatsapp_id, access_token)
bot.SendMessage()
