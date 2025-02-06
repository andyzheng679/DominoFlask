import requests


def creatingGithubIssue(pat,orgName, repoName, issueTitle, issueDesc):
    endpoint = "https://api.github.com/repos/{owner}/{repo}/issues"
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