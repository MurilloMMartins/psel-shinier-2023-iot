import git

def checkForCommitChanges(repository:git.Repo):
    activeBranch = repository.active_branch

    localCommits = list(repository.iter_commits(activeBranch))
    remoteCommits = list(repository.iter_commits(f'origin/{activeBranch}'))

    # we don't need to sort these lists to compare them
    return localCommits != remoteCommits

def checkForChangesInRemote(repository:git.Repo):
    for remote in repository.remotes:
        remote.fetch()
    
    return checkForCommitChanges(repository)


def main():
    repo = git.Repo('./')
    if checkForChangesInRemote(repo):
        print("Changes in remote detected!")
        print("Pulling from local repository")
        try:
            repo.git.reset('--hard')
            repo.remotes.origin.pull()
        except git.GitCommandError as err:
            print(f"Unexpected error of type {type(err)}:\n {err}")
            exit
    else:
        print("Repository up to date.")

if __name__ == "__main__":
    main()
