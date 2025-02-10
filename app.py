from flask import Flask, render_template, request, session, redirect
from importedFunctions.createGitIssue import creatingGithubIssue, creatingGithubIssue2
import os
from importedFunctions.githubAuth import githubAuth
from importedFunctions.getAccessCode import getAccessCode

app = Flask(__name__)
app.secret_key = os.urandom(10)

@app.route("/", methods=["POST", "GET"])
def homePage():
    requestMessage = None

    if request.method == "POST":
        pat = request.form["PAT"]
        orgName = request.form["ORGNAME"]
        repoName = request.form["REPONAME"]
        issueTitle = request.form["ISSUETITLE"]
        issueDesc = request.form["ISSUEDESC"]

        if pat and orgName and repoName and issueTitle and issueDesc:
            requestMessage = creatingGithubIssue(pat, orgName, repoName, issueTitle, issueDesc)
        else:
            requestMessage = "Make sure to fill out the form"
    
    return render_template("homePage.html", message=requestMessage)


@app.route("/gitHubIssues", methods=["POST", "GET"])
def gitHubIssues():
    requestMessage = None
    if "clientId" not in session and "clientSecret" not in session:
        return redirect("/githubInfo")
    
    if request.method == "POST":
        orgName = request.form["ORGNAME"]
        repoName = request.form["REPONAME"]
        issueTitle = request.form["ISSUETITLE"]
        issueDesc = request.form["ISSUEDESC"]

        if orgName and repoName and issueTitle and issueDesc:
            requestMessage = creatingGithubIssue2(orgName, repoName, issueTitle, issueDesc)
        else:
            requestMessage = "Make sure to fill out the form"
        
    return render_template("createGitHubIssues.html", message=requestMessage) 


@app.route("/githubInfo", methods=["POST", "GET"])
def githubInfoPage():

    if request.method == "POST":
        session["clientId"] = request.form["CLIENTID"]
        session["clientSecret"] = request.form["CLIENTSECRET"]
        return githubAuth()

        #return redirect("/delete")

    return render_template("githubInfo.html")


@app.route("/callback", methods=["POST", "GET"])
def callback():
    authCode = request.args.get("code")

    if not authCode:
        return "Testing, this will not work", 400
    
    return getAccessCode(authCode)

    #return render_template("callback.html", message=authCode)



@app.route("/delete")
def delete():
    gitId = session.get("clientId")
    gitSecrets = session.get("clientSecret")
    #request.host_url + "callback"
    #session.get("clientSecret")

    return render_template("delete.html", oauthid=gitId, oauthsecrets=gitSecrets)



if __name__ == "__main__":
    app.run(debug=True)#, use_reloader=False)
    #Restarting with stat - means that flask is starting a second process
    #turn debug to false when pushing to prod, use_reloader=False means when changes are made, it will not reload it, manually do it, cooked