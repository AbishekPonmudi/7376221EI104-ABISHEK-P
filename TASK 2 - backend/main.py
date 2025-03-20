from fastapi import FastAPI, Path, Query
import requests

app = FastAPI()

urls_random = "http://20.244.56.144/test/users"


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQyNDQ2NDA5LCJpYXQiOjE3NDI0NDYxMDksImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjIzN2E2NTViLTQyOWQtNDE4My04MWQ1LTU3MGUzYWU2NGY2MSIsInN1YiI6ImFiaXNoZWsuZWkyMkBiaXRzYXRoeS5hYy5pbiJ9LCJjb21wYW55TmFtZSI6ImdvTWFydCIsImNsaWVudElEIjoiMjM3YTY1NWItNDI5ZC00MTgzLTgxZDUtNTcwZTNhZTY0ZjYxIiwiY2xpZW50U2VjcmV0Ijoicmtnd2R4Y1pFaHl1WWZIWSIsIm93bmVyTmFtZSI6IkFiaXNoZWsiLCJvd25lckVtYWlsIjoiYWJpc2hlay5laTIyQGJpdHNhdGh5LmFjLmluIiwicm9sbE5vIjoiNzM3NjIyMUVJMTA0In0.82zl8W9V6KX1L4qmfxW_las8YiCO0ley_mqlfMSSBKY"

headers = {
    "Authorization": f"Bearer {token}"
}

response1 = requests.get(urls_random, headers=headers)
print("Status Code:", response1.status_code)
print("Response Body:", response1.json())
