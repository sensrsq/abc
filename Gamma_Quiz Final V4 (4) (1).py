#Imports for tkinter, os, counting tool, ect.
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from itertools import count

#Master frame along with title and size
master=Tk()
master.title("English Quiz :D")
master.geometry("900x600")

#PlayerScore Counting established here for later use
PlayerScore = 0


#Frames for Windows:
#The frames are organised so each question gets its own frame and the 4 multiple choice answers are each given their own frame to interpret the answer,
#give designated feedback and outline if you have chosen the correct option
#The only exceptions to this method are the start frame which allows your to actually being the quiz and the ending frames which are arranged in a different manner
#Also the reflection frames, "Quiz1" and "Quiz2"
frameStart = Frame(master)

frameOne = Frame(master)
frameOneA = Frame(master)
frameOneB = Frame(master)
frameOneC = Frame(master)
frameOneD = Frame(master)

frameTwo = Frame(master)
frameTwoA = Frame(master)
frameTwoB = Frame(master)
frameTwoC = Frame(master)
frameTwoD = Frame(master)

frameThree = Frame(master)
frameThreeA = Frame(master)
frameThreeB = Frame(master)
frameThreeC = Frame(master)
frameThreeD = Frame(master)

frameFour = Frame(master)
frameFourA = Frame(master)
frameFourB = Frame(master)
frameFourC = Frame(master)
frameFourD = Frame(master)

frameFive = Frame(master)
frameFiveA = Frame(master)
frameFiveB = Frame(master)
frameFiveC = Frame(master)
frameFiveD = Frame(master)

frameSix = Frame(master)
frameSixA = Frame(master)
frameSixB = Frame(master)
frameSixC = Frame(master)
frameSixD = Frame(master)

frameSeven = Frame(master)
frameSevenA = Frame(master)
frameSevenB = Frame(master)
frameSevenC = Frame(master)
frameSevenD = Frame(master)

frameEight = Frame(master)
frameEightA = Frame(master)
frameEightB = Frame(master)
frameEightC = Frame(master)
frameEightD = Frame(master)

frameNine = Frame(master)
frameNineA = Frame(master)
frameNineB = Frame(master)
frameNineC = Frame(master)
frameNineD = Frame(master)

frameTen = Frame(master)
frameTenA = Frame(master)
frameTenB = Frame(master)
frameTenC = Frame(master)
frameTenD = Frame(master)

frameEnd = Frame(master)

frameQuiz1 = Frame(master)
frameQuiz2 = Frame(master)

#The counter or second stopwatch that measures the time is established at 0 seconds to begin
counter=0

#This function runs the second count when "Frame1Label" is implemented
#The function itself allows for the counter to increase in value after each second and other properties of a stopwatch
def start_counter(Frame1Label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

#ChangeScore is a function that imcreases the playerscore by a given amount when a number is given in the place of "Value"
def ChangeScore(Value):
    global PlayerScore
    PlayerScore = Value + PlayerScore
        
#OpenFrame1 is a function that immediately replaces the starting frame with the first question frame
#This frame will always stay the same, however, therre will be a designated messagebox opened if the user either responds with their year level in FrameStart as 9, 11 or any other response other than 10,
    #The difference being that if an answer other than 9, 10 or 11 is given, the user will not be permitted to advance in the quiz
#First we global (Call in) counter in order to begin the timer, then the score is placed in the top right corner of the frame
#Then after the distinction of year levels, The counter label is place, the counter is reset due to some mild errors that were mitigated during testing, and an empty label named "Space" is defined
#After this, the labels telling which question this is and the written options are established
#These option labels are acccompanied by buttons that will signify which option is being chosen along with the command to open the answer frame for that specific option
    #Addtionally, the Image, as defined near the bottom, is set below the question before forgetting the starting frame (but not its contents) and packing the current frame
def OpenFrame1():
    global counter
    TopLabel.place(x=15, y=2)
    ScoreLabel.place(x=66,y=25)
    if YrTextField.get() == "10" and NameTextField.get() != "":
        counter = 0
        label.place(x=845, y=5)
        Space = Label(frameOne, text="")
        
        Frame1Label = Label(frameOne, text="First Question Window")
        Question1 = Label(frameOne, text="Which sentence is correct?", font=5, fg='blue')
        OptionA = Button(frameOne, text="A", command= OpenFrame1A, font=2)
        OptionALabel = Label(frameOne, text="The decoration of the cupcakes is always in different colours that represents each house at school")
        OptionB = Button(frameOne, text="B", command=lambda: [ChangeScore(1), OpenFrame1B()], font=2)
        OptionBLabel = Label(frameOne, text="The decoration of the cupcakes is always in different colours that represent each house at school")
        OptionC = Button(frameOne, text="C", command= OpenFrame1C, font=2)
        OptionCLabel = Label(frameOne, text="The decoration of the cupcakes are always in different colours that represents each house at school")
        OptionD = Button(frameOne, text="D", command= OpenFrame1D, font=2)
        OptionDLabel = Label(frameOne, text="The decoration of the cupcakes are always in different colours that represent each house at school")
        
        Frame1Label.pack()
        Space.pack()
        Question1.pack()
        Space.pack()
        OptionA.pack()
        OptionALabel.pack()
        OptionB.pack()
        OptionBLabel.pack()
        OptionC.pack()
        OptionCLabel.pack()
        OptionD.pack()
        OptionDLabel.pack()
        Q1ImgLabel.pack()
        frameStart.pack_forget()
        frameOne.pack()
    elif YrTextField.get() == "9" and NameTextField.get() != "":
        counter = 0
        label.place(x=845, y=5)
        mboxYoung()
        Space = Label(frameOne, text="")
        
        Frame1Label = Label(frameOne, text="First Question Window")
        Question1 = Label(frameOne, text="Which sentence is correct?", font=5, fg='blue')
        OptionA = Button(frameOne, text="A", command= OpenFrame1A, font=2)
        OptionALabel = Label(frameOne, text="The decoration of the cupcakes is always in different colours that represents each house at school")
        OptionB = Button(frameOne, text="B", command=lambda: [ChangeScore(1), OpenFrame1B()], font=2)
        OptionBLabel = Label(frameOne, text="The decoration of the cupcakes is always in different colours that represent each house at school")
        OptionC = Button(frameOne, text="C", command= OpenFrame1C, font=2)
        OptionCLabel = Label(frameOne, text="The decoration of the cupcakes are always in different colours that represents each house at school")
        OptionD = Button(frameOne, text="D", command= OpenFrame1D, font=2)
        OptionDLabel = Label(frameOne, text="The decoration of the cupcakes are always in different colours that represent each house at school")
        
        Frame1Label.pack()
        Space.pack()
        Question1.pack()
        Space.pack()
        OptionA.pack()
        OptionALabel.pack()
        OptionB.pack()
        OptionBLabel.pack()
        OptionC.pack()
        OptionCLabel.pack()
        OptionD.pack()
        OptionDLabel.pack()
        Q1ImgLabel.pack()
        frameStart.pack_forget()
        frameOne.pack()
    elif YrTextField.get() == "11" and NameTextField.get() != "":
        counter = 0
        label.place(x=845, y=5)
        mboxOld()
        Space = Label(frameOne, text="")
        
        Frame1Label = Label(frameOne, text="First Question Window")
        Question1 = Label(frameOne, text="Which sentence is correct?", font=5, fg='blue')
        OptionA = Button(frameOne, text="A", command= OpenFrame1A, font=2)
        OptionALabel = Label(frameOne, text="The decoration of the cupcakes is always in different colours that represents each house at school")
        OptionB = Button(frameOne, text="B", command=lambda: [ChangeScore(1), OpenFrame1B()], font=2)
        OptionBLabel = Label(frameOne, text="The decoration of the cupcakes is always in different colours that represent each house at school")
        OptionC = Button(frameOne, text="C", command= OpenFrame1C, font=2)
        OptionCLabel = Label(frameOne, text="The decoration of the cupcakes are always in different colours that represents each house at school")
        OptionD = Button(frameOne, text="D", command= OpenFrame1D, font=2)
        OptionDLabel = Label(frameOne, text="The decoration of the cupcakes are always in different colours that represent each house at school")
        
        Frame1Label.pack()
        Space.pack()
        Question1.pack()
        Space.pack()
        OptionA.pack()
        OptionALabel.pack()
        OptionB.pack()
        OptionBLabel.pack()
        OptionC.pack()
        OptionCLabel.pack()
        OptionD.pack()
        OptionDLabel.pack()
        Q1ImgLabel.pack()
        frameStart.pack_forget()
        frameOne.pack()
    else:
        mbox()

#The function below will establish the first option of question one (Option A)
#First the label stating whether the answer given was correct is defined
#Additionally the labels for the previous frame's options are re-established for this function and frame along with the button to go to the next question frame
    #The option labels however will have changed to indicate whether or not the chosen answer was correct, with red options being incorrect responses from users and green options being either correct
    #options given by the user or what would have been the correct option if the user was incorrect
#All these parts are then packed into the current frame and the previous question frame is forgotten
def OpenFrame1A():
    BigLabel = Label(frameOneA, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameOneA, text="The decoration of the cupcakes is always in different colours that represents each house at school. (YOUR ANSWER)", fg='red')
    OptionBLabel = Label(frameOneA, text="The decoration of the cupcakes is always in different colours that represent each house at school (CORRECT ANSWER)", fg='green')   
    OptionCLabel = Label(frameOneA, text="The decoration of the cupcakes are always in different colours that represents each house at school")   
    OptionDLabel = Label(frameOneA, text="The decoration of the cupcakes are always in different colours that represent each house at school")
    Frame1AButton = Button(frameOneA, text = "Next question", command= OpenFrame2)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame1AButton.pack()
    frameOne.pack_forget()
    frameOneA.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments, however, here the user will have made the correct choice and only the correct option is highlighted as to
#indicate a correct response along with the different "BigLabel" also showing that the user was correct
def OpenFrame1B():
    BigLabel = Label(frameOneB, text="CORRECT", font=8, fg='green')
                     
    OptionALabel = Label(frameOneB, text="The decoration of the cupcakes is always in different colours that represents each house at school.")
    OptionBLabel = Label(frameOneB, text="The decoration of the cupcakes is always in different colours that represent each house at school (YOUR ANSWER)(CORRECT ANSWER)", fg='green')   
    OptionCLabel = Label(frameOneB, text="The decoration of the cupcakes are always in different colours that represents each house at school")   
    OptionDLabel = Label(frameOneB, text="The decoration of the cupcakes are always in different colours that represent each house at school")
    Frame1BButton = Button(frameOneB, text = "Next question", command= OpenFrame2)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame1BButton.pack()
    frameOne.pack_forget()
    frameOneB.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame1C():
    BigLabel = Label(frameOneC, text="INCORRECT", font=8, fg='red')
    
    OptionALabel = Label(frameOneC, text="The decoration of the cupcakes is always in different colours that represents each house at school.")
    OptionBLabel = Label(frameOneC, text="The decoration of the cupcakes is always in different colours that represent each house at school (CORRECT ANSWER)", fg='green')   
    OptionCLabel = Label(frameOneC, text="The decoration of the cupcakes are always in different colours that represents each house at school (YOUR ANSWER)", fg='red')   
    OptionDLabel = Label(frameOneC, text="The decoration of the cupcakes are always in different colours that represent each house at school")
    Frame1CButton = Button(frameOneC, text = "Next question", command= OpenFrame2)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame1CButton.pack()
    frameOne.pack_forget()
    frameOneC.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame1D():
    BigLabel = Label(frameOneD, text="INCORRECT", font=8, fg='red')
    
    OptionALabel = Label(frameOneD, text="The decoration of the cupcakes is always in different colours that represents each house at school.")
    OptionBLabel = Label(frameOneD, text="The decoration of the cupcakes is always in different colours that represent each house at school (CORRECT ANSWER)", fg='green')   
    OptionCLabel = Label(frameOneD, text="The decoration of the cupcakes are always in different colours that represents each house at school")   
    OptionDLabel = Label(frameOneD, text="The decoration of the cupcakes are always in different colours that represent each house at school (YOUR ANSWER)", fg='red')
    Frame1DButton = Button(frameOneD, text = "Next question", command= OpenFrame2)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame1DButton.pack()
    frameOne.pack_forget()
    frameOneD.pack()

#OpenFrame2 is a function that immediately replaces the starting frame with the first question frame
#First we update the score through a configuration then replacement where the score is placed in the top right corner of the frame
#Then an empty label named "Space" is defined and after this, the labels telling which question this is and the written options are established
#These option labels are acccompanied by buttons that will signify which option is being chosen along with the command to open the answer frame for that specific option
    #Addtionally, the Image, as defined near the bottom, is set below the question before forgetting the starting frame (but not its contents) and packing the current frame
def OpenFrame2():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameTwo, text="")
    
    Frame2Label = Label(frameTwo, text="Second Question Window")
    Question2 = Label(frameTwo, text="Complete the analogy - Frailty is to Strength as Shame is to ___", font=5, fg='blue')
    OptionA = Button(frameTwo, text="A", command=lambda: [ChangeScore(1), OpenFrame2A()], font=2)
    OptionALabel = Label(frameTwo, text="Pride")
    OptionB = Button(frameTwo, text="B", command= OpenFrame2B, font=2)
    OptionBLabel = Label(frameTwo, text="Passion")
    OptionC = Button(frameTwo, text="C", command= OpenFrame2C, font=2)
    OptionCLabel = Label(frameTwo, text="Relief")
    OptionD = Button(frameTwo, text="D", command= OpenFrame2D, font=2)
    OptionDLabel = Label(frameTwo, text="Embarassment")

    ScoreLabel.place(x=66,y=25)
    Frame2Label.pack()
    Space.pack()
    Question2.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q2ImgLabel.pack()
    frameOneA.pack_forget()
    frameOneB.pack_forget()
    frameOneC.pack_forget()
    frameOneD.pack_forget()
    frameTwo.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame2A():
    BigLabel = Label(frameTwoA, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameTwoA, text="Pride (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    OptionBLabel = Label(frameTwoA, text="Passion")
    OptionCLabel = Label(frameTwoA, text="Relief")
    OptionDLabel = Label(frameTwoA, text="Embarassment")
    Frame2AButton = Button(frameTwoA, text = "Next question", command= OpenFrame3)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame2AButton.pack()
    frameTwo.pack_forget()
    frameTwoA.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame2B():
    BigLabel = Label(frameTwoB, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameTwoB, text="Pride (CORRECT ANSWER)", fg='green')
    OptionBLabel = Label(frameTwoB, text="Passion (YOUR ANSWER)", fg='red')
    OptionCLabel = Label(frameTwoB, text="Relief")
    OptionDLabel = Label(frameTwoB, text="Embarassment")
    Frame2BButton = Button(frameTwoB, text = "Next question", command= OpenFrame3)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame2BButton.pack()
    frameTwo.pack_forget()
    frameTwoB.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame2C():
    BigLabel = Label(frameTwoC, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameTwoC, text="Pride (CORRECT ANSWER)", fg='green')
    OptionBLabel = Label(frameTwoC, text="Passion")
    OptionCLabel = Label(frameTwoC, text="Relief (YOUR ANSWER)", fg='red')
    OptionDLabel = Label(frameTwoC, text="Embarassment")
    Frame2CButton = Button(frameTwoC, text = "Next question", command= OpenFrame3)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame2CButton.pack()
    frameTwo.pack_forget()
    frameTwoC.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame2D():
    BigLabel = Label(frameTwoD, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameTwoD, text="Pride (CORRECT ANSWER)", fg='green')
    OptionBLabel = Label(frameTwoD, text="Passion")
    OptionCLabel = Label(frameTwoD, text="Relief")
    OptionDLabel = Label(frameTwoD, text="Embarassment (YOUR ANSWER)", fg='red')
    Frame2DButton = Button(frameTwoD, text = "Next question", command= OpenFrame3)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame2DButton.pack()
    frameTwo.pack_forget()
    frameTwoD.pack()

#This function works off of the same principles of "OpenFrame2" as described in the comments
def OpenFrame3():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameThree, text="")
    
    Frame3Label = Label(frameThree, text="Third Question Window")
    Question3 = Label(frameThree, text="Complete the Correlation - Child : Childhood, Nation : ___", font=5, fg='blue')
    OptionA = Button(frameThree, text="A", command= OpenFrame3A, font=2)
    OptionALabel = Label(frameThree, text="Nationale")
    OptionB = Button(frameThree, text="B", command=lambda: [ChangeScore(1), OpenFrame3B()], font=2)
    OptionBLabel = Label(frameThree, text="Nationhood")
    OptionC = Button(frameThree, text="C", command= OpenFrame3C, font=2)
    OptionCLabel = Label(frameThree, text="Patriotism")
    OptionD = Button(frameThree, text="D", command= OpenFrame3D, font=2)
    OptionDLabel = Label(frameThree, text="Liberalism")

    ScoreLabel.place(x=66,y=25)
    Frame3Label.pack()
    Space.pack()
    Question3.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q3ImgLabel.pack()
    frameTwoA.pack_forget()
    frameTwoB.pack_forget()
    frameTwoC.pack_forget()
    frameTwoD.pack_forget()
    frameThree.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame3A():
    BigLabel = Label(frameThreeA, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameThreeA, text="Nationale (YOUR ANSWER)", fg='red')
    OptionBLabel = Label(frameThreeA, text="Nationhood (CORRECT ANSWER)", fg='green')
    OptionCLabel = Label(frameThreeA, text="Patriotism")
    OptionDLabel = Label(frameThreeA, text="Liberalism")
    Frame3AButton = Button(frameThreeA, text = "Next question", command= OpenFrame4)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame3AButton.pack()
    frameThree.pack_forget()
    frameThreeA.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame3B():
    BigLabel = Label(frameThreeB, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameThreeB, text="Nationale")
    OptionBLabel = Label(frameThreeB, text="Nationhood (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    OptionCLabel = Label(frameThreeB, text="Patriotism")
    OptionDLabel = Label(frameThreeB, text="Liberalism")
    Frame3BButton = Button(frameThreeB, text = "Next question", command= OpenFrame4)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame3BButton.pack()
    frameThree.pack_forget()
    frameThreeB.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame3C():
    BigLabel = Label(frameThreeC, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameThreeC, text="Nationale")
    OptionBLabel = Label(frameThreeC, text="Nationhood(CORRECT ANSWER)", fg='green')
    OptionCLabel = Label(frameThreeC, text="Patriotism (YOUR ANSWER)", fg='red')
    OptionDLabel = Label(frameThreeC, text="Liberalism")
    Frame3CButton = Button(frameThreeC, text = "Next question", command= OpenFrame4)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame3CButton.pack()
    frameThree.pack_forget()
    frameThreeC.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame3D():
    BigLabel = Label(frameThreeD, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameThreeD, text="Nationale")
    OptionBLabel = Label(frameThreeD, text="Nationhood(CORRECT ANSWER)", fg='green')
    OptionCLabel = Label(frameThreeD, text="Patriotism")
    OptionDLabel = Label(frameThreeD, text="Liberalism (YOUR ANSWER)", fg='red')
    Frame3DButton = Button(frameThreeD, text = "Next question", command= OpenFrame4)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame3DButton.pack()
    frameThree.pack_forget()
    frameThreeD.pack()

#This function works off of the same principles of "OpenFrame2" as described in the comments
def OpenFrame4():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameFour, text="")
    
    Frame4Label = Label(frameFour, text="Fourth Question Window")
    Question4 = Label(frameFour, text="Identify the independent clause -  The hospital recently hired a brilliant brain surgeon", font=5, fg='blue')
    Question44 = Label(frameFour, text=" whose cardiology research has recently revolutionised heart transplant procedures.", font=5, fg='blue')
    OptionA = Button(frameFour, text="A", command= OpenFrame4A, font=2)
    OptionALabel = Label(frameFour, text="a brilliant brain surgeon whose cardiology research has recently revolutionised heart transplant procedures.")
    OptionB = Button(frameFour, text="B", command= OpenFrame4B, font=2)
    OptionBLabel = Label(frameFour, text="The hospital recently hired")
    OptionC = Button(frameFour, text="C", command= OpenFrame4C, font=2)
    OptionCLabel = Label(frameFour, text="cardiology research has recently revolutionised heart transplant procedures")
    OptionD = Button(frameFour, text="D", command=lambda: [ChangeScore(1), OpenFrame4D()], font=2)
    OptionDLabel = Label(frameFour, text="The hospital recently hired a brilliant brain surgeon")

    ScoreLabel.place(x=66,y=25)
    Frame4Label.pack()
    Space.pack()
    Question4.pack()
    Question44.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q4ImgLabel.pack()
    frameThreeA.pack_forget()
    frameThreeB.pack_forget()
    frameThreeC.pack_forget()
    frameThreeD.pack_forget()
    frameFour.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame4A():
    BigLabel = Label(frameFourA, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameFourA, text="a brilliant brain surgeon whose cardiology research has recently revolutionised heart transplant procedures (YOUR ANSWER)", fg='red')
    OptionBLabel = Label(frameFourA, text="The hospital recently hired")
    OptionCLabel = Label(frameFourA, text="cardiology research has recently revolutionised heart transplant procedures")
    OptionDLabel = Label(frameFourA, text="The hospital recently hired a brilliant brain surgeon (CORRECT ANSWER)", fg='green')
    Frame4AButton = Button(frameFourA, text = "Next question", command= OpenFrame5)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame4AButton.pack()
    frameFour.pack_forget()
    frameFourA.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame4B():
    BigLabel = Label(frameFourB, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameFourB, text="a brilliant brain surgeon whose cardiology research has recently revolutionised heart transplant procedures")
    OptionBLabel = Label(frameFourB, text="The hospital recently hired (YOUR ANSWER)", fg='red')
    OptionCLabel = Label(frameFourB, text="cardiology research has recently revolutionised heart transplant procedures")
    OptionDLabel = Label(frameFourB, text="The hospital recently hired a brilliant brain surgeon (CORRECT ANSWER)", fg='green')
    Frame4BButton = Button(frameFourB, text = "Next question", command= OpenFrame5)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame4BButton.pack()
    frameFour.pack_forget()
    frameFourB.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame4C():
    BigLabel = Label(frameFourC, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameFourC, text="a brilliant brain surgeon whose cardiology research has recently revolutionised heart transplant procedures")
    OptionBLabel = Label(frameFourC, text="The hospital recently hired")
    OptionCLabel = Label(frameFourC, text="cardiology research has recently revolutionised heart transplant procedures (YOUR ANSWER)", fg='red')
    OptionDLabel = Label(frameFourC, text="The hospital recently hired a brilliant brain surgeon (CORRECT ANSWER)", fg='green')
    Frame4CButton = Button(frameFourC, text = "Next question", command= OpenFrame5)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame4CButton.pack()
    frameFour.pack_forget()
    frameFourC.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame4D():
    BigLabel = Label(frameFourD, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameFourD, text="a brilliant brain surgeon whose cardiology research has recently revolutionised heart transplant procedures")
    OptionBLabel = Label(frameFourD, text="The hospital recently hired")
    OptionCLabel = Label(frameFourD, text="cardiology research has recently revolutionised heart transplant procedures")
    OptionDLabel = Label(frameFourD, text="The hospital recently hired a brilliant brain surgeon (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    Frame4DButton = Button(frameFourD, text = "Next question", command= OpenFrame5)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame4DButton.pack()
    frameFour.pack_forget()
    frameFourD.pack()

#This function works off of the same principles of "OpenFrame2" as described in the comments
def OpenFrame5():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameFive, text="")
    
    Frame5Label = Label(frameFive, text="Fifth Question Window")
    Question5 = Label(frameFive, text="Correct the spelling of the word - Kalideoskope", font=5, fg='blue')
    OptionA = Button(frameFive, text="A", command= OpenFrame5A, font=2)
    OptionALabel = Label(frameFive, text="Kaliedeoscope")
    OptionB = Button(frameFive, text="B", command= OpenFrame5B, font=2)
    OptionBLabel = Label(frameFive, text="Kaleidoskope")
    OptionC = Button(frameFive, text="C", command=lambda: [ChangeScore(1), OpenFrame5C()], font=2)
    OptionCLabel = Label(frameFive, text="Kaleidoscope")
    OptionD = Button(frameFive, text="D", command= OpenFrame5D, font=2)
    OptionDLabel = Label(frameFive, text="Kalideoscope")

    ScoreLabel.place(x=66,y=25)
    Frame5Label.pack()
    Space.pack()
    Question5.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q5ImgLabel.pack()
    frameFourA.pack_forget()
    frameFourB.pack_forget()
    frameFourC.pack_forget()
    frameFourD.pack_forget()
    frameFive.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame5A():
    BigLabel = Label(frameFiveA, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameFiveA, text="Kaliedeoscope (YOUR ANSWER)", fg='red')
    OptionBLabel = Label(frameFiveA, text="Kaleidoskope")
    OptionCLabel = Label(frameFiveA, text="Kaleidoscope (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameFiveA, text="Kalideoscope")
    Frame5AButton = Button(frameFiveA, text = "Next question", command= OpenFrame6)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame5AButton.pack()
    frameFive.pack_forget()
    frameFiveA.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame5B():
    BigLabel = Label(frameFiveB, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameFiveB, text="Kaliedeoscope")
    OptionBLabel = Label(frameFiveB, text="Kaleidoskope (YOUR ANSWER)", fg='red')
    OptionCLabel = Label(frameFiveB, text="Kaleidoscope (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameFiveB, text="Kalideoscope")
    Frame5BButton = Button(frameFiveB, text = "Next question", command= OpenFrame6)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame5BButton.pack()
    frameFive.pack_forget()
    frameFiveB.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame5C():
    BigLabel = Label(frameFiveC, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameFiveC, text="Kaliedeoscope")
    OptionBLabel = Label(frameFiveC, text="Kaleidoskope")
    OptionCLabel = Label(frameFiveC, text="Kaleidoscope (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameFiveC, text="Kalideoscope")
    Frame5CButton = Button(frameFiveC, text = "Next question", command= OpenFrame6)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame5CButton.pack()
    frameFive.pack_forget()
    frameFiveC.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame5D():
    BigLabel = Label(frameFiveD, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameFiveD, text="Kaliedeoscope")
    OptionBLabel = Label(frameFiveD, text="Kaleidoskope")
    OptionCLabel = Label(frameFiveD, text="Kaleidoscope (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameFiveD, text="Kalideoscope (YOUR ANSWER)", fg='red')
    Frame5DButton = Button(frameFiveD, text = "Next question", command= OpenFrame6)

    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame5DButton.pack()
    frameFive.pack_forget()
    frameFiveD.pack()

#This function works off of the same principles of "OpenFrame2" as described in the comments
def OpenFrame6():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameSix, text="")
    
    Frame6Label = Label(frameSix, text="Sixth Question Window")
    Question6 = Label(frameSix, text="Complete the Analogy - Cyclops is to ___ as Ox is to Oxen", font=5, fg='blue')
    OptionA = Button(frameSix, text="A", command=lambda: [ChangeScore(1), OpenFrame6A()], font=2)
    OptionALabel = Label(frameSix, text="Cyclopes")
    OptionB = Button(frameSix, text="B", command= OpenFrame6B, font=2)
    OptionBLabel = Label(frameSix, text="Cyslopses")
    OptionC = Button(frameSix, text="C", command= OpenFrame6C, font=2)
    OptionCLabel = Label(frameSix, text="Cylopsi")
    OptionD = Button(frameSix, text="D", command= OpenFrame6D, font=2)
    OptionDLabel = Label(frameSix, text="Cyclops")

    ScoreLabel.place(x=66,y=25)
    Frame6Label.pack()
    Space.pack()
    Question6.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q6ImgLabel.pack()
    frameFiveA.pack_forget()
    frameFiveB.pack_forget()
    frameFiveC.pack_forget()
    frameFiveD.pack_forget()
    frameSix.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame6A():
    BigLabel = Label(frameSixA, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameSixA, text="Cyclopes (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    OptionBLabel = Label(frameSixA, text="Cyslopses")
    OptionCLabel = Label(frameSixA, text="Cylopsi")
    OptionDLabel = Label(frameSixA, text="Cyclops")
    Frame6AButton = Button(frameSixA, text = "Next question", command= OpenFrame7)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame6AButton.pack()
    frameSix.pack_forget()
    frameSixA.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame6B():
    BigLabel = Label(frameSixB, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameSixB, text="Cyclopes (CORRECT ANSWER)", fg='green')
    OptionBLabel = Label(frameSixB, text="Cyslopses (YOUR ANSWER)", fg='red')
    OptionCLabel = Label(frameSixB, text="Cylopsi")
    OptionDLabel = Label(frameSixB, text="Cyclops")
    Frame6BButton = Button(frameSixB, text = "Next question", command= OpenFrame7)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame6BButton.pack()
    frameSix.pack_forget()
    frameSixB.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame6C():
    BigLabel = Label(frameSixC, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameSixC, text="Cyclopes (CORRECT ANSWER)", fg='green')
    OptionBLabel = Label(frameSixC, text="Cyslopses")
    OptionCLabel = Label(frameSixC, text="Cylopsi (YOUR ANSWER)", fg='red')
    OptionDLabel = Label(frameSixC, text="Cyclops")
    Frame6CButton = Button(frameSixC, text = "Next question", command= OpenFrame7)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame6CButton.pack()
    frameSix.pack_forget()
    frameSixC.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame6D():
    BigLabel = Label(frameSixD, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameSixD, text="Cyclopes (CORRECT ANSWER)", fg='green')
    OptionBLabel = Label(frameSixD, text="Cyslopses")
    OptionCLabel = Label(frameSixD, text="Cylopsi")
    OptionDLabel = Label(frameSixD, text="Cyclops (YOUR ANSWER)", fg='red')
    Frame6DButton = Button(frameSixD, text = "Next question", command= OpenFrame7)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame6DButton.pack()
    frameSix.pack_forget()
    frameSixD.pack()

#This function works off of the same principles of "OpenFrame2" as described in the comments
def OpenFrame7():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameSeven, text="")
    
    Frame7Label = Label(frameSeven, text="Seventh Question Window")
    Question7 = Label(frameSeven, text="Convert this sentence into active voice: The chair was sat on by Pat.", font=5, fg='blue')
    OptionA = Button(frameSeven, text="A", command= OpenFrame7A, font=2)
    OptionALabel = Label(frameSeven, text="The chair is where Pat sat")
    OptionB = Button(frameSeven, text="B", command= OpenFrame7B, font=2)
    OptionBLabel = Label(frameSeven, text="On the chair Pat sat")
    OptionC = Button(frameSeven, text="C", command=lambda: [ChangeScore(1),  OpenFrame7C()], font=2)
    OptionCLabel = Label(frameSeven, text="Pat sat on the chair")
    OptionD = Button(frameSeven, text="D", command= OpenFrame7D, font=2)
    OptionDLabel = Label(frameSeven, text="Pat on the chair sat")

    ScoreLabel.place(x=66,y=25)
    Frame7Label.pack()
    Space.pack()
    Question7.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q7ImgLabel.pack()
    frameSixA.pack_forget()
    frameSixB.pack_forget()
    frameSixC.pack_forget()
    frameSixD.pack_forget()
    frameSeven.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame7A():
    BigLabel = Label(frameSevenA, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameSevenA, text="The chair is where Pat sat (YOUR ANSWER)", fg='red')
    OptionBLabel = Label(frameSevenA, text="On the chair Pat sat")
    OptionCLabel = Label(frameSevenA, text="Pat sat on the chair (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameSevenA, text="Pat on the chair sat")
    Frame7AButton = Button(frameSevenA, text = "Next question", command= OpenFrame8)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame7AButton.pack()
    frameSeven.pack_forget()
    frameSevenA.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame7B():
    BigLabel = Label(frameSevenB, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameSevenB, text="The chair is where Pat sat")
    OptionBLabel = Label(frameSevenB, text="On the chair Pat sat (YOUR ANSWER)", fg='red')
    OptionCLabel = Label(frameSevenB, text="Pat sat on the chair (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameSevenB, text="Pat on the chair sat")
    Frame7BButton = Button(frameSevenB, text = "Next question", command= OpenFrame8)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame7BButton.pack()
    frameSeven.pack_forget()
    frameSevenB.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame7C():
    BigLabel = Label(frameSevenC, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameSevenC, text="The chair is where Pat sat")
    OptionBLabel = Label(frameSevenC, text="On the chair Pat sat")
    OptionCLabel = Label(frameSevenC, text="Pat sat on the chair (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameSevenC, text="Pat on the chair sat")
    Frame7CButton = Button(frameSevenC, text = "Next question", command= OpenFrame8)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame7CButton.pack()
    frameSeven.pack_forget()
    frameSevenC.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame7D():
    BigLabel = Label(frameSevenD, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameSevenD, text="The chair is where Pat sat")
    OptionBLabel = Label(frameSevenD, text="On the chair Pat sat")
    OptionCLabel = Label(frameSevenD, text="Pat sat on the chair (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameSevenD, text="Pat on the chair sat (YOUR ANSWER)", fg='red')
    Frame7DButton = Button(frameSevenD, text = "Next question", command= OpenFrame8)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame7DButton.pack()
    frameSeven.pack_forget()
    frameSevenD.pack()

#This function works off of the same principles of "OpenFrame2" as described in the comments
def OpenFrame8():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameEight, text="")
    
    Frame8Label = Label(frameEight, text="Eighth Question Window")
    Question8 = Label(frameEight, text="Correct the spelling of the word - Peragitive", font=5, fg='blue')
    OptionA = Button(frameEight, text="A", command= OpenFrame8A, font=2)
    OptionALabel = Label(frameEight, text="Prerogitive")
    OptionB = Button(frameEight, text="B", command= OpenFrame8B, font=2)
    OptionBLabel = Label(frameEight, text="Perogative")
    OptionC = Button(frameEight, text="C", command= OpenFrame8C, font=2)
    OptionCLabel = Label(frameEight, text="Perogitive")
    OptionD = Button(frameEight, text="D", command=lambda: [ChangeScore(1),  OpenFrame8D()], font=2)
    OptionDLabel = Label(frameEight, text="Prerogative")

    ScoreLabel.place(x=66,y=25)
    Frame8Label.pack()
    Space.pack()
    Question8.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q8ImgLabel.pack()
    frameSevenA.pack_forget()
    frameSevenB.pack_forget()
    frameSevenC.pack_forget()
    frameSevenD.pack_forget()
    frameEight.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame8A():
    BigLabel = Label(frameEightA, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameEightA, text="Prerogitive (YOUR ANSWER)", fg='red')
    OptionBLabel = Label(frameEightA, text="Perogative")
    OptionCLabel = Label(frameEightA, text="Perogitive")
    OptionDLabel = Label(frameEightA, text="Prerogative (CORRECT ANSWER)", fg='green')
    Frame8AButton = Button(frameEightA, text = "Next question", command= OpenFrame9)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame8AButton.pack()
    frameEight.pack_forget()
    frameEightA.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame8B():
    BigLabel = Label(frameEightB, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameEightB, text="Prerogitive")
    OptionBLabel = Label(frameEightB, text="Perogative (YOUR ANSWER)", fg='red')
    OptionCLabel = Label(frameEightB, text="Perogitive")
    OptionDLabel = Label(frameEightB, text="Prerogative (CORRECT ANSWER)", fg='green')
    Frame8BButton = Button(frameEightB, text = "Next question", command= OpenFrame9)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame8BButton.pack()
    frameEight.pack_forget()
    frameEightB.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame8C():
    BigLabel = Label(frameEightC, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameEightC, text="Prerogitive")
    OptionBLabel = Label(frameEightC, text="Perogative")
    OptionCLabel = Label(frameEightC, text="Perogitive (YOUR ANSWER)", fg='red')
    OptionDLabel = Label(frameEightC, text="Prerogative (CORRECT ANSWER)", fg='green')
    Frame8CButton = Button(frameEightC, text = "Next question", command= OpenFrame9)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame8CButton.pack()
    frameEight.pack_forget()
    frameEightC.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame8D():
    BigLabel = Label(frameEightD, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameEightD, text="Prerogitive")
    OptionBLabel = Label(frameEightD, text="Perogative")
    OptionCLabel = Label(frameEightD, text="Perogitive")
    OptionDLabel = Label(frameEightD, text="Prerogative (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    Frame8DButton = Button(frameEightD, text = "Next question", command= OpenFrame9)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame8DButton.pack()
    frameEight.pack_forget()
    frameEightD.pack()

#This function works off of the same principles of "OpenFrame2" as described in the comments
def OpenFrame9():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameNine, text="")
    
    Frame9Label = Label(frameNine, text="Ninth Question Window")
    Question9 = Label(frameNine, text="Fill in the blank - The evidence collectively condemned one culprit,", font=5, fg='blue')
    Question99 = Label(frameNine, text=" ___ the sole witness’ claims contradicted the final verdict.", font=5, fg='blue')
    OptionA = Button(frameNine, text="A", command= OpenFrame9A, font=2)
    OptionALabel = Label(frameNine, text="Therefore")
    OptionB = Button(frameNine, text="B", command= OpenFrame9B, font=2)
    OptionBLabel = Label(frameNine, text="Moreover")
    OptionC = Button(frameNine, text="C", command=lambda: [ChangeScore(1), OpenFrame9C()], font=2)
    OptionCLabel = Label(frameNine, text="Adversely")
    OptionD = Button(frameNine, text="D", command= OpenFrame9D, font=2)
    OptionDLabel = Label(frameNine, text="Additionally")

    ScoreLabel.place(x=66,y=25)
    Frame9Label.pack()
    Space.pack()
    Question9.pack()
    Question99.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q9ImgLabel.pack()
    frameEightA.pack_forget()
    frameEightB.pack_forget()
    frameEightC.pack_forget()
    frameEightD.pack_forget()
    frameNine.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame9A():
    BigLabel = Label(frameNineA, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameNineA, text="Therefore (YOUR ANSWER)", fg='red')
    OptionBLabel = Label(frameNineA, text="Moreover")
    OptionCLabel = Label(frameNineA, text="Adversely (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameNineA, text="Additionally")
    Frame9AButton = Button(frameNineA, text = "Next question", command= OpenFrame10)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame9AButton.pack()
    frameNine.pack_forget()
    frameNineA.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame9B():
    BigLabel = Label(frameNineB, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameNineB, text="Therefore")
    OptionBLabel = Label(frameNineB, text="Moreover (YOUR ANSWER)", fg='red')
    OptionCLabel = Label(frameNineB, text="Adversely (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameNineB, text="Additionally")
    Frame9BButton = Button(frameNineB, text = "Next question", command= OpenFrame10)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame9BButton.pack()
    frameNine.pack_forget()
    frameNineB.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame9C():
    BigLabel = Label(frameNineC, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameNineC, text="Therefore")
    OptionBLabel = Label(frameNineC, text="Moreover")
    OptionCLabel = Label(frameNineC, text="Adversely (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameNineC, text="Additionally")
    Frame9CButton = Button(frameNineC, text = "Next question", command= OpenFrame10)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame9CButton.pack()
    frameNine.pack_forget()
    frameNineC.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame9D():
    BigLabel = Label(frameNineD, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameNineD, text="Therefore")
    OptionBLabel = Label(frameNineD, text="Moreover")
    OptionCLabel = Label(frameNineD, text="Adversely (CORRECT ANSWER)", fg='green')
    OptionDLabel = Label(frameNineD, text="Additionally (YOUR ANSWER)", fg='red')
    Frame9DButton = Button(frameNineD, text = "Next question", command= OpenFrame10)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame9DButton.pack()
    frameNine.pack_forget()
    frameNineD.pack()

#This function works off of the same principles of "OpenFrame2" as described in the comments
def OpenFrame10():
    ScoreLabel.config(text = str(PlayerScore), fg='purple', font=4)
    Space = Label(frameTen, text="")
    
    Frame10Label = Label(frameTen, text="Tenth Question Window")
    Question10 = Label(frameTen, text="Select the correct collective noun for the word - Lemurs", font=5, fg='blue')
    OptionA = Button(frameTen, text="A", command= OpenFrame10A, font=2)
    OptionALabel = Label(frameTen, text="Congress")
    OptionB = Button(frameTen, text="B", command=lambda: [ChangeScore(1), OpenFrame10B()], font=2)
    OptionBLabel = Label(frameTen, text="Conspiracy")
    OptionC = Button(frameTen, text="C", command= OpenFrame10C, font=2)
    OptionCLabel = Label(frameTen, text="Lounge")
    OptionD = Button(frameTen, text="D", command= OpenFrame10D, font=2)
    OptionDLabel = Label(frameTen, text="Pod")

    ScoreLabel.place(x=66,y=25)
    Frame10Label.pack()
    Space.pack()
    Question10.pack()
    Space.pack()
    OptionA.pack()
    OptionALabel.pack()
    OptionB.pack()
    OptionBLabel.pack()
    OptionC.pack()
    OptionCLabel.pack()
    OptionD.pack()
    OptionDLabel.pack()
    Q10ImgLabel.pack()
    frameNineA.pack_forget()
    frameNineB.pack_forget()
    frameNineC.pack_forget()
    frameNineD.pack_forget()
    frameTen.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame10A():
    BigLabel = Label(frameTenA, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameTenA, text="Congress (YOUR ANSWER)", fg='red')
    OptionBLabel = Label(frameTenA, text="Conspiracy (CORRECT ANSWER)", fg='green')
    OptionCLabel = Label(frameTenA, text="Lounge")
    OptionDLabel = Label(frameTenA, text="Pod")
    Frame10AButton = Button(frameTenA, text = "Next question", command= OpenFrameEnd)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame10AButton.pack()
    frameTen.pack_forget()
    frameTenA.pack()

#This function works off of the same principles of "OpenFrame1B" as described in the comments
def OpenFrame10B():
    BigLabel = Label(frameTenB, text="CORRECT", font=8, fg='green')

    OptionALabel = Label(frameTenB, text="Congress")
    OptionBLabel = Label(frameTenB, text="Conspiracy (YOUR ANSWER)(CORRECT ANSWER)", fg='green')
    OptionCLabel = Label(frameTenB, text="Lounge")
    OptionDLabel = Label(frameTenB, text="Pod")
    Frame10BButton = Button(frameTenB, text = "Next question", command= OpenFrameEnd)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame10BButton.pack()
    frameTen.pack_forget()
    frameTenB.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame10C():
    BigLabel = Label(frameTenC, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameTenC, text="Congress")
    OptionBLabel = Label(frameTenC, text="Conspiracy (CORRECT ANSWER)", fg='green')
    OptionCLabel = Label(frameTenC, text="Lounge (YOUR ANSWER)", fg='red')
    OptionDLabel = Label(frameTenC, text="Pod")
    Frame10CButton = Button(frameTenC, text = "Next question", command= OpenFrameEnd)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame10CButton.pack()
    frameTen.pack_forget()
    frameTenC.pack()

#This function works off of the same principles of "OpenFrame1A" as described in the comments
def OpenFrame10D():
    BigLabel = Label(frameTenD, text="INCORRECT", font=8, fg='red')

    OptionALabel = Label(frameTenD, text="Congress")
    OptionBLabel = Label(frameTenD, text="Conspiracy (CORRECT ANSWER)", fg='green')
    OptionCLabel = Label(frameTenD, text="Lounge")
    OptionDLabel = Label(frameTenD, text="Pod (YOUR ANSWER)", fg='red')
    Frame10DButton = Button(frameTenD, text = "Next question", command= OpenFrameEnd)
    
    BigLabel.pack()
    OptionALabel.pack()
    OptionBLabel.pack()
    OptionCLabel.pack()
    OptionDLabel.pack()
    Frame10DButton.pack()
    frameTen.pack_forget()
    frameTenD.pack()

#This is the ending/results page of the quiz, this is where all necessary information is provided and everything is tied together
#First PlayerScore and Counter are globalled to call them in for string usage and the necessary labels such as labels to put over the counter and score label are defined
    #The additional labels include the 'EndLabel's which tell the user that they have reached the end of the quiz, referring to their name, score and time taken to complete the quiz
#There is also a reflection to be directed to in order to display my usage of radiobuttons and for the user to give their opinion on the quiz
#The if/else statement essentially provides the user with a different image if they get a perfect score and a normal picture otherwise, along with packing all necessary components
def OpenFrameEnd():
    global PlayerScore
    global counter
    Space = Label(frameEnd, text="")
    Barricade = Label(master, text="===", fg='grey', bg='brown', font=11)
    Barricade.place(x=845, y=5)
    Barricade2 = Label(master, text="===========", fg='grey', bg='brown', font=99)
    Barricade2.place(x=1, y=1)
    Barricade3 = Label(master, text="===========", fg='grey', bg='brown', font=99)
    Barricade3.place(x=1, y=30)
    EndLabel = Label(frameEnd, text="This is the END of the quiz " + NameTextField.get(), font=6)
    EndLabel2 = Label(frameEnd, text="Your final score was " + str(PlayerScore) + "/10", font=6)
    EndLabel3 = Label(frameEnd, text="Your final time was " + str(counter) + " seconds", font=6)
    ReflectionLabel = Label(frameEnd, text="If you wish to give a rating of the quiz, please click the following button", font=4)
    ReflectionButton = Button(frameEnd, text="Reflection (evidence of RadioButton use)", command = OpenFrameQuiz1, font=4)
    if str(PlayerScore) == "10":
        EndLabel.pack()
        EndLabel2.pack()
        EndLabel3.pack()
        Space.pack()
        ReflectionLabel.pack()
        ReflectionButton.pack()
        End2ImgLabel.pack()
        frameTenA.pack_forget()
        frameTenB.pack_forget()
        frameTenC.pack_forget()
        frameTenD.pack_forget()
        frameEnd.pack()
    else:
        EndLabel.pack()
        EndLabel2.pack()
        EndLabel3.pack()
        Space.pack()
        ReflectionLabel.pack()
        ReflectionButton.pack()
        EndImgLabel.pack()
        frameTenA.pack_forget()
        frameTenB.pack_forget()
        frameTenC.pack_forget()
        frameTenD.pack_forget()
        frameEnd.pack()

#This is the first question variable for the radiobuttons in the reflection being established as a variable for use
q1Var = IntVar()

#SubmitClicked is a function that will change based on the answer you give in frameQuiz1
#A different response to your chosen rating of the quiz will determine the response given based on the radiobuttons and the value retrieved by them
def submitClicked():
    if str(q1Var.get()) == "5":
        responseLabel.config(text = "Thank you for the rating of " + str(q1Var.get()) + " out of 5, Yay! Perfect score! Woohoo!!")
    elif str(q1Var.get()) == "4":
        responseLabel.config(text = "Thank you for the rating of " + str(q1Var.get()) + " out of 5, I will make sure to improve next time")
    elif str(q1Var.get()) == "3":
        responseLabel.config(text = "Thank you for the rating of " + str(q1Var.get()) + " out of 5, I hope mediocre is good enough :P")
    elif str(q1Var.get()) == "2":
        responseLabel.config(text = "Thank you for the rating of " + str(q1Var.get()) + " out of 5, Are you kidding me? Less than 50%!")
    elif str(q1Var.get()) == "1":
        responseLabel.config(text = "Thank you for the rating of " + str(q1Var.get()) + " out of 5, Aww that's just mean ;(")
    
#OpenFrameQuiz1 is the first frame for the reflection part
#Here we simply incorporate a label and pack in the radiobuttons and submit buttons below (they have been given comments too)
def OpenFrameQuiz1():
    QuizLabel = Label(frameQuiz1, text="What would you rate this quiz out of five?", font=6)

    QuizLabel.pack()
    radioButton1.pack()
    radioButton2.pack()
    radioButton3.pack()
    radioButton4.pack()
    radioButton5.pack()
    submitButton.pack()
    frameEnd.pack_forget()
    frameQuiz1.pack()

#OpenFrameQuiz1 is the second frame for the reflection part and the final frame
#Also the responseLabel is used as configured in the 'SubmitClicked' function along with the defining and placement of a thank you label
def OpenFrameQuiz2():
    QuizLabel2 = Label(frameQuiz2, text="Thank you for your time, I hope you enjoyed the quiz :D", font=6)

    QuizLabel2.pack()
    responseLabel.pack()
    frameQuiz1.pack_forget()
    frameQuiz2.pack()
    


#mbox is a function defining a message box which shows the instructions, this function being used if a user answers the first frame incorrectly or is the welcome button is pressed
def mbox():
   messagebox.showinfo("-=-=-INSTRUCTIONS-=-=-", "This is an ENGLISH mutliple choice quiz at the year 10 level. You may begin the test once your Name and Grade Level are confirmed below. :D    (Please note that you can only advance from this window if your year level is confirmed to be 10 and if you have typed your name)")

#mboxYoung is a messagebox that pops up if your put your year level as year 9, telling you that you are younger than the intended audience and what the implications are of that
def mboxYoung():
   messagebox.showinfo("-=-=-INSTRUCTIONS-=-=-", "This ENGLISH multiple choice quiz is not suitable for your year level, however, you may advance regardless. Do note that the questions may be of great difficulty to you, but if not, fair enough. :D")

#mboxOld is a messagebox that pops up if your put your year level as year 11, telling you that you are older than the intended audience and what the implications are of that
def mboxOld():
   messagebox.showinfo("-=-=-INSTRUCTIONS-=-=-", "This ENGLISH multiple choice quiz is not suitable for your year level, however, you may advance regardless. Do note that the questions may be quite easy for you, but if not, fair enough. :D")


Space = Label(frameStart, text="")

#Top label is a label to display the score as Score label display the actual score as configured in the question frams above
TopLabel = Label(master, text="-==Score==-", fg='purple', font=3)
ScoreLabel = Label(master, text= str(PlayerScore), fg='purple', font=4)

#This Welcome label will redirect you to the instruction message box to help you understand the program
welcomeLabel = Button(frameStart, text="  Welcome  :D  ", command = mbox, font=10, bg='white', fg='#f00')

#This label instructs you on what to do on this frame
ExplainLabelStart = Label(frameStart, text="Welcome to the Year 10 level ENGLISH quiz, please enter your details then click 'Next Frame'.")

#The labels here correlate to their respective text field which will be referred to at the end frame and to determine whether you can progress further based on your year level
NameLabel = Label(frameStart, text="Please enter your name below")
NameTextField = Entry(frameStart)
YrLabel = Label(frameStart, text="Please enter your year level below (in numbers)")
YrTextField = Entry(frameStart)

#This button will take you to the first question frame
FirstWindow = Button(frameStart, text="Start Quiz", command= OpenFrame1)

#This is where we define the label that will begin the second counter in the quiz
label = Label(master, fg='purple')
start_counter(label)

#These next few lines of code define the images, including the ending images, images for each question and the starting image
#These image files are put into usable parts of code to implement into a label for the designated image then that image is packed
EnglishImg = PhotoImage(file="Eng.Img.png")
EnglishImgLabel = Label(frameStart, image= EnglishImg)

Q1Img = PhotoImage(file="Pics.Q1.png")
Q1ImgLabel = Label(frameOne, image= Q1Img)
Q2Img = PhotoImage(file="Pics.Q2.png")
Q2ImgLabel = Label(frameTwo, image= Q2Img)
Q3Img = PhotoImage(file="Pics.Q3.png")
Q3ImgLabel = Label(frameThree, image= Q3Img)
Q4Img = PhotoImage(file="Pics.Q4.png")
Q4ImgLabel = Label(frameFour, image= Q4Img)
Q5Img = PhotoImage(file="Pics.Q5.png")
Q5ImgLabel = Label(frameFive, image= Q5Img)
Q6Img = PhotoImage(file="Pics.Q6.png")
Q6ImgLabel = Label(frameSix, image= Q6Img)
Q7Img = PhotoImage(file="Pics.Q7.png")
Q7ImgLabel = Label(frameSeven, image= Q7Img)
Q8Img = PhotoImage(file="Pics.Q8.png")
Q8ImgLabel = Label(frameEight, image= Q8Img)
Q9Img = PhotoImage(file="Pics.Q9.png")
Q9ImgLabel = Label(frameNine, image= Q9Img)
Q10Img = PhotoImage(file="Pics.Q10.png")
Q10ImgLabel = Label(frameTen, image= Q10Img)

EndImg = PhotoImage(file="Pics.1.png")
EndImgLabel = Label(frameEnd, image= EndImg)
End2Img = PhotoImage(file="Pics.2.png")
End2ImgLabel = Label(frameEnd, image= End2Img)

#These are the radiobuttons used in the review part at the end of the quiz
#The radiobuttons are given a value and correlated with a vairable to indicate the response you get at the final frame of the quiz
radioButton1 = Radiobutton(frameQuiz1, variable = q1Var, text = "1", value = 1)
radioButton2 = Radiobutton(frameQuiz1, variable = q1Var, text = "2", value = 2)
radioButton3 = Radiobutton(frameQuiz1, variable = q1Var, text = "3", value = 3)
radioButton4 = Radiobutton(frameQuiz1, variable = q1Var, text = "4", value = 4)
radioButton5 = Radiobutton(frameQuiz1, variable = q1Var, text = "5", value = 5)

#The submit button allows you to submit your response and for the response to be processed to determine the response given at the end
submitButton = Button(frameQuiz1, text="Submit rating", command =lambda: [submitClicked(), OpenFrameQuiz2()], font=4)

#The response determined above will be shown in this response label
responseLabel = Label(frameQuiz2)

#Packed parts of frameStart
welcomeLabel.pack()
Space.pack()

ExplainLabelStart.pack()
NameLabel.pack()
NameTextField.pack()
YrLabel.pack()
YrTextField.pack()
FirstWindow.pack()
EnglishImgLabel.pack()


frameStart.pack()

#THE END :0
mainloop()
