import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/3/project"
API_TOKEN="ATATT3xFfGF0Kq5hzHPJwX4ovZAt1xv9qq948zfAjTl6SYnEcG-3NipeXJu5Z-hJQznH12GFd5FhaZ4ch0X3NrBM8K9iepcaLo76gnV_Ul8xHXiPZ3i2u_xhRDu--WkCzQJrvFBz7RYXSOdm6_LASbecvQkXTXROv7RO5tVhcUDIGUI-XZWqahw=D4545826"
auth = HTTPBasicAuth("saranbukk448@gmail.com",API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))