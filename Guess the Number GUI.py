import os
import wx
import time
import random
#def cls():
#    print('\n' * 10)
##
#cls()
## Guess My Number
##
## The computer picks a random number between 1 and 100
## The player tries to guess it and the computer lets
## the player know if the guess is too high, too low
## or right on the money
#
#
#print("\tWelcome to Guess The Number!")
#print("\nI'm thinking of a number between 1 and 100.")
#print("You will have five tries to guess correctly.")
#print("Try not to screw this up...\n")
#
## set the initial values
#the_number = random.randint(1, 100)
#attempt = int(input("Take a guess: "))
#tries = 1
#
## guessing loop
#while attempt != the_number:
#    if attempt > the_number:
#        print("Are you serious...LOWER!")
#    else:
#        print("Haha you might wanna try higher...")
#
#    attempt = int(input("Take another guess: "))
#    tries += 1
#    if tries == 5:
#        print ("That was awful!")
#        print ("The correct number was", the_number)
#        break
#    if attempt == the_number:
#        print("You didn't fail me this time! The number was", the_number)
#        print("It only took you", tries, "tries...pathetic.\n")


#This Code Entered and Provided By Jacob C. based on Python101 Textbook

#
#class DemoPanel(wx.Panel):    
#
#    def __init__(self, parent):
#
#        wx.Panel.__init__(self,parent)
#
#        labels = ["Guess of a number through 1 and 100","label2","label 3"]
#
#        mainSizer = wx.BoxSizer(wx.VERTICAL)
#
#        lbl = wx.StaticText(self,label = "Number Guessing Game ")
#        #This next line controls the appearance of the Please enter your...
#        lbl.SetFont(wx.Font(24,wx.SWISS,wx.NORMAL,wx.BOLD))
#        #first number is row of the input box, second number controls top margin
#        mainSizer.Add(lbl,5,wx.ALL,20)
#
#        for lbl in labels:
#
#            sizer = self.buildControls(lbl)
#
#            mainSizer.Add(sizer,1,wx.EXPAND)
#
#        self.SetSizer(mainSizer)
#
#        mainSizer.Layout()
#
#    def buildControls(self,label):
#
#        sizer = wx.BoxSizer(wx.HORIZONTAL)
#        #size of input box
#        size = (400,400)
#
#        font = wx.Font(12,wx.SWISS,wx.NORMAL,wx.BOLD)
#
#        lbl = wx.StaticText(self,label = label, size = size)
#
#        lbl.SetFont(font)
#
#        sizer.Add(lbl,0,wx.ALL|wx.CENTER,5)
#
#        if label != "Notes":
#
#            txt = wx.TextCtrl(self, name=label)
#
#        else:
#
#            txt = wx.TextCtrl(self, style=wx.TE_MULTILINE, name=label)
#
#        sizer.Add(txt, 1, wx.ALL, 5)
#
#        return sizer
#        print ("sizer is "+sizer)
#class DemoFrame(wx.Frame):
#
#    def __init__(self):
#        #also controls size of overall window
#        wx.Frame.__init__(self, None, wx.ID_ANY, "Py2Exe Tutorial",size=(600,400))
#
#        panel = DemoPanel(self)
#
#        self.Show()
#
#if __name__ == "__main__":
#
#    app = wx.App(False)
#
#    frame = DemoFrame()
#
#    app.MainLoop()



def ask(parent=None, message='', default_value=''):
    dlg = wx.TextEntryDialog(parent, message,)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result

# Initialize wx App
app = wx.App()
app.MainLoop()
the_number = random.randint(1, 100)
response = "First guess please" 
y=0
for guess in range(7):
    y+=1
    x = ask(message=response)
    if str(x) == str(the_number):
        response=str(x)+" is correct. It took you "+(str(y))+" guesses. Press enter or OK to end game. "
    elif int(x) > the_number:
        response=str(x)+" Guess lower. "
    elif int(x) <the_number:
        response=str(x)+" You better try higher. "
    else:
        response=str(x)+" is wrong "
    if str(x) == str(the_number):
        x = ask(message=response)
        time.sleep(10) 
        break
