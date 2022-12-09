"""Auth"""
import jwt

ISSUER = "sample-auth-server"

with open("public.pem", "rb") as f:
    public_key = f.read()


def verify_access_token(access_token):
    """Decode the access token"""
    try:
        jwt.decode(access_token.encode(), public_key, issuer=ISSUER, algorithms="RS256")
    except (
        jwt.exceptions.InvalidTokenError,
        jwt.exceptions.InvalidSignatureError,
        jwt.exceptions.InvalidIssuerError,
        jwt.exceptions.ExpiredSignatureError,
    ):
        return False

    return True
