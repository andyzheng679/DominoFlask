from flask import Flask, render_template, request
from importedFunctions.createGitIssue import creatingGithubIssue

app = Flask(__name__)

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

@app.route("/test")
def testing():
    return render_template("createGitHubIssues.html")






if __name__ == "__main__":
    app.run(debug=True)#, use_reloader=False)
    #Restarting with stat - means that flask is starting a second process
    #turn debug to false when pushing to prod, use_reloader=False means when changes are made, it will not reload it, manually do it, cooked