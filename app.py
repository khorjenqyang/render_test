import requests

url = "https://prod-31.westus.logic.azure.com:443/workflows/c5992cc9e6604817bb7b0c43f140caf6/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=FE_r_MB-bngxY6pXWJb7XO36XDv9JEnJYktkyeMzw8c"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())  # or response.text
else:
    print(f"Error: {response.status_code}")