# python-oidc-sample

This is a very simple example of how to use Python to obtain an Access Token from an OpenID-connect/OAuth2 Token server.

Run `pipinstall.bat` to install python dependencies.

Use the accompanying IdentityServer to test against. This requires dotnet 5+ to be installed.

Just run `run-tokenserver.bat` to get it up and running.

Now just run `python oidc-test-client.py` to test the python app and see it printing out an access token.

**NOTE:**
The code does bypass Certificate Validation since a localhost self-signed cert is not recognized by Python as legit. Please do not use in your production code!