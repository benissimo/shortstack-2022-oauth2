
# Authentication System Security

<!-- TODO: break this up into multiple different files and link them here, similar to how we do the vimrc file -->

<https://github.com/michaelawyu/auth-server-sample>

## Tool Versions

| Tool | Description | Version |
| ---- | ----------- | ------- |
| Python | Language used | 3.10.2

## Tool Setup

### Rancher

### Docker

### Docker-Compose

### Python

## Best Practices

## OAuth 2.0

[Authorization Code Flows](./docs/authz-code-flows.md)

#### Resource Owner Password Credentials

#### Implicit

#### Client Credentials

```mermaid
    flowchart LR
    A(Resource Server) <--2. Client uses access token\n to access resource server-->
    B(Client) <--1. Client exchanges ID and secret\n for an access token-->
    D(Authorization Server);
```

## Attack Scenarios

### Improper Redirect URI

```mermaid
    sequenceDiagram
    participant Client Application
    participant Attack Server

    participant Authorization Server

    Client Application->>Authorization Server: /authorize? redirect_uri=https://example.com.attacker.com/callback
    Authorization Server->>Attack Server: HTTP 302\n https://example.com.attacker.com/callback/#access_token=eyJOe...
```
