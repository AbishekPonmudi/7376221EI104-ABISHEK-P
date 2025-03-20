# Writtent By ABishek - 7376221EI104 - AFFORDMED 

#This is for authn Purpoe only
import requests

# url = "http://20.244.56.144/test/register"
url = "http://20.244.56.144/test/auth"

data = {
    "companyName": "goMart",
    "clientID"   : "null",   # -> Hided confidential
    "clientSecret":"null",   # -> Hided confidential
    "OwnerName"  : "Abishek",
    "ownerEmail" : "null",   # -> Hided confidential
    "rollNo"     : "null",    # -> Hided confidential
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
