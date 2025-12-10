'''
Steven Kalis
11/30/2025
IS350
Semester Project - Room Class
Description: Builds up the items within a room that the user can identify are low in stock or not

Types of rooms:
    -Single Bed
    -Double Bed
        -Make this more of a premium option, with more features than the single bed room.
'''
import random

class Room:
    def __init__(self):
        self.toiletPaper = random.randint(0, 1)
        self.bedSheets = random.randint(0,4) # 2 pillow cases, bed sheet, and blanket
        self.shampoo = random.randint(0,1)
        self.conditioner = random.randint(0,1)
        self.bodyWash = random.randint(0,1)
        self.soap = random.randint(0,1)

    def getToiletPaper(self):
        return self.toiletPaper
    def getBedSheets(self):
        return self.bedSheets
    def getShampoo(self):
        return self.shampoo
    def getConditioner(self):
        return self.conditioner
    def getBodyWash(self):
        return self.bodyWash
    def getSoap(self):
        return self.soap

class DeluxeRoom(Room):
    def __init__(self):
        super().__init__()
        self.bedSheets = random.randint(0,8) #Two Beds, same stuff
        self.robe = random.randint(0,2) #Deluxe room has two robes that can be used
        
        self.refreshments = random.randint(0,6) #Refrigerator includes up to 6 refreshments
    
    def getRobe(self):
        return self.robe
    def getRefreshments(self):
        return self.refreshments