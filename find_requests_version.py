import requests

print("requests version:", requests.__version__)

# get the google homepage with requests
response = requests.get("http://www.google.com/")
print(response)