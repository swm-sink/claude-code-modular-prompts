# Example: Analyzing Code with `/query`

The `/query` command is a powerful tool for analyzing your codebase without making any modifications. You can use it to ask questions, understand how different parts of your system work, and find specific pieces of information.

## Scenario

You're a new developer on a project, and you've been tasked with fixing a bug in the authentication system. Before you start making changes, you want to understand how authentication is currently handled.

## Usage

You can use the `/query` command to ask a high-level question about the authentication system:

```bash
/query "how is authentication handled in this project?"
```

## Expected Output

The `/query` command will perform a parallel search and analysis of your codebase and then synthesize the results into a clear, structured report. The output might look something like this:

> 🤖 **Authentication Analysis**
>
> Here's a summary of how authentication is handled in this project:
>
> *   **Primary Method**: JWT tokens with Passport.js middleware.
> *   **Key Files**:
>     *   `src/middleware/auth.js`: Contains the main authentication middleware.
>     *   `src/services/tokenService.js`: Handles the creation and verification of JWTs.
>     *   `config/passport.js`: Configures the Passport.js strategy.
> *   **Workflow**:
>     1.  A user logs in via the `/api/login` endpoint.
>     2.  The `tokenService` generates a JWT.
>     3.  The JWT is sent back to the client.
>     4.  The client includes the JWT in the `Authorization` header for all subsequent requests.
>     5.  The `auth.js` middleware verifies the JWT and attaches the user to the request object.

This kind of detailed, context-aware analysis can save you hours of manual code exploration and help you get up to speed on a new project much more quickly. 