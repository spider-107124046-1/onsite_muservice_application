## Authentication using JWT

|HTTP Method|API Endpoint|Description|
|-----------|------------|-----------|
|POST|/register|Register new account with mail and password|
|POST|/login|Login with existing account and password|
|GET|/me|Get user info about self|
|POST|/refresh-token|Refresh authentication token|
|GET|/capabilities|Get the permissions/capabilities of the user within the scope of the app|