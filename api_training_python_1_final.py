import requests
import json

thoughtspot_url = 'https://yourinstance.thoughtspot.cloud')
api_version = '2.0'
base_url = '{thoughtspot_url}/api/rest/{version}/'.format(thoughtspot_url=thoughtspot_url, version=api_version)
# Add additional headers for specific request if necessary
api_headers = {
    'X-Requested-By': 'ThoughtSpot', 
    'Accept': 'application/json'
}

requests_session = requests.Session()
# Set the headers for all uses of the requests_session object
requests_session.headers.update(api_headers)

# url is base_url + endpoint
endpoint = "auth/token/full"
url = base_url + endpoint

# JSON request as Python Dict
json_post_data = {
  "username": "yourusername",
  "password": "y0urP@ssword",
  "validity_time_in_sec": 3600,
  "org_id": 0,
  "auto_create": False  # make sure to uppercase in Python
}

try:
    # requests returns back Response object with various properties and methods
    resp = requests_session.post(url=url, json=json_post_data)
    # This method causes Python Exception to throw if the response status is not 2XX
    resp.raise_for_status()
    # Retrieve the JSON body of response and convert into Python Dict
    # If a call (like a DELETE) returns 204 instead of 200, with no body, this may cause error
    resp_json = resp.json()
    # You can just print(resp_json) to see the Python Dict
    print(json.dumps(resp_json, indent=2))
    # 'token' property of the response is the Bearer Token to use
    token = resp_json["token"]

    # Update the api_headers from before with a new header for the Bearer token
    api_headers['Authorization'] = 'Bearer {}'.format(token)
    requests_session.headers.update(api_headers)
    # Now we can use the requests_session object to issue any other command we'd like
    
except requests.exceptions.HTTPError as e:
    print("Requests")
    print(e)
    print(e.request)
    print(e.request.url)
    print(e.request.headers)
    print(e.request.body)
    print(e.response.content)
