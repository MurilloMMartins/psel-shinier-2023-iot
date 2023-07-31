import git

def checkForChangesInRemote(repository:git.Repo):
    currentBranch = repository.active_branch

    localCommits = list(repository.iter_commits(currentBranch))
    remoteCommits = list(repository.iter_commits(f'origin/{currentBranch}'))

    return localCommits != remoteCommits

def main():
    repo = git.Repo('./')
    if checkForChangesInRemote(repo):
        print("Changes in remote detected!")
    else:
        print("Repository up to date.")
    

if __name__ == "__main__":
    main()