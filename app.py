from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("homePage.html")

@app.route("/test")
def testing():
    return render_template("createGitHubIssues.html")






if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    #Restarting with stat - means that flask is starting a second process
    #turn debug to false when pushing to prod, use_reloader=False means when changes are made, it will not reload it, manually do it, cooked