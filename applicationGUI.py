import tkinter as tk
from tkinter import ttk

def createApplicatinGUI():
    # Creating Tkinter Root
    root = tk.Tk()
    root.title('Psel-Shinier-2023-IoT')
    root.geometry('400x225')
    # Creating frame that will have all UI elements
    frame = ttk.Frame(master=root, borderwidth=1)
    frame.grid(column=0, row=0)
    configureUIResponsivity(root, frame)

    label, input, button = createUIElements(frame)
    placeUIElementsOnFrame(frame, label, input, button)

    return root

def configureUIResponsivity(root:tk.Tk, frame:tk.Frame):
    # Configuring root responsivity
    root.columnconfigure(0, weight=1, minsize=0)
    root.rowconfigure(0, weight=1, minsize=0)
    # Configuring frame responsivity
    frame.columnconfigure(0, weight=1, minsize=0)
    frame.rowconfigure(0, weight=1, minsize=0)
    frame.rowconfigure(1, weight=1, minsize=0)
    frame.rowconfigure(2, weight=1, minsize=0)

def placeUIElementsOnFrame(frame:tk.Frame, *elements):
    for index, element, in enumerate(elements):
        element.grid(column=0, row=index, padx=5, pady=5)

def createUIElements(frame:tk.Frame):
    # UI elements
    label = ttk.Label(master=frame, text="Nome do candidato")
    input = ttk.Entry(master=frame)
    button = ttk.Button(master=frame, text="Inserir", command=onButtonClick)

    return label, input, button

def onButtonClick():
    popup = tk.Toplevel()
    
    label = tk.Label(popup, text="Candidato processo seletivo Shinier IoT")
    button = tk.Button(popup, text="OK", command=popup.destroy)

    label.pack(padx=30, pady=10, fill='both', expand=True)
    button.pack(pady=10, padx=10, ipadx=20)