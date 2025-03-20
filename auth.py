import requests

# url = "http://20.244.56.144/test/register"
url = "http://20.244.56.144/test/auth"

data = {
    "companyName": "goMart",
    "clientID"   : "237a655b-429d-4183-81d5-570e3ae64f61",
    "clientSecret":"rkgwdxcZEhyuYfHY",
    "OwnerName"  : "Abishek",
    "ownerEmail" : "abishek.ei22@bitsathy.ac.in",
    "rollNo"     : "7376221EI104",
}

response = requests.post(url, json=data)


print("Status Code:", response.status_code)
print("Response Body:", response.text)
