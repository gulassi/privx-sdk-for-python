# An example how to use PrivX API for role creation.
# Requires Python 3.6+

import sys

import config

# this importation for demonstration purpose only
# for proper importation of privx_api module
# see https://github.com/SSHcom/privx-sdk-for-python#getting-started
try:
    # Running example with pip-installed SDK
    import privx_api
except ImportError:
    # Running example without installing SDK
    from utils import load_privx_api_lib_path

    load_privx_api_lib_path()
    import privx_api

# Initialize the API.
api = privx_api.PrivXAPI(
    config.HOSTNAME,
    config.HOSTPORT,
    config.CA_CERT,
    config.OAUTH_CLIENT_ID,
    config.OAUTH_CLIENT_SECRET,
)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate(config.API_CLIENT_ID, config.API_CLIENT_SECRET)

# Get sources.
sourceID = ""
resp = api.get_sources()
if resp.ok:
    # Select wanted source, "Local users" for example.
    for item in resp.data["items"]:
        if item["name"] == "Local users":
            sourceID = item["id"]
else:
    print(resp.data)
    sys.exit(1)


if sourceID == "":
    print("did not find source ID")
    sys.exit(1)


# Create role.
data = {
    "name": "testrole",
    "source_rules": {
        "type": "GROUP",
        "match": "ANY",
        "rules": [
            {"type": "RULE", "source": sourceID, "search_string": "(cn=testuser)"}
        ],
    },
}
resp = api.create_role(data)
if resp.ok:
    print("Role created.")
else:
    print("Role creation failed.")
    print(resp.data)
