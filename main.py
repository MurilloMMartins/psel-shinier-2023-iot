import git
from autoupdate import AutoUpdateProgram
from applicationGUI import createApplicatinGUI

def main():
    # repo = git.Repo('./')
    # try:
    #     AutoUpdateProgram(repo, __file__)
    # except Exception as err:
    #     print(f"Unexpected error of type {type(err)}:\n {err}")
    #     exit(1)

    root = createApplicatinGUI()
    root.mainloop()

if __name__ == "__main__":
    main()
