from flask import session, request, redirect

def githubAuth():
    redirectUri = request.host_url + "callback"
    clientId = session.get("clientId")
    holder = f"?client_id={clientId}&scope=repo&redirect_uri={redirectUri}"
    oAuthEndpoint = "https://github.com/login/oauth/authorize" + holder

    #make sure in github, the oauth is the same as the redirect here

    return redirect(oAuthEndpoint)
    