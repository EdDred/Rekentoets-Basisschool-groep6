from tkinter import * #from tkinter import
import os
import time # time for countdown timer

# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from rekentoets_backend import Rekentoets

'''
This Module build the display of rekentoets with tkinter
It use the Class Rekentoets from the module backend


'''

class frontend():
    def __init__(self,*args,**kwargs):
        #set variables

        self.var=StringVar()
        self.v1getal=IntVar()
        self.counter=IntVar()
        self.uitkomst=IntVar()
        self.result=IntVar()
        self.tijdverdiend=IntVar()
        self.today_score=0.0
        self.counter=0
        self.i=IntVar()
        self.time_str = StringVar()
        sf ="00:00" # set default timer value to 00:00

        window.title ("Rekentoetsen Basisschool")
        #window.geometry("1050x300")
        #window.configure(background='black')
        window.resizable(width=True, height=True)
        # Create Frames
        window.grid_rowconfigure(1, weight=1)
        window.grid_columnconfigure(0, weight=1)
        self.frametop = Frame(width=1400, height=100, borderwidth=2,highlightbackground="green", highlightcolor="green", highlightthickness=1)
        self.framecenter = Frame(width=1200, height=380)
        self.framebottom = Frame(width=1200, height=100)

        #Layout of frames
        self.frametop.grid(row=0,sticky="ew")
        self.frametop.grid_rowconfigure(0, weight=1)
        self.frametop.grid_columnconfigure(0, weight=3)
        self.frametop.grid_columnconfigure(1, weight=1)
        self.framecenter.grid(row=1,sticky="nsew")
        self.framebottom.grid(row=2,sticky="ew")


        self.framecenter.grid_rowconfigure(0, weight=1)
        self.framecenter.grid_columnconfigure(1, weight=1)
        self.framebottom.grid_rowconfigure(0, weight=1)
        self.framebottom.grid_columnconfigure(0, weight=1)
        self.framesum = Frame(self.framecenter,  width=800, height=380)
        self.framescore = Frame(self.framecenter, width=400, height=380, padx=3, pady=3)


        self.framesum.grid(row=1, column=0, sticky="nw")
        self.framescore.grid(row=1,column=1, sticky="ne")


        # Title Frame
        self.comment = Label(self.frametop,text="Toetssommetjes voor de Basisschool", fg="green", font="Verdana 14 italic",anchor='nw')
        self.comment.grid(row=0,column=0)
        img1 = PhotoImage(file="rekenenisleuk.gif")
        logo = Label(self.frametop, image=img1,anchor='ne')
        logo.image = img1
        logo.grid(row=0,column=1)

        # Frame for calculations
        self.a= Label(self.framesum,text="Wat is het maximale getal dat je wilt gebruiken? ", takefocus=True, font="Verdana 10 italic")
        self.a.grid(row=0,column=0, sticky='e')
        self.v1getal = Entry(self.framesum, width=10,font="Verdana 10 bold italic",justify='center')
        self.v1getal.grid(row=0,column=1, sticky='w')
        self.w= Label(self.framesum, text="Welk soort som wil je testen? " ,pady=5, font="Verdana 10 italic", anchor=NW).grid(row=1, column=0, sticky='e')
        self.R1 = ttk.Radiobutton(self.framesum, text="Vermenigvuldigen", variable=self.var, value="v").grid(row=1,column=1, sticky='w')
        self.R2 = ttk.Radiobutton(self.framesum, text="Delen (hele getallen uitkomst)", variable=self.var, value="dh").grid(row=2,column=1, sticky='w')
#        self.R3 = Radiobutton(self.framesum, text="Breuken (gelijke deler)", variable=self.var, value="bgelijkedeler", anchor='w', font="Verdana 10").grid(row=3,column=1, sticky='w')
        self.Givecalc = ttk.Button(self.framesum,text="Geef een som", width=30, command=lambda: self.DisplayCalculation(self.v1getal.get(),self.var.get()))
        #DisplayCalculation(self,self.v1getal.get(),self.var.get())
        self.Givecalc.grid(row=6, column=1)
        vorige_v1getal=self.v1getal.get()
        vorige_getal=self.var.get()
        self.L0 = Label(self.framesum,text="De gevraagde som is:", font="Verdana 10 italic")
        self.L0.grid(row=8,column=0, sticky='e')
        self.SomShow = Entry(self.framesum,width=60 , font="Verdana 10",justify='center')
        self.SomShow.grid(row=8,column=1)
        self.SomShowDeler = Entry(self.framesum,width=60 , font="Verdana 10",justify='center')
        self.SomShowDeler.grid(row=9,column=1)
        self.L1 = Label(self.framesum,text="Antwoord:", font="Verdana 10 italic")
        self.L1.grid(row=10,column=0, sticky='e')
        self.SomResult = Entry(self.framesum,)
        self.SomResult.grid(row=10,column=1,sticky='w')
        self.CheckResult = ttk.Button(self.framesum,text="Controleer Antwoord", width=20,command=lambda: self.CheckResults(self.SomResult.get(),self.uitkomst,self.counter))
        self.CheckResult.grid(row=12, column=1)
        self.SomError = Entry(self.framesum, width=62, border=0, font="Verdana 10", justify='center', bg='#f9f9f9self.')
        self.SomError.grid(row=13, column=0, columnspan=2, sticky='e')

        self.Quitbutton = ttk.Button(self.framesum,text="Stop en Mail de score", width=20, command=lambda: self.quitactions())
        self.Quitbutton.grid(row=14, column=1)
        self.Timerbutton = ttk.Button(self.framescore,text="Start de Timer", width=15, command=lambda: self.count_down(self.tijdverdiend))


        # Fill Scoreframe
        self.LZ =Label(self.framescore,text="Je score vandaag is:",  font="Verdana 10")
        self.LZ.grid(row=0,sticky='e')
        self.Score = Entry(self.framescore,  width=17, border=0, justify='right', font="Verdana 10")
        self.Score.grid(row=1,sticky='e')
        self.MI = Label(self.framescore,text="minuten",font="Verdana 10")
        self.MI.grid(row=2,sticky='e')
        self.DIV0 = Label(self.framescore,text="")
        self.DIV1 = Label(self.framescore,text="")
        self.DIV2 = Label(self.framescore,text="")
        self.DIV3 = Label(self.framescore,text="")
        self.DIV0.grid(row=7,sticky='SE')
        self.DIV2.grid(row=9,sticky='SE')
        self.DIV1.grid(row=8,sticky='SE')
        self.DIV3.grid(row=10,sticky='SE')
        self.Timerbutton.grid(row=7)
        self.LS1= Label(self.framescore,text="Getalgrootte <11: levert = 0.5 minuut")
        self.LS2= Label(self.framescore,text="Getalgrootte <101: levert = 1 minuut")
        self.LS3= Label(self.framescore,text="Getalgrootte >101: levert = 10 minuten")
        self.LS1.grid(row=20,sticky='SW')
        self.LS2.grid(row=21,sticky='SW')
        self.LS3.grid(row=22,sticky='SW')

        label_font = ('helvetica', 40)

        #show the countdown timer
        self.timer = Label(self.framebottom, textvariable=self.time_str, font=label_font, fg='black', relief='raised', bd=3, anchor='center')
        self.timer.grid(sticky='nsew')
        #set countdown to 00:00
        self.time_str.set(sf)
        window.update()

    def toggle_checkresultbtn(self,statusbutton):
    #   Toggle the check result button
        self.CheckResult = ttk.Button(self.framesum,text="Controleer Antwoord",state=statusbutton, width=20,command=lambda: self.CheckResults(self.SomResult.get(),self.uitkomst,self.counter))
        self.CheckResult.grid(row=12, column=1)

    def toggle_givenewcalc(self,statuscalc):
        # Toggle the give a new calculation button
        self.Givecalc = ttk.Button(self.framesum,text="Geef een som", width=30, state=statuscalc, command=lambda: self.DisplayCalculation(self.v1getal.get(),self.var.get())).grid(row=6, column=1)

    def DisplayCalculation(self,Getalgrootte,somtype):
        som,self.uitkomst = b.berekening(Getalgrootte,somtype)
        self.SomError.delete(0, "end")
        self.SomShow.delete(0, "end")
        self.SomShow.insert(0, som)
        self.toggle_givenewcalc(DISABLED)
        self.toggle_checkresultbtn(NORMAL)

    def CheckResults(self,somresult,uitkomst,counter):
        teller,antwoord,resultaat = b.Checkresult(somresult,uitkomst,counter)
        print(resultaat)
        print(type(resultaat))
        print("teller in frontend = " + str(teller))
        if resultaat:
            print("Uitkomst is correct")
            self.SomError.delete(0, "end")
            self.SomError.insert(0, "Geweldig , dat is GOED! Vraag een nieuwe som.")
            self.tijd,self.tijdverdiend= b.determine_score(self.v1getal.get())
            self.counter = 0
            self.toggle_checkresultbtn(DISABLED)
            self.toggle_givenewcalc(NORMAL)
            self.Score.delete(0,"end")
            self.Score.insert(0,str(self.tijdverdiend/60))
            self.time_str.set(self.tijd)
            window.update()
        elif (teller>2):
            self.SomError.insert(0, "Dat is helaas niet goed, je mag niet meer proberen, vraag een andere som")
            print("Uitkomst is niet correct, je mag niet meer proberen")
            self.toggle_checkresultbtn(DISABLED)
            self.toggle_givenewcalc(NORMAL)
            self.counter = 0

        else:
            nog = 3-teller
            self.counter = teller
            self.SomError.delete(0, "end")
            self.SomError.insert(0, "Dat is helaas niet goed, je mag nog "+ str(nog) + " keer proberen" )
            print("Uitkomst is niet correct, probeer opnieuw, self.counter=" +str(self.counter))
            self.toggle_checkresultbtn(NORMAL)
            self.toggle_givenewcalc(DISABLED)

    def count_down(self,t_s):
        today_score = int(t_s)
#        tijdverdiend = int(today_score * 60)
        messagebox.showinfo("Information","Er wordt een mailtje met je verdiende tijd van %s minuten, naar je vader gestuurd en de timer met je verdiende tijd gaat lopen" %(self.today_score))
        b.MailResults(self.today_score,0)
        b.reset_score()
        self.today_score = 0
        self.tijd = 0
        self.tijdverdiend = 0
        self.Score.delete(0,"end")
        self.Score.insert(0,"Tijd weer op 0")

        # start with 2 minutes --> 120 seconds
        for t in range(today_score, -1, -1):
    #    for t in range(tijdverdiend, -1, -1):
            # format as 2 digit integers, fills with zero to the left
            # divmod() gives minutes, seconds
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            #print(sf)  # test
            self.time_str.set(sf)
            window.update()
            # delay one second
            if t == 0:
                b.play_buzzer()
            time.sleep(1)
        messagebox.showinfo("Information","Je tijd is helaas op")

    def quitactions(self):
        print("start quitactions")
        b.MailResults(self.tijdverdiend,1)
        messagebox.showinfo("Information","Er wordt een mailtje met je verdiende tijd van %s minuten, naar je vader gestuurd. " %(self.today_score))
        self.frametop.quit()



b = Rekentoets(frontend)

if __name__ == "__main__":
    window = tk.Tk()
    window.iconbitmap('rekenenisleuk.ico')
    frontend()
    window.mainloop()
