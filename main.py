'''
Steven Kalis
11/30/2025
IS350
Semester Project - Main.py
Description: 
'''
import tkinter as tk
from tkinter import ttk
import room
import windows



def mainMenu():
    app = windows.initialize()
    app.mainloop()

    
#Returns the list of rooms from the rooms class
def generateRooms():
    rooms = []
    count = 0
    
    while count < 42:
        if count < 21: 
            rooms.append(room.Room()) #Build single rooms into array
            
        else:
            rooms.append(room.DeluxeRoom()) #Builds deluxe rooms after single rooms
        count += 1
    
    return rooms



#Takes the rooms list and compares how much we have to how much we should have
def getInventoryStatus(roomList, component = " "):
    invTP = 0
    invBS = 0
    invShmp = 0
    invBdW = 0
    invSoap = 0
    invRb = 0
    invRefresh = 0
    
    
    for count in range (len(roomList)):
        
        #Count how many we have
        invTP += roomList[count].getToiletPaper()
        invBS += roomList[count].getBedSheets()
        invShmp += roomList[count].getShampoo()
        invBdW += roomList[count].getBodyWash()
        invSoap += roomList[count].getSoap()
        if(count > 20):
            invRb += roomList[count].getRobe()
            
            invRefresh += roomList[count].getRefreshments()
        count+=1
    if component == " ":
        return f"Total Rooms in Inn: 42\n-----------------------\nAvailable/Required \nComponent Quantity:\nToilet Paper:\t\t{invTP}/42\nBed Sheets:\t\t{invBS}/168\nShampoo:\t\t{invShmp}/42\nBody Wash:\t\t{invBdW}/42\nSoap:\t\t{invSoap}/42\nRobes:\t\t{invRb}/42\nRefreshments:\t\t{invRefresh}/144"
    elif component == "TP":
        return invTP
    elif component == "BS":
        return invBS
    elif component == "Shmp":
        return invShmp
    elif component == "BdW":
        return invBdW
    elif component == "Soap":
        return invSoap
    elif component == "Rb":
        return invRb
    elif component == "Refresh":
        return invRefresh


if __name__ == "__main__":
    mainMenu()

    