# palo_alto_api
Palo Alto API call (python)

In this project, we are going to get Palo Alto PAN-OS and Panorama settings via API.

# API key
You need to get your API key via the following http API call:

```
curl -H "Content-Type: application/x-www-form-urlencoded" -X POST https://firewall/api/?type=keygen -d 'user=<user>&password=<password>'
```

# Dependencies: requests
These Dependencies need to be installed.

```
    pip install -r requirements.txt
```