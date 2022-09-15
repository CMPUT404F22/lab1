import requests

print("requests version:", requests.__version__)

# get the google homepage with requests
response = requests.get("http://www.google.com/")
print(response)

# download this script from github and print itself
url_on_github = "https://raw.githubusercontent.com/CMPUT404F22/lab1/master/find_requests_version.py"
response = requests.get(url_on_github)
print(response.text)