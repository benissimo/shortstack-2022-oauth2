# Best Practices

## Lean on Your Team(s)

- Talk with your relevant Platform, DevOps, and Infosec teams.

![not-alone](./assets/not-alone.png)

## Authorization Code Flow

- Use the Authorization Code Flow!
- Always recommended over the implicit flow, regardless of whether the client is public or confidential

Previously, Authorization Code Flow couldn't be implemented with public clients because it exposes the client secret.

So use PKCE!

## Requiring State

Now recommended in OAuth 2.0 RFC

- The Client generates a sufficiently large random value and stores it in the User-Agent (could be browser cookies)
- During Oauth 2.0 flow, Client introduces an additional state parameter in it's request to the Authorization server
- When the Authorization Server responds to the client with an access token or Authorization Code, it includes the same State parameter it was given
- Client must validate that the "state" parameter that was sent equals the "state" parameter that is stored locally in the user agent.
- If state parameters don't match, client should exit the flow.

## Good Hygiene

### Don't Run Containers as Root

<https://amazic.com/get-the-evil-out-dont-run-containers-as-root/>

![root](./assets/root.png)

### Multi-Stage Docker Builds

If you run with an extremely slim (or even distroless!) image, the attack surface of the application is greatly reduced

### Keep Packages Updated

Tools like Snyk and Github's Dependabot
