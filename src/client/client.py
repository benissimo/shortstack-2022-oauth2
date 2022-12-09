"""Front end, handle login and callback url"""
import json
import requests

from flask import Flask, make_response, render_template, redirect, request, url_for

REDIRECT_URL = "http://127.0.0.1:5050/callback"
AUTH_PATH = "http://127.0.0.1:5051/auth"
TOKEN_PATH = "http://127.0.0.1:5051/token"
RES_PATH = "http://127.0.0.1:5052/users"

CLIENT_ID = "shortstack"
CLIENT_SECRET = "shortstack"

app = Flask(__name__)


@app.before_request
def before_request():
    """Redirects user to the login page if access token is not present"""

    if request.endpoint not in ["login", "callback"]:
        access_token = request.cookies.get("access_token")
        if access_token:
            return None

        return redirect(url_for("login"))


@app.route("/")
def main():
    """Retrieve a list of users"""

    access_token = request.cookies.get("access_token")

    req = requests.get(
        RES_PATH, headers={"Authorization": "Bearer {}".format(access_token)}
    )

    if req.status_code != 200:
        return (
            json.dumps(
                {"error": "The resource server returns an error: \n{}".format(req.text)}
            ),
            500,
        )

    users = json.loads(req.text).get("results")

    return render_template("users.html", users=users)


@app.route("/login")
def login():
    """Present the login page"""

    return render_template(
        "AC_login.html", dest=AUTH_PATH, client_id=CLIENT_ID, redirect_url=REDIRECT_URL
    )


@app.route("/callback")
def callback():
    """Accept the authorization code and exchange it for an access token"""

    authorization_code = request.args.get("authorization_code")

    if not authorization_code:
        return json.dumps({"error": "No authorization code is received."}), 500

    r = requests.post(
        TOKEN_PATH,
        data={
            "grant_type": "authorization_code",
            "authorization_code": authorization_code,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_url": REDIRECT_URL,
        },
    )

    if r.status_code != 200:
        return (
            json.dumps(
                {
                    "error": "The authorization server returns an error: \n{}".format(
                        r.text
                    )
                }
            ),
            500,
        )

    access_token = json.loads(r.text).get("access_token")

    response = make_response(redirect(url_for("main")))
    response.set_cookie("access_token", access_token)
    return response


if __name__ == "__main__":
    app.run(port=5050, host="0.0.0.0")
