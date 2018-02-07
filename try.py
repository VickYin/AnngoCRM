# _*_ coding: utf-8 _*_

from tkinter import *

class InputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.outString = Variable()
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Please Input:',)
        self.helloLabel.pack(side=LEFT)
        self.inputEdit = Entry(self)
        self.inputEdit.pack(side=RIGHT)
        self.OKButton = Button(self, text="OK", command=self.getString)
        self.OKButton.pack()

    def getString(self):
        self.outString = self.inputEdit.get()
        self.quit()

root = Tk()
root.geometry("400x300")
root.title('I do')
root.resizable(width=False, height=False)

instring = InputFrame(root)
instring.mainloop()
print(instring.outString)