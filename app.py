from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def homePage():
    if request.method == "POST":
        pat = request.form["PAT"]
        orgName = request.form["ORGNAME"]
        repoName = request.form["REPONAME"]
        issueTitle = request.form["ISSUETITLE"]
        issueDesc = request.form["ISSUEDESC"]

        return render_template("testing.html")
    
    return render_template("homePage.html")

@app.route("/test")
def testing():
    return render_template("createGitHubIssues.html")






if __name__ == "__main__":
    app.run(debug=True)#, use_reloader=False)
    #Restarting with stat - means that flask is starting a second process
    #turn debug to false when pushing to prod, use_reloader=False means when changes are made, it will not reload it, manually do it, cooked