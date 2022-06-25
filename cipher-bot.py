import requests
from requests.structures import CaseInsensitiveDict

print("""
Cipher bot is only enabling the following TLS 1.2 ciphers: 
ECDHE-ECDSA-AES128-GCM-SHA256
ECDHE-ECDSA-CHACHA20-POLY1305
ECDHE-ECDSA-AES256-GCM-SHA384
ECDHE-RSA-AES128-GCM-SHA256
ECDHE-RSA-CHACHA20-POLY1305
ECDHE-RSA-AES256-GCM-SHA384
""")

zoneid = input("Insert Zone ID: ")
token = input("Insert Bearer token: ")

url = f"https://api.cloudflare.com/client/v4/zones/{zoneid}/settings/ciphers"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"
headers["Content-Type"] = "application/json"
resp = requests.get(url, headers=headers)

print("\nCurrently:")
print(resp.text)

payload = {
    "value": [
        "ECDHE-ECDSA-AES128-GCM-SHA256",
        "ECDHE-ECDSA-CHACHA20-POLY1305",
        "ECDHE-ECDSA-AES256-GCM-SHA384",
        "ECDHE-RSA-AES128-GCM-SHA256",
        "ECDHE-RSA-CHACHA20-POLY1305",
        "ECDHE-RSA-AES256-GCM-SHA384"
    ]
}
resp = requests.patch(url, headers=headers, json=payload)

print("\nAfter:")
print(resp.text)
