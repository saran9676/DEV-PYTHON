# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0Kq5hzHPJwX4ovZAt1xv9qq948zfAjTl6SYnEcG-3NipeXJu5Z-hJQznH12GFd5FhaZ4ch0X3NrBM8K9iepcaLo76gnV_Ul8xHXiPZ3i2u_xhRDu--WkCzQJrvFBz7RYXSOdm6_LASbecvQkXTXROv7RO5tVhcUDIGUI-XZWqahw=D4545826"

auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AB"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))