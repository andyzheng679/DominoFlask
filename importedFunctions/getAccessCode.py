from flask import session, request, redirect, url_for
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
        session["accessCode"] = accessRespose.json().get("access_token")
        return redirect(url_for("gitHubIssues"))
        #return accessRespose.json().get()
    else:
        return f"Error: {accessRespose.text}", 400