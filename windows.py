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
from tkinter import filedialog
rooms = []
updatedInventory = []
class initialize(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args, **kwargs)
        self.title("Arlington Inn and Suites Relenishment system")
        self.geometry("1000x350")
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

        #Label for InventoryStatus
        lblInvStatus = ttk.Label(self, text="Review the current state of the Inn ventory:")
        lblInvStatus.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
        
        #Label for product tree
        lblProdTree = ttk.Label(self, text="Product Structure Tree")
        lblProdTree.grid(column=2, row=1, sticky=tk.EW, padx=5, pady=5)

        '''
            Had issues with this part. I had to build the list of rooms here
            then reference the global variable in each class
        '''
        txtInventoryStatus = tk.Text(self, wrap='word', height = 11, width=30)
        txtInventoryStatus.grid(column=0, row=3, padx=5, pady=5)
        txtInventoryStatus.insert(tk.END,main.getInventoryStatus(rooms))
        txtInventoryStatus.config(state=tk.DISABLED)

        txtProductStructure = tk.Text(self, wrap='word', height = 11, width=90)
        txtProductStructure.grid(column=2, row=3, padx=5, pady=5)
        txtProductStructure.insert(tk.END,"\t\t\t\t\t  Deluxe Room:\n" + "\t\t\t\t\t\t|\n" + "\t\t\t---------------------------------------------------------\n" + 
                                     "\t\t\t|\t\t\t\t\t\t\t|\n"  +  "\t\t\tRoom (1)\t\t\t\t\t\t\t|\n" + "--------------------------------------------------------------------  \t\t\t\t\t\t\t\t\t\t|\n" + 
                                     "\t|\t|\t\t|\t|\t\t|\t   |\t\t|\n" + 
                                   "Toilet Paper(1) BedSheets(4) Shampoo(1) Conditioner(1) BodyWash(1) Soap(1)\t\t\t\t\t\t|\n" +
                                 "\t\t\t\t\t\t\t\t-------------------------\n" + "\t\t\t\t\t\t\t\t|\t\t\t|\n" + "\t\t\t\t\t\t\t\tRobe(2)    Refreshments(6)")
        txtProductStructure.config(state=tk.DISABLED)
        
        
        #Button to start process 
        btnBegin = ttk.Button(self, text="Order Items",
        command= lambda : controller.show_frame(orderItems))
        btnBegin.grid(column=2, row=4, sticky=tk.EW, padx=5, pady=5)


class orderItems(tk.Frame):
    
    
    def changeAmount(self, multiplier, amount):
        amount.config(resolution=multiplier.get())


    def purchaseOrder(self,tp, bs, shmp, bdw, soap, rb, refresh, lbl):
        lbl.config(text="Ordered!")
        count = 0
        while count < 42:
            if count < 21: 
                updatedInventory.append(tp) 
                updatedInventory.append(bs) 
                updatedInventory.append(shmp) 
                updatedInventory.append(bdw) 
                updatedInventory.append(soap) 
                
            else:
                updatedInventory.append(rb) 
                updatedInventory.append(refresh) 
            count += 1

        

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global rooms

        global tpMultiplier, bsMultiplier, soapMultiplier, refreshMultiplier

        
        #--------Grid Labels---------------
        lblMaterials = ttk.Label(self, text="Raw Materials:")
        lblMaterials.grid(column=0, row=0, sticky=tk.EW)
        
        lblLotSize = ttk.Label(self, text="\tLot Size:")
        lblLotSize.grid(column=1, row=0, sticky=tk.EW)

        lblCompQnty = ttk.Label(self, text="Component Quantity:")
        lblCompQnty.grid(column=3, row=0, sticky=tk.EW)

        lblAvailable = ttk.Label(self, text="Available:")
        lblAvailable.grid(column=4, row=0, sticky=tk.EW, padx=20)
        
        lblNetRequirement = ttk.Label(self, text="Net Requirement:")
        lblNetRequirement.grid(column=5, row=0, sticky=tk.EW, padx=20)

        lblPlndOrd = ttk.Label(self, text="Planned Order:")
        lblPlndOrd.grid(column=6, row=0, sticky=tk.EW, padx=20)

        #--------TOILET PAPER---------------
        #Some items will have fixed amounts to increase by
        lblToiletPaper = ttk.Label(self, text="Toilet Paper")
        lblToiletPaper.grid(column=0, row=1, sticky=tk.EW)
        
        #Radio Buttons to select the kind to purchase
        tpMultiplier = tk.StringVar(value=8)
        rdoTPEight = ttk.Radiobutton(self, text="8F", value=8, variable=tpMultiplier)
        rdoTPEight.grid(column=1, row=1, sticky=tk.EW)
        rdoTPTwelve = ttk.Radiobutton(self, text="12F", value=12, variable=tpMultiplier) 
        rdoTPTwelve.grid(column=2, row=1, sticky=tk.EW)
        #slider to show how much to purchase
        tpAmount = tk.DoubleVar()
        tpSlider = tk.Scale(self,from_=0, to=100,orient="horizontal",variable=tpAmount)
        tpSlider.grid(column=3,row=1, sticky=tk.EW)
        #Grabs the amount of inventory from all rooms
        lbltpAvailable = ttk.Label(self, text=main.getInventoryStatus(rooms,component="TP"))
        lbltpAvailable.grid(column=4, row=1, sticky=tk.EW, padx=20)
        #displays how much are needed for a day
        lbltpNetRequirement = ttk.Label(self, text=f"{42 - int(main.getInventoryStatus(rooms,component="TP"))}")
        lbltpNetRequirement.grid(column=5, row=1, sticky=tk.EW, padx=20)

        #displays the adjusted amount from the slider to the planned order
        lbltpPlndOrd = ttk.Label(self, textvariable=tpAmount)
        lbltpPlndOrd.grid(column=6, row=1, sticky=tk.EW, padx=20)
        #controls the ability to change the multiplier of the amount slider
        rdoTPEight.config(command=self.changeAmount(tpMultiplier,tpSlider))
        rdoTPTwelve.config(command=self.changeAmount(tpMultiplier,tpSlider))

        #--------Bed Sheets---------------
        #Some items will have fixed amounts to increase by
        lblBedSheets = ttk.Label(self, text="Bed Sheets")
        lblBedSheets.grid(column=0, row=2, sticky=tk.EW)
        #Radio Buttons to select the kind to purchase
        bsMultiplier = tk.StringVar(value=2)
        rdoBSTwo = ttk.Radiobutton(self, text="2F", value=2, variable=bsMultiplier)
        rdoBSTwo.grid(column=1, row=2, sticky=tk.EW)
        rdoBSFour = ttk.Radiobutton(self, text="4F", value=4, variable=bsMultiplier) 
        rdoBSFour.grid(column=2, row=2, sticky=tk.EW)
        #slider to show how much to purchase
        bsAmount = tk.DoubleVar()
        bsSlider = tk.Scale(self,from_=0, to=100,orient="horizontal",variable=bsAmount)
        bsSlider.grid(column=3,row=2, sticky=tk.EW)
        
        lblbsAvailable = ttk.Label(self, text=main.getInventoryStatus(rooms,component="BS"))
        lblbsAvailable.grid(column=4, row=2, sticky=tk.EW, padx=20)

        lblbsNetRequirement = ttk.Label(self, text=f"{168 - int(main.getInventoryStatus(rooms,component="BS"))}")
        lblbsNetRequirement.grid(column=5, row=2, sticky=tk.EW, padx=20)
        
        #displays the adjusted amount from the slider to the planned order
        lblbsPlndOrd = ttk.Label(self, textvariable=bsAmount)
        lblbsPlndOrd.grid(column=6, row=2, sticky=tk.EW, padx=20)
        #controls the ability to change the multiplier of the amount slider
        rdoBSTwo.config(command=self.changeAmount(bsMultiplier,bsSlider))
        rdoBSFour.config(command=self.changeAmount(bsMultiplier,bsSlider))

        #--------Shampoo---------------
        #Some items will have fixed amounts to increase by
        lblShampoo = ttk.Label(self, text="Shampoo")
        lblShampoo.grid(column=0, row=3, sticky=tk.EW)
        
        lblshmpLFL = ttk.Label(self, text="\t      LFL")
        lblshmpLFL.grid(column=1, row=3, sticky=tk.EW)
        #Maybe find an alternative to selecting an amount
        shmpAmount = tk.DoubleVar()
        shmpSlider = tk.Scale(self,from_=0, to=100,orient="horizontal",variable=shmpAmount)
        shmpSlider.grid(column=3,row=3, sticky=tk.EW)
        
        lblshmpAvailable = ttk.Label(self, text=main.getInventoryStatus(rooms,component="Shmp"))
        lblshmpAvailable.grid(column=4, row=3, sticky=tk.EW, padx=20)

        lblshmpNetRequirement = ttk.Label(self, text=f"{42 - int(main.getInventoryStatus(rooms,component="Shmp"))}")
        lblshmpNetRequirement.grid(column=5, row=3, sticky=tk.EW, padx=20)

        #displays the adjusted amount from the slider to the planned order
        lbshmpPlndOrd = ttk.Label(self, textvariable=shmpAmount)
        lbshmpPlndOrd.grid(column=6, row=3, sticky=tk.EW, padx=20)
        

        #--------Body Wash---------------
        #Some items will have fixed amounts to increase by
        lblBodyWash = ttk.Label(self, text="Body Wash")
        lblBodyWash.grid(column=0, row=4, sticky=tk.EW)
        lblbdWLFL = ttk.Label(self, text="\t      LFL")
        lblbdWLFL.grid(column=1, row=4, sticky=tk.EW)
        bdWAmount = tk.DoubleVar()
        bdWSlider = tk.Scale(self,from_=0, to=100,orient="horizontal",variable=bdWAmount)
        bdWSlider.grid(column=3,row=4, sticky=tk.EW)
        
        lblbdWAvailable = ttk.Label(self, text=main.getInventoryStatus(rooms,component="BdW"))
        lblbdWAvailable.grid(column=4, row=4, sticky=tk.EW, padx=20)

        lblbdWNetRequirement = ttk.Label(self, text=f"{42 - int(main.getInventoryStatus(rooms,component="BdW"))}")
        lblbdWNetRequirement.grid(column=5, row=4, sticky=tk.EW, padx=20)

        #displays the adjusted amount from the slider to the planned order
        lbbdWPlndOrd = ttk.Label(self, textvariable=bdWAmount)
        lbbdWPlndOrd.grid(column=6, row=4, sticky=tk.EW, padx=20)

        #--------Soap---------------
        #Some items will have fixed amounts to increase by
        lblSoap = ttk.Label(self, text="Soap")
        lblSoap.grid(column=0, row=5, sticky=tk.EW)
        #Radio Buttons to select the kind to purchase
        soapMultiplier = tk.StringVar(value=5)
        rdoSoapFive = ttk.Radiobutton(self, text="5F", value=5, variable=soapMultiplier)
        rdoSoapFive.grid(column=1, row=5, sticky=tk.EW)
        rdoSoapTen = ttk.Radiobutton(self, text="10F", value=10, variable=soapMultiplier) 
        rdoSoapTen.grid(column=2, row=5, sticky=tk.EW)
        #slider to show how much to purchase
        soapAmount = tk.DoubleVar()
        soapSlider = tk.Scale(self,from_=0, to=100,orient="horizontal",variable=soapAmount)
        soapSlider.grid(column=3,row=5, sticky=tk.EW)
        
        lblsoapAvailable = ttk.Label(self, text=main.getInventoryStatus(rooms,component="Soap"))
        lblsoapAvailable.grid(column=4, row=5, sticky=tk.EW, padx=20)

        lblsoapNetRequirement = ttk.Label(self, text=f"{42 - int(main.getInventoryStatus(rooms,component="Soap"))}")
        lblsoapNetRequirement.grid(column=5, row=5, sticky=tk.EW, padx=20)

        #displays the adjusted amount from the slider to the planned order
        lblsoapPlndOrd = ttk.Label(self, textvariable=soapAmount)
        lblsoapPlndOrd.grid(column=6, row=5, sticky=tk.EW, padx=20)
        #controls the ability to change the multiplier of the amount slider
        rdoSoapFive.config(command=self.changeAmount(soapMultiplier,soapSlider))
        rdoSoapTen.config(command=self.changeAmount(soapMultiplier,soapSlider))

        #--------Robes ---------------
        #Some items will have fixed amounts to increase by
        lblRobes = ttk.Label(self, text="Robes")
        lblRobes.grid(column=0, row=6, sticky=tk.EW)
        lblRobeLFL = ttk.Label(self, text="\t      LFL")
        lblRobeLFL.grid(column=1, row=6, sticky=tk.EW)
        rbAmount = tk.DoubleVar()
        rbSlider = tk.Scale(self,from_=0, to=100,orient="horizontal",variable=rbAmount)
        rbSlider.grid(column=3,row=6, sticky=tk.EW)
        
        lblrbAvailable = ttk.Label(self, text=main.getInventoryStatus(rooms, component="Rb"))
        lblrbAvailable.grid(column=4, row=6, sticky=tk.EW, padx=20)

        lblrbNetRequirement = ttk.Label(self, text=f"{42 - int(main.getInventoryStatus(rooms,component="Rb"))}")
        lblrbNetRequirement.grid(column=5, row=6, sticky=tk.EW, padx=20)

        #displays the adjusted amount from the slider to the planned order
        lbrobeWPlndOrd = ttk.Label(self, textvariable=rbAmount)
        lbrobeWPlndOrd.grid(column=6, row=6, sticky=tk.EW, padx=20)


        #--------Refreshments ---------------
        #Some items will have fixed amounts to increase by
        lblRefresh = ttk.Label(self, text="Refreshments")
        lblRefresh.grid(column=0, row=7, sticky=tk.EW)

        refreshMultiplier = tk.StringVar(value=6)
        rdoRefreshSix = ttk.Radiobutton(self, text="6F", value=6, variable=refreshMultiplier)
        rdoRefreshSix.grid(column=1, row=7, sticky=tk.EW)
        rdoRefreshTwentyFour = ttk.Radiobutton(self, text="24F", value=24, variable=refreshMultiplier) 
        rdoRefreshTwentyFour.grid(column=2, row=7, sticky=tk.EW)
        refreshAmount = tk.DoubleVar()
        refreshSlider = tk.Scale(self,from_=0, to=100,orient="horizontal",variable=refreshAmount)
        refreshSlider.grid(column=3,row=7, sticky=tk.EW)
        
        lblrefreshAvailable = ttk.Label(self, text=main.getInventoryStatus(rooms,component="Refresh"))
        lblrefreshAvailable.grid(column=4, row=7, sticky=tk.EW, padx=20)

        lblrefreshNetRequirement = ttk.Label(self, text=f"{144 - int(main.getInventoryStatus(rooms,component="Refresh"))}")
        lblrefreshNetRequirement.grid(column=5, row=7, sticky=tk.EW, padx=20)

        #displays the adjusted amount from the slider to the planned order
        lblrefreshPlndOrd = ttk.Label(self, textvariable=refreshAmount)
        lblrefreshPlndOrd.grid(column=6, row=7, sticky=tk.EW, padx=20)
        #controls the ability to change the multiplier of the amount slider
        rdoRefreshSix.config(command=self.changeAmount(refreshMultiplier,refreshSlider))
        rdoRefreshTwentyFour.config(command=self.changeAmount(refreshMultiplier,refreshSlider)) 



        btnBackToMenu = ttk.Button(self, text="Back",
        command= lambda : controller.show_frame(mainMenu))
        btnBackToMenu.grid(column=0, row=8, sticky=tk.EW, padx=5, pady=5)

        lblOrderStatus = ttk.Label(self)
        lblOrderStatus.grid(column=7, row=8, sticky=tk.EW, padx=20)

        btnPurchaseOrder = ttk.Button(self, text="Order",
        command= lambda : self.purchaseOrder(tpAmount,bsAmount.get,shmpAmount.get,bdWAmount.get,soapAmount.get,rbAmount.get,refreshAmount.get,lblOrderStatus))
        btnPurchaseOrder.grid(column=6, row=8, sticky=tk.EW, padx=5, pady=5)


        btnInvoice = ttk.Button(self, text="View Invoice",
        command= lambda : controller.show_frame(viewInvoice))
        btnInvoice.grid(column=8, row=8, sticky=tk.EW, padx=5, pady=5)

        

        
    
        


class viewInvoice(tk.Frame):
     
     def ButtonSaveEvent(self):
        files = [
            ("All Files", "*."),
            ("Text Document", "*.txt")
        ]
        file_path = filedialog.asksaveasfile(filetypes=files, defaultextension=files)

        if file_path:
                try:
                    with open(file_path,'w') as file:
                        file.write()
                except Exception as e:
                    print(f"Error creating file: {e}")
     
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Button to save planned order receipts
        btnBackToOrder = ttk.Button(self, text="Save",
        command= lambda : self.ButtonSaveEvent())
        btnBackToOrder.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)


        #Get back to the Order Items screen
        btnBackToOrder = ttk.Button(self, text="Back",
        command= lambda : controller.show_frame(orderItems))
        btnBackToOrder.grid(column=0, row=7, sticky=tk.EW, padx=5, pady=5)