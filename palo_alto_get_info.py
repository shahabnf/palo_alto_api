import requests
import xml.etree.ElementTree as ET


# Read API key from "api_key.txt" file
api_key = open('api_key.txt','r').read()

firewall_ip_add = input("Plaese enter firewall's IP address: ")
# firewall_ip_add = "192.168.91.201"

base_url = "https://" + firewall_ip_add + "/api/?type=op&cmd=<show><system><info></info></system></show>&key="

complete_url = base_url + api_key
# print(complete_url)

api_response = requests.get(complete_url, verify=False)
# print(api_response)

# result_in_json = api_response.text
# print(result_in_json)

# Check if the request was successful (status code 200)
if api_response.status_code == 200:
    # Parse the XML response
    xml_data = api_response.text
    root = ET.fromstring(xml_data)

    # Extract the relevant data from the XML response
    # You can access specific elements and attributes as needed
    system_info = root.find(".//system")

    # Convert the extracted data to a dictionary or any other format as needed
    result_data = {
        "hostname": system_info.findtext("hostname"),
        "serial_number": system_info.findtext("serial"),
        "ip-address": system_info.findtext("ip-address"),
        "mgt_mac_address": system_info.findtext("mac-address"),
        "uptime": system_info.findtext("uptime"),
        "sw-version": system_info.findtext("sw-version"),
        "app-version": system_info.findtext("app-version"),
        "vm-uuid": system_info.findtext("vm-uuid"),
        # Add more data fields as needed
    }

    # Print or use the result_data dictionary
    print(result_data)
else:
    print(f"Failed to retrieve data. Status code: {api_response.status_code}")

