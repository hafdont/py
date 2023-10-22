import requests
import os

# Replace with your GitHub username and personal access token
username = ""
token = " "

# Fetch a list of your GitHub repositories
url = f"https://api.github.com/users/hafdont/repos"
headers = {"Authorization": f"token {token}"}
response = requests.get(url, headers=headers)
repos = response.json()

# Clone each repository
for repo in repos:
    repo_name = repo["name"]
    repo_url = repo["clone_url"]
    os.system(f"git clone {repo_url}")
