import pandas as pd
import numpy as np
import requests
import json

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

def parsing_access_token_json():
    """
    Function that manipulates the JSON that is returned from the API access key call from the get_api_access function
    """
    amadeus = get_api_access(secret, c_id)
    json_api_token = amadeus.json()
    final_access_token = json_api_token['access_token']
    print(final_access_token)

    return final_access_token

def get_flights_between_cities(first_city, second_city, departure_date, adults):
    """
    This function requires the ATA code of an airport or city to properly fetch flight data
    """
    token = parsing_access_token_json()
    flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    header = {"Authorization": "Bearer {token}"}
    data = {
        "originLocationCode": first_city,
        "destinationLocationCode": second_city,
        "departureDate": departure_date,
        "adults": adults,
    }

    flight_data = requests.get(flight_url, data=data, headers=header)

    if flight_data.status_code == 200:
        print('everything works w')
    else:
        print("this does not work")
        # 401 status code - something is wrong
        print(flight_data.status_code)


get_flights_between_cities("BOS", "NYC", "2025-04-10", 1)

