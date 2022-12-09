# Best Practices

## Lean on Your Team(s)

![not-alone](./assets/not-alone.png)

Talk with your relevant Platform, DevOps, and Infosec teams.

Use the authorization code flow!

Always recommended over the implicit flow, regardless of whether the client is public or confidential

Previously, auth code flow couldn't be implemented with public clients because it exposes the client secret.

So use pixie!

- Access token Is never placed in a URL
- Access Token can be concealed from user agent
- Confidential Clients identify themselves with a Client Secret

PKCE extends the Oauth 2.0 framework, and adds additional security and allows public clients to perform the authorization code flow

PKCE RFC: <https://tools.ietf.org/html/rfc7636>

- Let's public clients use the Authorization Code flow rather than the implicit flow, even though they can't secure a client secret
- Mitigates the impact of a compromised Authorization Code by a malicious actor

## Good Hygeine

### Not running as root

![root](./assets/root.png)

### Multi-Stage Docker Builds

If you run with an extremely slim (or even distroless!) image, the attack surface of the application is greatly reduced

- Packages up to date
