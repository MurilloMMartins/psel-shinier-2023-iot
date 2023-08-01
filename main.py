import git
import subprocess

def checkForCommitChanges(repository:git.Repo):
    activeBranch = repository.active_branch

    localCommits = list(repository.iter_commits(activeBranch))
    remoteCommits = list(repository.iter_commits(f'origin/{activeBranch}'))

    lastLocalCommit = localCommits[0]
    lastRemoteCommit = remoteCommits[0]

    return lastLocalCommit != lastRemoteCommit

def checkForChangesInRemote(repository:git.Repo):
    for remote in repository.remotes:
        remote.fetch()
    
    return checkForCommitChanges(repository)

def pullToLocalRepository(repository:git.Repo):
    repository.git.reset('--hard')
    repository.remotes.origin.pull()

def AutoUpdateProgram(repository:git.Repo):
    if checkForChangesInRemote(repository):
        print("Changes in remote detected! Pulling to local repository.")
        pullToLocalRepository(repository)
        
        print("Restarting process!")
        subprocess.Popen(['python', __file__])
    else:
        print("Repository up to date.")

def main():
    repo = git.Repo('./')
    try:
        AutoUpdateProgram(repo)
    except git.GitCommandError as err:
        print(f"Unexpected error of type {type(err)}:\n {err}")
        exit(1)

if __name__ == "__main__":
    main()
