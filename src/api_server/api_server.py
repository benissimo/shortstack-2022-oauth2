"""API Server"""
import json

from flask import Flask, request
from auth import verify_access_token

app = Flask(__name__)


@app.before_request
def before_request():
    """Check if the access token is present and valid"""

    auth_header = request.headers.get("Authorization")
    print("Auth header: ", auth_header, flush=True)

    if "Bearer" not in auth_header:
        return json.dumps({"error": "Access token does not exist."}), 400

    access_token = auth_header[7:]

    if access_token and verify_access_token(access_token):
        pass
    else:
        return json.dumps({"error": "Access token is invalid."}), 400


@app.route("/users", methods=["GET"])
def get_user():
    """Return a list of users"""

    users = [
        {"username": "Jane Doe", "email": "janedoe@example.com"},
        {"username": "John Doe", "email": "johndoe@example.com"},
    ]

    return json.dumps({"results": users})


if __name__ == "__main__":
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    # context.load_cert_chain('domain.crt', 'domain.key')
    # app.run(port = 5000, debug = True, ssl_context = context)
    app.run(port=5052, debug=True)
