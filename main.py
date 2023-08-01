import git
from autoupdate import AutoUpdateProgram

import tkinter as tk
from tkinter import ttk, messagebox

def onButtonClick():
    popup = tk.Toplevel()
    
    label = tk.Label(popup, text="Candidato processo seletivo Shinier IoT")
    label.pack(padx=30, pady=10, fill='both', expand=True)
    
    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack(pady=10, padx=10, ipadx=20)


def main():
    # repo = git.Repo('./')
    # try:
    #     AutoUpdateProgram(repo, __file__)
    # except Exception as err:
    #     print(f"Unexpected error of type {type(err)}:\n {err}")
    #     exit(1)

    # Creating Tkinter Root
    root = tk.Tk()
    root.title('Psel-Shinier-2023-IoT')
    root.geometry('400x225')

    # Creating frame that will have all UI elements
    frame = ttk.Frame(master=root, borderwidth=1)
    frame.grid(column=0, row=0)

    # Configuring frame responsivity
    frame.columnconfigure(0, weight=1, minsize=0)
    frame.rowconfigure(0, weight=1, minsize=0)
    frame.rowconfigure(1, weight=1, minsize=0)
    frame.rowconfigure(2, weight=1, minsize=0)

    # Configuring root responsivity
    root.columnconfigure(0, weight=1, minsize=0)
    root.rowconfigure(0, weight=1, minsize=0)

    # UI elements
    label = ttk.Label(master=frame, text="Nome do candidato")
    input = ttk.Entry(master=frame)
    button = ttk.Button(master=frame, text="Inserir", command=onButtonClick)

    # Placing elements on Frame
    label.grid(column=0, row=0, padx=5, pady=5)
    input.grid(column=0, row=1, padx=5, pady=5)
    button.grid(column=0, row=2, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
