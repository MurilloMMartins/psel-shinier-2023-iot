import git

def checkForChangesInRemote(repository:git.Repo):
    activeBranch = repository.active_branch

    localCommits = list(repository.iter_commits(activeBranch))
    remoteCommits = list(repository.iter_commits(f'origin/{activeBranch}'))

    # we don't need to sort these lists to compare them
    return localCommits != remoteCommits

def main():
    repo = git.Repo('./')
    if checkForChangesInRemote(repo):
        print("Changes in remote detected!")
    else:
        print("Repository up to date.")

if __name__ == "__main__":
    main()