import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
print(response)
# print(response.text)

# WHEN NOT APPLY API KEY and PARAM required
# <Response [400]>
# JSON OBJ
# {"error": {"code": "VALIDATION_ERROR", "description": "Please specify a location or a latitude and longitude"}}

# AFTER
# <Response [200]>
# JSON OBJECT THAT LIST OF BUSINESS in NYC

# Change json to python dict
businesses = response.json()["businesses"]
# print(businesses)


businesses_name = [business["name"]
                   for business in businesses]

print(businesses_name)
# ["Barber's Point", 'Soho NYC Barbers', 'Ace of Cuts Barber Shop', '12 Pell', 'On the Mark Barbershop', 'DaZhong Barber Shop', 'The Kinsman Barber Shop', 'Big Apple Barbers', 'Barber on Pearl', 'East 6th Street Barber Shop', 'Rafaels Barbershop', 'Well Connected', 'Park Ave Barbershop', 'Cutting Edge Barbers', 'The Flying Row', 'East Village Barber Shop', 'Thee Brooklyn Barber', 'Euro Barber Shop', 'Hairrari East Village', 'Tuft']


businesses_rate_45 = [business["name"]
                      for business in businesses if business["rating"] > 4.5]
print(businesses_rate_45)
# ["Barber's Point", 'Soho NYC Barbers', '12 Pell', 'Euro Barber Shop', 'Hairrari East Village']
