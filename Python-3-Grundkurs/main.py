from tkinter import *
from bmi import Benutzer,Bmirechner

class Rahmen(Frame):
    def __init__(self,master=None,labeltext=''):
        Frame.__init__(self,master)
        self.pack()
        self.Label=Label(self,anchor=W,text=labeltext,width=30)
        self.Label.pack(side='left')
        self.text=StringVar()
        self.Entry=Entry(self,width=30,textvariable=self.text)
        self.Entry.pack(side='right')
        
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.nameFrame=Rahmen(master,'Name:')
        self.groesseFrame=Rahmen(master,'Körpergrösse:')
        self.gewichtFrame=Rahmen(master,'Gewicht:')
        self.buttonFrame=Frame(master)
        self.buttonFrame.pack()
        self.okButton=Button(self.buttonFrame,width=20,text='OK',command=self.action)
        self.okButton.pack(side='left')
        self.cancelButton=Button(self.buttonFrame,width=20,text='Abbrechen!',command=root.destroy)
        self.cancelButton.pack(side='right')
        self.listbox=Listbox(master)
        self.listbox.pack(fill=BOTH)
    def action(self):
        benutzer=Benutzer(
            self.nameFrame.text.get(),
            self.groesseFrame.text.get())
        bmirechner=Bmirechner()
        bmi=bmirechner.rechnen(benutzer.groesse,self.gewichtFrame.text.get())
        bmirechner.hinzufuegen(benutzer.name,bmi)
        self.listbox.delete(0,END)
        if benutzer.name in bmirechner.datenspeicher:
            bmis=bmirechner.datenspeicher[benutzer.name]
            for bmi in bmis:
                self.listbox.insert(
                    END,
                    benutzer.name+':'+
                    str(bmi)+':'+
                    bmirechner.auswerten(bmi))
        
root=Tk()
Application(master=root)
root.mainloop
