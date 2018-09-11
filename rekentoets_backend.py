from tkinter import * #from tkinter import
import random
import os
from email.mime.text import MIMEText #import email
import smtplib
import time # time for countdown timer
from pygame import mixer #lib to play sound when time is up
# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


'''
This module contains a Rekentoets class.
It provides a calculation for dutch group 6 (at the moment)
The result is time that is earned (in our case that time can be used for playing games)
Checks the result of the calculations
Determines the score based on how big the used numbers are
Writes and returns the Score
mails the score to parent
creates a timer

To do:
    Flexibel scoring based parent Entry
    add group7 calculations
    add flexible mailing adress
    expand with 'breuken'
    expand with redactiesommen'

'''


class Rekentoets():

    '''
    The Class rekentoets containing everything
    '''

    def __init__(self,parent, *args, **kwargs):

        '''
        Args:
            self:
            parent:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        '''

        self.today_score=0.0
        self.counter=1


    def rewards(self,Getal):
        '''
        Method rewards , based on the maximum number that is given in the frontend the score per calcultion is defined

        Args:
            Getal: containg the getalgrootte


        Returns:
            reward an real number containing the reward per correct calculation

        '''
        #This function determines the reward won per correct answer
        Getalgrootte = int(Getal)
        if Getalgrootte <11:
            reward = 0.5
            # 0,5 minuten voor sommen onder de 10
        elif (11 <= Getalgrootte < 101):
            reward = 1
            # 1 minuut bij sommen tussen 12 en 100
        else:
            reward = 10
        return(reward)

    def get_previous_score(self):
        '''
        Method previous score opens the score.txt file and reads the previous score value
        if the file score.txt is not available it will be created with one value 0
        Args:
            None


        Returns:
            lastscore value

        '''
        #Get the previous score from the score file
        if os.path.isfile('score.txt'):
            myfile = open("score.txt")
            numberlines = myfile.readlines()
            lastscore = numberlines[-1]
        #    print (lastscore)
            myfile.close()
            return(lastscore)
        else:
            print("geen file aanwezig voor score")
            file = open("score.txt", "w")
            file.write('0')
            file.close()
            lastscore=0
            return(lastscore)

    def write_score(self,new_score):
        # Append the new score in the score file
        if os.path.isfile('score.txt'):
            myfile = open("score.txt", "a")
            myfile.write("\n"+new_score)
            myfile.close()
            return
        else:
            print("geen file aanwezig voor score")
            file = open("score.txt", "w")
            file.write('0')
            file.close()

    def reset_score(self):
        '''
        Reset the score and writes a zero to the score file
        Args:
            none

        Returns:
            none
        '''
        self.today_score=0
        self.write_score(str(self.today_score))

    def determine_score(self,Getalgrootte):
        '''
        Determinse the score
        Args:
            Getalgrootte value of the maximum height of the numbers used in the calcution
            Writes the score to the file
            updates the self.today_score variable
            Converts to a parameter to be used as a timer
        Returns:
            sf: value in minutes and secondes 00:00
            tijdverdiend: time earned in minutes (0,0)
        '''
        print("score berekenen")
        reward = float(self.rewards(Getalgrootte))
        print("Je beloning per som is %s minuten" %(reward))
        prev = float(self.get_previous_score())
        new_score = reward + prev
        print(prev)
        print("New score = " + str(new_score))

        self.write_score(str(new_score))
#        self.Score.delete(0,"end")
        #the score today:
        today_score_prev = self.today_score
        self.today_score= float(reward) + float(today_score_prev)
        print("de score van vandaag is " + str(self.today_score))
#        self.Score.insert(0,str(self.today_score))
        tijdverdiend = int(self.today_score * 60)
        sf = "{:02d}:{:02d}".format(*divmod(tijdverdiend, 60))
        #print(sf)  # test
    #    self.time_str.set(sf)
    #    window.update()
        return(sf,tijdverdiend)



    def berekening(self,Getalgrootte,Typesom):
        '''
        defines the calcultion based on the maximum Number and Type of Calculation
        Args:
            Getalgrootte (int): Maximum number
            Typesom (string): The type of the calculation
                    v : Multiply
                    dh : Divide with an outcome of whole numbers

        Returns:
            som: the description of the som that can be displayed
            self.uitkomst : the result of the calculation to be used in result check
            rtype som: StringVar
            rtype self.uitkomst: number
        '''


        print(str(Getalgrootte) + str(Typesom))
        if Typesom == 'v':
            getal = int(random.random() * int(Getalgrootte))
            getal1 = int(random.random()*10)
            self.uitkomst = int(getal1 *getal)
            som = ("Wat is de uitkomst van: " + str(getal) + " x " + str(getal1))
            print(som)
            return(som,self.uitkomst)

        elif Typesom == 'dh':
            print("delen")
            number_dec = 1
            self.uitkomst = 1
            while (number_dec != "0" or deler == 0 or Noemer ==0):
                Noemer = int(random.random()*int(Getalgrootte))
                deler = int(random.random()*10)
        #        print("Noemer is %s" %(Noemer))
        #        print("Deler is %s" %(deler))
                if deler != 0: # deze berekening alleen uitvoeren als er geen division by zero kan ontstaan
                    self.uitkomst = Noemer / deler
                    number_dec = str(self.uitkomst).split(".")[1]
            som = ("Wat is de uitkomst van: " + str(Noemer) + " : " + str(deler))
            print(som)
            return(som,self.uitkomst)

# Breuken met een gelijke deler voor niveau start groep 7
        elif Typesom == 'bgelijkedeler':
            print("breuken")
            Deler1 =  int(random.random()*int(Getalgrootte))
            Noemer1 = int(random.random()*int(int(Getalgrootte)-1))
            print("De breuk 1 is %s / %s" %(Noemer1,Deler1))
            Deler2 =  int(random.random()*int(Getalgrootte))
            Noemer2 = int(random.random()*int(int(Getalgrootte)-1))
            som = ("Wat is de uitkomst van: " + str(Noemer1) + " / " + str(Deler1) + " + " + str(Noemer2) + " / " + str(Deler1))
            print(som)
            self.uitkomst = (Noemer1/Deler1)+(Noemer2/Deler2)
            print(self.uitkomst)
            return(som,self.uitkomst)
        else:
            print("niks")
        return(self.uitkomst)


    def Checkresult(self,result,uitkomst,i):
        '''
        Checks the result given by the user with the correct result of the calculation

        Args:
            result (int): result given by the user to be checked
            uitkomst(int): correct result of the calculation
            i(int): count for number of times tried


        Returns:
            i(int): update of the counter
            result(int): Result given by user
            answercorrect(bool): Answer correct or not

        '''


    # Check if result is correct
        print("Dit is het ingevoerde antwoord: " + result)
        print("Dit is de verwachte uitkomst: " + str(uitkomst))
        print("teller backend (i) = "+ str(i))
        if int(result) == int(uitkomst):
            print("Geweldig , dat is GOED!")
            i=0
            answercorrect=True
        elif ((result != uitkomst) and (i>2)):
            i=0
            answercorrect=False
        else:
            i +=1
            answercorrect=False
            print("i backend = "+ str(i))
            print("Self.counter = "+ str(self.counter))
        return(i,result,answercorrect)

    def MailResults(self,today_score,quit):
        '''
        Mail the score to a fixed mail adres.

        Args:
            today_score(int): the Score
            quit(bool):


        Returns:
            nothing


        '''

        print(today_score)
        email="*****@gmail.com"
        from_email="*****@gmail.com"
        from_password="*******"
        to_email=email
        subject="Uitkomst van de rekentoets"
        message="De score van vandaag is <strong>%s</strong> minuten" %(today_score/60)
        msg=MIMEText(message, 'html')
        msg['Subject']=subject
        msg['To']= to_email
        msg['From'] = from_email

        try:
            gmail=smtplib.SMTP('smtp.gmail.com',587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login(from_email, from_password)
            gmail.send_message(msg)

        except:
            print("Er kon geen verbinding gemaakt worden met GMAIL")
            messagebox.showinfo("Information","Er kon geen verbinding gemaakt worden met Gmail")



    def play_buzzer(self):
        '''
        Plays a buzzer sound

        '''
        mixer.init()
        mixer.music.load('Loudbuzzer.mp3')
        mixer.music.play()
