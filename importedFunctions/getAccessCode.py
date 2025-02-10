from flask import session, request
import requests

accessCodeEndpoint = "https://github.com/login/oauth/access_token"

def getAccessCode(authCode):
    
    payload = {
        "client_id": session.get("clientId"),
        "client_secret": session.get("clientSecret"),
        "code": authCode,
        "redirect_uri": request.host_url + "callback"
    }

    headers = {
        "Accept": "application/json"
    }

    accessRespose = requests.post(accessCodeEndpoint, headers=headers, data=payload)

    if accessRespose.status_code == 200:
        return accessRespose.json()
    else:
        return f"Error: {accessRespose.text}", 400