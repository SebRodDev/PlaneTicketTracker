import pandas as pd
import numpy as np
import requests

secret = "C6HYFUI5uXx0frbq"
c_id = "4kY6IGhYvfJXr3MhDiJBxvQRfF2Yl1JW"

def get_api_access(client_secret, client_id):
    """
    Function to obtain an API access token for Amadeus Travel API to obtain flight information for 
    a specific airline
    """
    auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    args = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    access_token = requests.post(auth_url, data=args, headers=headers)

    return access_token


amadeus = get_api_access(secret, c_id)
print(amadeus.text)

