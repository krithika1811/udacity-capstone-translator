import requests
import os
import base64

def decode_token(token):
    """
     This method decodes base64 encoded string to string
    """
    base64_bytes = token.encode('ascii') 
    message_bytes = base64.b64decode(base64_bytes)
    decoded_token = message_bytes.decode('ascii')
    return decoded_token

def get_random_quote(token, category="Success"):
    url = f"https://api.api-ninjas.com/v1/quotes?category={category.lower()}"
    try:
        # response = requests.get(url, headers= {'X-Api-Key': 'hOtaHIXSL6MwSRc7X9lsWQ==qpweoPqBbcusyVLe'})
        response = requests.get(url, headers= {'X-Api-Key': decode_token(token)})
        if response.status_code == 200:
            json_data = response.json()
            author = json_data[0]['author']
            quote = json_data[0]['quote']
            return f"{author} once said {quote}"
        else:
            return "Error while getting quote"
    except Exception:
        raise Exception