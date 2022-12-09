# Attacks

## CSRF

- Entice a victim user to browse a Client URL that contains the Access Token or Authorization Code of the attacker, integrating the attackers account
- Most of the time this scenario is benign, but context can increase risk.

- Scenario - user has integrated their paypal account with the client, which they use to withdraw money from the Paypal account
- If CSRF was possible, the attacker could integrate their own paypal account with the victims Client account.

## Clickjacking

Social Engineering attacks which trick users into clicking buttons that perform sensitive actions

Embed the vulnerable page within an attacker's page using an HTML iframe

## XSS

### URI Redirect

```mermaid
    flowchart LR
    A(Resource Server) <--2. Client uses access token\n to access resource server-->
    B(Client) <--1. Client exchanges ID and secret\n for an access token-->
    D(Authorization Server);
```

```mermaid
    sequenceDiagram
    participant Client Application
    participant Attack Server

    participant Authorization Server

    Client Application->>Authorization Server: /authorize? redirect_uri=https://example.com.attacker.com/callback
    Authorization Server->>Attack Server: HTTP 302\n https://example.com.attacker.com/callback/#access_token=eyJOe...
```

## Demo - Compromised Authorization Code

If following along with the presentation:

`docker-compose up`

```Bash
curl -H "Authorization: Bearer <bearer token>" http://localhost:5052/users
```

Example

```Bash
curl -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzYW1wbGUtYXV0aC1zZXJ2ZXIiLCJleHAiOjE2NzA2MDMyODkuMTY0MDY0fQ.GBj45okfAdaNVWgMQ2m7m1KVR_mG7yNnSmDX3BHTdIFfy4GTMrjY3_moRmUK9anzDZuNmEdJ2bOUBTexK_CF5Qqf2rDA7J6JbEacfNf5QVnST7OV2JM8Fgxazos8YAlAVCcMH7spOlKiJ2RGZ9-QnILvy_oqy8dKRxdnl9El4-NFYSyKmsBhJ-HGv-uGR8ZZTTMvr6JJKuVKZ4kYOw4I-9RWH4O4l6Rt3Pvmi9ehQ9o-S-YdHGsQ5MUkdscpIn0nbgko3MggRscmJKZzJNRHGf7yk_ZdL3_jk3k30iGLpNDLDnztxoqOeWdHIE2fg81M83dEufuYrDfCZiaTySdF5w" http://localhost:5052/users
```
