'''
Steven Kalis
12/7/2025
IS350
Semester Project - Windows Class
Description: This application will have multiple menus for input and output
throughout the replenishment system. This class will allow the main.py to swap
between pages when its time to move on to the next steps

Reference for multi-page setup: https://www.geeksforgeeks.org/python/tkinter-application-to-switch-between-different-page-frames/

'''
import main
import tkinter as tk
from tkinter import ttk
rooms = []
class initialize(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args, **kwargs)
        self.title("Arlington Inn and Suites Relenishment system")
        self.geometry("500x300")
        container = tk.Frame(self)
        #Pack the container
        container.pack(side = "top", fill="both", expand=True)
        #The frame within the container will be configured with grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        global rooms 
        rooms = main.generateRooms()
        
        self.frames = {}
        #add pages into frame tuple
        for F in (mainMenu, orderItems, viewInvoice):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
           

        self.show_frame(mainMenu)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class mainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global rooms
        #Header
        lblHeader = ttk.Label(self, text="Welcome to the replenishment system")
        lblHeader.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

        #Label for selection
        lblSelection = ttk.Label(self, text="Please select which item to replenish:")
        lblSelection.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

        #List of replenishment items
        #TODO: Change from combo buttons to radio/checklists
        selectedItem = tk.StringVar()
        lstInventory = ttk.Combobox(self, textvariable=selectedItem)
        lstInventory["values"] = ("Toilet Paper", "Bed Sheets", "Shampoo", "Conditioner", "Body Wash", "Soap", "Bath Robes", "Refreshments")
        lstInventory["state"] = "readonly"
        lstInventory.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        '''
            Had issues with this part. I had to build the list of rooms here
            then reference the global variable in each class
        '''
        txtInventoryStatus = tk.Text(self, wrap='word', height = 10, width=40)
        txtInventoryStatus.grid(column=0, row=3, padx=5, pady=5)
        txtInventoryStatus.insert(tk.END,main.getInventoryStatus(rooms))
        txtInventoryStatus.config(state=tk.DISABLED)
        #Button to start process for the selected item
        btnBegin = ttk.Button(self, text="Order Items")
        btnBegin.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

#TODO:Build up other pages 

class orderItems(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class viewInvoice(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)