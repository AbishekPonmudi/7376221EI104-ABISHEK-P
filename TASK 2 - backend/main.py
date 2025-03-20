#written by Abishek 7376221EI104  - AFFORDMED TEST

"""QUESTIONS :
    Develope a Social Media Analytics HTTP Microservice
    """

#CODE FOR TEST SOCIAL MEDIA SERVER API'S

from fastapi import FastAPI, Path, Query
import requests

app = FastAPI()

# urls = "http://20.244.56.144/test/users"
urls = "http://20.244.56.144/test/users/1/posts"
# urls = "http://20.244.56.144/test/posts/150/comments"

# Temp TOken
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQyNDQ4NjYwLCJpYXQiOjE3NDI0NDgzNjAsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjIzN2E2NTViLTQyOWQtNDE4My04MWQ1LTU3MGUzYWU2NGY2MSIsInN1YiI6ImFiaXNoZWsuZWkyMkBiaXRzYXRoeS5hYy5pbiJ9LCJjb21wYW55TmFtZSI6ImdvTWFydCIsImNsaWVudElEIjoiMjM3YTY1NWItNDI5ZC00MTgzLTgxZDUtNTcwZTNhZTY0ZjYxIiwiY2xpZW50U2VjcmV0Ijoicmtnd2R4Y1pFaHl1WWZIWSIsIm93bmVyTmFtZSI6IkFiaXNoZWsiLCJvd25lckVtYWlsIjoiYWJpc2hlay5laTIyQGJpdHNhdGh5LmFjLmluIiwicm9sbE5vIjoiNzM3NjIyMUVJMTA0In0.uCGsE0fKrU6n_tzG7C4WJngQ_2OpCFB6rs8QLrbMpjg"

headers = {
    "Authorization": f"Bearer {token}"
}

response1 = requests.get(urls, headers=headers)
print("status code :", response1.status_code)
print("response body : ", response1.json())


# response = requests.get(urls,headers=headers)
# print("status code :" ,response.status_code)
# print("reponse body : ",response.json())