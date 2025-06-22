# AUTO GENARATED, DO NOT TRY TO MODIFY
# sigmas
GIT_COMMITT = "06da0ebead4c15fc91f09efe9d4307edeeb5076d"
COMMIT_DATE = "2025-06-22 09:28:22 -0400"

from github import Github

g = Github()
repo = g.get_repo("lutionhq/lution")
ltcommit = repo.get_commits()[1]
if ltcommit.sha == GIT_COMMITT:
    GIT_COMMIT = f"{GIT_COMMITT} (outdated)"
else:
    GIT_COMMIT = GIT_COMMITT

