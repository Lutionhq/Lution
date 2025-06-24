# AUTO GENERATED, DO NOT MODIFY
# sigmas
GIT_COMMITT = "a925d939fabf402cecbb8bbad319b7f942a196af"
COMMIT_DATE = "2025-06-24 06:20:14 +0700"

import os
import time
from github import Github

CACHE_FILE = ".latest_commit_cache"
CACHE_TTL = 300  # seconds

def get_cached_commit():
    if os.path.exists(CACHE_FILE):
        age = time.time() - os.path.getmtime(CACHE_FILE)
        if age < CACHE_TTL:
            with open(CACHE_FILE, "r") as f:
                return f.read().strip()
    return None

def update_cache(sha):
    with open(CACHE_FILE, "w") as f:
        f.write(sha)

cached_commit = get_cached_commit()
if cached_commit is None:
    g = Github()
    repo = g.get_repo("lutionhq/lution")
    latest_commit = repo.get_commits()[0].sha
    update_cache(latest_commit)
else:
    latest_commit = cached_commit

if latest_commit.startswith(GIT_COMMITT):
    GIT_COMMIT = GIT_COMMITT
else:
    GIT_COMMIT = f"{GIT_COMMITT} (outdated)"


