import git
import subprocess

def AutoUpdateProgram(repository:git.Repo, main_file_path:str):
    if CheckForChangesInRemote(repository):
        print("Changes in remote detected! Pulling to local repository.")
        PullToLocalRepository(repository)
        
        print("Restarting process!")
        subprocess.Popen(['python', main_file_path])

        return True
    else:
        print("Repository up to date.")
        return False

def PullToLocalRepository(repository:git.Repo):
    active_branch = repository.active_branch
    repository.git.reset('--hard', f'origin/{active_branch}')
    repository.remotes.origin.pull()
    
def CheckForChangesInRemote(repository:git.Repo):
    for remote in repository.remotes:
        remote.fetch()
    
    return CheckForCommitChanges(repository)

def CheckForCommitChanges(repository:git.Repo):
    active_branch = repository.active_branch

    local_commits = list(repository.iter_commits(active_branch))
    remote_commits = list(repository.iter_commits(f'origin/{active_branch}'))

    last_local_commit = local_commits[0]
    last_remote_commit = remote_commits[0]

    return last_local_commit != last_remote_commit