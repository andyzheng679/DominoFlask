import requests
from flask import session

endpoint = "https://api.github.com/repos/{owner}/{repo}/issues"

def creatingGithubIssue(pat,orgName, repoName, issueTitle, issueDesc):
    realEndpoint = endpoint.replace("{owner}", orgName).replace("{repo}", repoName)

    headers = {
        "Authorization": f"token {pat}"
    }

    body = f"""Description: {issueDesc}"""
    
    payload = {
        "title": f"{issueTitle}",
        "body": body
    }

    postResponse = requests.post(realEndpoint, json=payload, headers=headers)

    if postResponse.status_code == 201:
        return "Github Issue Created"
    else:
        return f"Error: {postResponse.text}"
    

def creatingGithubIssue2(orgName, repoName, issueTitle, issueDesc):
    realEndpoint = endpoint.replace("{owner}", orgName).replace("{repo}", repoName)

    headers = {
        "Authorization": f"Bearer {session.get("accessCode")}"
    }
    body = f"""Description: {issueDesc}"""
    
    payload = {
        "title": f"{issueTitle}",
        "body": body
    }

    postResponse = requests.post(realEndpoint, json=payload, headers=headers)

    if postResponse.status_code == 201:
        return "Github Issue Created"
    else:
        return f"Error: {postResponse.text}"
