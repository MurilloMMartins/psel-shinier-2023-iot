import tkinter as tk
from tkinter import ttk

def CreateApplicatinGUI():
    # Creating Tkinter Root
    root = tk.Tk()
    root.title('Psel-Shinier-2023-IoT')
    root.geometry('400x225')
    # Creating frame that will have all UI elements
    frame = ttk.Frame(master=root, borderwidth=1)
    frame.grid(column=0, row=0)
    ConfigureUIResponsivity(root, frame)

    label, input, button = CreateUIElements(frame)
    PlaceUIElementsOnFrame(frame, label, input, button)

    return root

def ConfigureUIResponsivity(root:tk.Tk, frame:tk.Frame):
    # Configuring root responsivity
    root.columnconfigure(0, weight=1, minsize=0)
    root.rowconfigure(0, weight=1, minsize=0)
    # Configuring frame responsivity
    frame.columnconfigure(0, weight=1, minsize=0)
    frame.rowconfigure(0, weight=1, minsize=0)
    frame.rowconfigure(1, weight=1, minsize=0)
    frame.rowconfigure(2, weight=1, minsize=0)

def PlaceUIElementsOnFrame(frame:tk.Frame, *elements):
    for index, element, in enumerate(elements):
        element.grid(column=0, row=index, padx=5, pady=5)

def CreateUIElements(frame:tk.Frame):
    # UI elements
    label = ttk.Label(master=frame, text="Nome do candidato")
    input = ttk.Entry(master=frame)
    button = ttk.Button(master=frame, text="Inserir", command=lambda: OnButtonClick(input.get()))

    return label, input, button

def OnButtonClick(candidate:str):
    popup = tk.Toplevel()
    
    label = tk.Label(popup, text=candidate + ", candidato processo seletivo Shinier IoT")
    button = tk.Button(popup, text="OK", command=popup.destroy)

    label.pack(padx=30, pady=10, fill='both', expand=True)
    button.pack(pady=10, padx=10, ipadx=20)