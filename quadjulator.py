from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import time
from math import sqrt

def test(event):
    global myimg # global keyword allows access to a variable from outside of function



def math():

    global cA
    #make new steps frame
    sframe.destroy()
    sframe2 = Frame(root,borderwidth = 1.5, relief=RAISED, width=220,height=332)
    sframe2.place(x=250,y=35)
    sframe2.pack_propagate(0)
    l4 = Label(sframe2,text="How Computer Solves Equation", fg="#b50909")
    l4.pack(side = TOP)
    #make new answer frame
    aframe.destroy()
    aframe2 = Frame(root,borderwidth = 1.5, relief=RAISED, width=130,height=260)
    aframe2.place(x=475,y=105)
    aframe2.pack_propagate(0)
    l6 = Label(aframe2,text="Solutions", fg="#b50909")
    l6.pack(side=TOP)
    
    if len(E1.get())>0 and len(E2.get())>0 and len(E3.get())>0: #If something is entered in every entry box


        #check if numbers are entered
        try:
            cA = float(E1.get()) #Checks if Coefficient A is a Number
            cB = float(E2.get()) #Checks if Coefficient B is a Number
            cC = float(E3.get()) #Checks if Coefficient C is a Number
            if cA==0: #Check if Coefficient A is 0 because if it is, it is not a quadratic equation.
                l13=Label(aframe2,text="\n\n\n Coefficient A = 0\n so this is not\n a quadratic\n equation", fg="black")
                l13.pack(side=TOP)
                
            #writing steps using quadratic adding formula
        
            as1="\nx=-({1})+sqrt({1}^2-4*{0}*{2})/2*({0})".format(round(cA,2),round(cB,2),round(cC,2)) #substituting entries into formula
            as2="x={0}+sqrt({1}-({2}))/{3}".format(round(-cB,2),round(cB*cB,2),round(4*cA*cC,2),round(2*cA,2)) #Each step from here to step 6 does algebra to solve for X
            as3="x={0}+sqrt({1})/{2}".format(round(-cB,2),round((cB*cB)-(4*cA*cC),2),round(2*cA,2))
            try: #This activates ff you do not have to sqare root a negative number. A negative number cannot be square rooted.
                as4="x={0}+{1}/{2}".format(round(-cB,2),round(sqrt((cB*cB)-(4*cA*cC)),2),round(2*cA,2))
                as5="x={0}/{1}".format(round(-cB + sqrt((cB*cB)-(4*cA*cC)),2),round(2*cA,2))
                try: #This activates if nothing divdided by 0 in the next 8 lines
                    as6="x={0}".format(round(((-cB) + sqrt((cB*cB)-(4*cA*cC)))/(2*cA),2))
                    asteps=[as1,as2,as3,as4,as5,as6] # all steps in addition formula stored in a list

                    for i in range(len (asteps)): #repeats the same number of times as the lenth of the list above
                        l9=Label(sframe2, text = asteps[i],fg="black") #writes each step as a label
                        l9.pack(side=TOP)
                        l9.config(font=("cambria",9))
            
                except ZeroDivisionError: #If anything is divided by 0 this will activate
                    a = 1 #Nothing Needs to happen so variable a will never be used


            except ValueError: #This activates if the previous math makes you sqaure root a negative number which is impossible 
                l13=Label(aframe2,text="\n\n The are no\n solutions", fg="black")
                l13.pack(side=TOP)
                
            #writing steps using quadratic substacting formula
            
            ss0="\nOr"
            ss1="\nx=-({1})-sqrt({1}^2-4*{0}*{2})/2*({0})".format(round(cA,2),round(cB,2),round(cC,2)) #substituting entries into formula
            ss2="x={0}-sqrt({1}-({2}))/{3}".format(round(-cB,2),round(cB*cB,2),round(4*cA*cC,2),round(2*cA,2)) #Each step from here to step 6 do algebra to solve for X
            ss3="x={0}-sqrt({1})/{2}".format(round(-cB,2),round((cB*cB)-(4*cA*cC),2),round(2*cA,2))
            try: #This activates ff you do not have to sqare root a negative number. A negative number cannot be square rooted
                ss4="x={0}-{1}/{2}".format(round(-cB,2),round(sqrt((cB*cB)-(4*cA*cC)),2),round(2*cA,2))
                ss5="x={0}/{1}".format(round((-cB) - sqrt((cB*cB)-(4*cA*cC)),2),round(2*cA,2))
                try: #This activates if nothing divdided by 0 in the next 8 lines
                    ss6="x={0}".format(round(((-cB) - sqrt((cB*cB)-(4*cA*cC)))/(2*cA),2))
                    ssteps=[ss0,ss1,ss2,ss3,ss4,ss5,ss6]# all steps in subtraction formula stored in a list
                    for j in range(len (ssteps)): #repeats the same number of times as the lenth of the list above
                        l10=Label(sframe2, text = ssteps[j],fg="black") #writes each step as a label
                        l10.pack(side=TOP)
                        l10.config(font=("cambria",9))
                        
                    #Create File with all of Computer's Steps

                    fo = open("qsteps.txt","w") #opens file named qsteps.txt to write
                    fo.write("Here are the computer's full steps to solve the equation:\n")
                    for j in range(6): #for loop repeating same # of times as lenth of asteps
                        fo.write(asteps[j]) #This will write all elements in asteps
                        fo.write("\n") #This will separate each item with a line
                    for j in range(len (ssteps)): #for loop repeating same # of times as lenth of ssteps
                        fo.write(ssteps[j])#This will write all elements in ssteps
                        fo.write("\n")#This will separate each item with a line
                    fo.close() #Closes file
                    l15=Label(sframe2,text="Find computer's full steps to solve equation\n on your file named qsteps.txt.",fg="black")
                    l15.config(font=("cambria",9))
                    l15.pack(side=BOTTOM)
                except ZeroDivisionError: #If anything is divided by 0 this will activate
                    a = 1 #Nothing Needs to happen so variable a will never be used
            except ValueError: #This activates if the previous math makes you sqaure root a negative number which is impossible
                a = 1 #Nothing Needs to happen so variable a will never be used
        
            #Calculate Discriminant
            Di = (cB)**2 - 4*(cA)*(cC)
            
            if Di > 0 and cA != 0:#if there is two answers
                a1 = round(((-cB) + sqrt((cB*cB)-(4*cA*cC)))/(2*cA),2) #this is the answer with adding formula
                a2 = round(((-cB) - sqrt((cB*cB)-(4*cA*cC)))/(2*cA),2) #this is theanswer with subtracting formula
                l7 = Label(aframe2, text = "\nThere are 2\n possible answers:\n\n\nX = {0} \nor \nX = {1}\n\n\n*Rounded to\n two decimal\n places".format(round(a1,2),round(a2,2)),fg="black")
                l7.pack(side=TOP)
            elif Di == 0 and cA > 0:#if the discriminant equal 0 meaning there is one answer
                a3 = (-cB)/(2*cA) #this is the only answer if discriminant equals 0
                l12=Label(aframe2,text="\nThe only\n possible asnwer\n is:\n\n\nX = {0}\n\n\n*Rounded to\n two decimal\n places".format(a3))
                l12.pack(side=TOP)

        except ValueError or UnboundLocalError: #Check if Non-numbers are entered
            l11 = Label(aframe2,text="\n\n\nYou did not\n enter numbers\n for all three\n coefficients",fg="black")
            l11.pack(side=TOP)
    
    else: #if nothing is entered
        l8=Label(aframe2, text = "\n\n\nEnter all\n Coefficients", fg = "black")
        l8.pack(side=TOP)
    
root = Tk()
root.title("Quadjulator")
root.geometry("615x380")

# make 'navbar' frame - info http://effbot.org/tkinterbook/frame.htm
topframe = Frame(root,bg="#b50909")
topframe.pack(fill=X)
l6 = Label(topframe,text="Quadratic Formula:", bg = "#b50909", fg = "white")
l6.pack(side=RIGHT)

# make a small canvas hamburger icon that binds as a button to a function
can1 = Canvas(topframe,height="20",bg="#b50909",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill="white")
can1.create_line(0, 10, 20, 10,fill="white")
can1.create_line(0, 15, 20, 15,fill="white")
can1.bind("<Button-1>",test )
can1.pack(side=LEFT, padx=5, pady=5)


# title frame
titleframe = Frame(root,borderwidth = 1.5, relief=RAISED)
titleframe.place(x=475,y=35)
canvas = Canvas(titleframe,height=50,width=120)
canvas.pack(side=RIGHT)
myimage = Image.open("quad.png")
myimage = myimage.resize((140, 50), Image.ANTIALIAS)
myimg = ImageTk.PhotoImage(myimage)
canvas.create_image(0, 0, image=myimg, anchor = NW)


# instructions frame

inframe = Frame(root,borderwidth = 1.5, relief=RAISED)
inframe.place(x=4,y=40)
l1 = Label(inframe,text="This program can find the \nsolutions for any quadratic\n equation. Simply enter the three \ncoefficients in a quadratic equation\n in the form Ax^2 + Bx + C = 0\n below. This program will solve\n for all possible values for X!",fg="#b50909")
l1.pack(side=LEFT)

# Coefficient Entries

cframe = Frame(root,borderwidth = 1.5, relief=RAISED)
cframe.place(x=17,y=175)
l2 = Label(cframe,text=" Enter Coefficients Below",fg="#b50909")
l2.pack(side = TOP)
l3 = Label(cframe,text="A:\n\n\n B:\n\n\n C:",fg="#b50909")
l3.pack(side = LEFT)
E1 = Entry(cframe)
E1.pack(side=TOP,ipady=10)
E2 = Entry(cframe)
E2.pack(side=TOP,ipady=10)
E3 = Entry(cframe)
E3.pack(side=TOP,ipady=10)

# Steps Frame: Computer's steps to solve equation 

sframe = Frame(root,borderwidth = 1.5, relief=RAISED, width=220,height=332)
sframe.place(x=250,y=35)
sframe.pack_propagate(0)
l4 = Label(sframe,text="How Computer Solves Equation", fg="#b50909")
l4.pack(side = TOP)

# Solution Frame

aframe = Frame(root,borderwidth = 1.5, relief=RAISED, width=130,height=260)
aframe.place(x=475,y=105)
aframe.pack_propagate(0)
l6 = Label(aframe,text="Solutions", fg="#b50909")
l6.pack(side = TOP)

# Button to activate math function

B1 = Button(cframe, text="Solve",command=math,fg="#b50909")
B1.pack(side = BOTTOM)
root.mainloop()
