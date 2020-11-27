from github import Github

g = Github()

username = "phadej"

user = g.get_user(username)

repos = user.get_repos()
total_repos = 0
for repo in repos:
    total_repos = total_repos + 1

print("Github User Statistics:", username)
print("Total Repositories:", total_repos)
