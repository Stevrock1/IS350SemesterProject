'''
Steven Kalis
11/30/2025
IS350
Semester Project - Main Menu GUI
Description: The home menu the user interfaces with
'''
import tkinter as tk
from tkinter import ttk
import room

rooms = []

def mainMenu():
    root = tk.Tk()
    root.title("Arlington Inn and Suites Replenishment System")
    root.geometry("500x300")

    #grid setup
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

    #Header
    lblHeader = tk.Label(root, text="Welcome to the replenishment system")
    lblHeader.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

    #Label for selection
    lblSelection = tk.Label(root, text="Please select which item to replenish:")
    lblSelection.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

    #List of replenishment items
   

    #Creates 42 room classes into an array. Assume there are 21 single and 21 double rooms
    # count = 0
    # while count < 41:
    #     if count < 22: 
    #         rooms.append(room.Room()) #Build single rooms into array
    #     else:
    #         rooms.append(room.DeluxeRoom()) #Builds deluxe rooms after single rooms
    # count += 1
    #TODO: Display Inventory List

    selectedItem = tk.StringVar()
    lstInventory = ttk.Combobox(root, textvariable=selectedItem)
    lstInventory["values"] = ("Toilet Paper", "Bed Sheets", "Shampoo", "Conditioner", "Body Wash", "Soap", "Bath Robes", "Refreshments")
    lstInventory["state"] = "readonly"
    lstInventory.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

    #Button to start process for the selected item
    btnBegin = ttk.Button(root, text="Replenish")
    btnBegin.grid(column=2, row=2, sticky=tk.EW, padx=5, pady=5)

    root.mainloop()

#def generateRooms()

if __name__ == "__main__":
    mainMenu()