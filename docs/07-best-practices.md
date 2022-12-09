# Best Practices

## Lean on Your Team(s)

- Talk with your relevant Platform, DevOps, and Infosec teams.

![not-alone](./assets/not-alone.png)

- Use the Authorization Code Flow!
- Always recommended over the implicit flow, regardless of whether the client is public or confidential

Previously, Authorization Code Flow couldn't be implemented with public clients because it exposes the client secret.

So use pixie!

## Good Hygeine

### Don't Run Containers as Root

<https://amazic.com/get-the-evil-out-dont-run-containers-as-root/>

![root](./assets/root.png)

### Multi-Stage Docker Builds

If you run with an extremely slim (or even distroless!) image, the attack surface of the application is greatly reduced

### Keep Packages Updated

Tools like Snyk and Github's Dependabot
