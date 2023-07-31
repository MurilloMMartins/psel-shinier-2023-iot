import git

def checkForCommitChanges(repository:git.Repo):
    activeBranch = repository.active_branch

    localCommits = set(repository.iter_commits(activeBranch))
    remoteCommits = set(repository.iter_commits(f'origin/{activeBranch}'))

    return not remoteCommits.issubset(localCommits)

def checkForChangesInRemote(repository:git.Repo):
    for remote in repository.remotes:
        remote.fetch()
    
    return checkForCommitChanges(repository)

def updateRepository(repository:git.Repo):
    repository.git.reset('--hard')
    repository.remotes.origin.pull()

def main():
    repo = git.Repo('./')
    if checkForChangesInRemote(repo):
        print("Changes in remote detected!")
        print("Pulling from local repository")
        try:
            updateRepository(repo)
        except git.GitCommandError as err:
            print(f"Unexpected error of type {type(err)}:\n {err}")
            exit()
    else:
        print("Repository up to date.")

if __name__ == "__main__":
    main()
