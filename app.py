from flask import Flask, render_template, request, session, redirect
from importedFunctions.createGitIssue import creatingGithubIssue
import os
from importedFunctions.githubAuth import githubAuth
from importedFunctions.getAccessCode import getAccessCode

app = Flask(__name__)
app.secret_key = os.urandom(10)


@app.route("/", methods=["POST", "GET"])
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
            requestMessage = creatingGithubIssue(orgName, repoName, issueTitle, issueDesc)
        else:
            requestMessage = "Make sure to fill out the form"
        
    return render_template("createGitHubIssues.html", message=requestMessage) 


@app.route("/githubInfo", methods=["POST", "GET"])
def githubInfoPage():

    if request.method == "POST":
        session["clientId"] = request.form["CLIENTID"]
        session["clientSecret"] = request.form["CLIENTSECRET"]
        return githubAuth()

    return render_template("githubInfo.html")


@app.route("/callback", methods=["POST", "GET"])
def callback():
    authCode = request.args.get("code")

    if not authCode:
        return "No code", 400
    
    return getAccessCode(authCode)





if __name__ == "__main__":
    app.run(debug=True)#, use_reloader=False)
    #Restarting with stat - means that flask is starting a second process
    #turn debug to false when pushing to prod, use_reloader=False means when changes are made, it will not reload it, manually do it, cooked