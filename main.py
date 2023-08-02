import git, threading, time
from autoupdate import AutoUpdateProgram
from applicationGUI import CreateApplicatinGUI

autoupdate_wait_time_in_seconds = 2

def AutoUpdateThreadFunction(event:threading.Event):
    while not event.is_set():
        repo = git.Repo('./')

        try:
            AutoUpdateProgram(repo, __file__)
        except Exception as err:
            print(f"Unexpected error of type {type(err)}:\n {err}")
            exit(1)
        
        event.wait(timeout=autoupdate_wait_time_in_seconds)

def main():
    # Event that tells if the code is still running or not
    event = threading.Event()
    event.clear()

    # Autoupdate event thread
    autoupdate_thread = threading.Thread(target=AutoUpdateThreadFunction, args=(event, ))
    autoupdate_thread.start()

    # GUI
    root = CreateApplicatinGUI()
    root.mainloop()
    
    # Closing the system
    event.set()
    autoupdate_thread.join()

if __name__ == "__main__":
    main()