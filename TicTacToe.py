#from sklearn import tree
#import numpy as np
import pygame
#import time
import random
from os import system
from tkinter import *
pygame.init()
click_sound=pygame.mixer.Sound("Click-Sound.wav")
click_sound2=pygame.mixer.Sound("Click-Sound2.wav")
win_sound=pygame.mixer.Sound("win_sound.wav")
computer = " SARA "
winning_patterns = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
tricks = [[1, 2], [7, 9], [8,  9],[4, 5]]
labels = [3,8,7,6]
entries=[2,2,2,2,2,2,2,2,2]
name = ""
score1=0
score2=0
players = [["",'',score1],["",'',score2]]
i = 0
tie = 0
class Warspyking(Frame):
    '''A button that has it's width and height set in pixels'''
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master)
        self.rowconfigure(0, minsize=kwargs.pop('height', None))
        self.columnconfigure(0, minsize=kwargs.pop('width', None))
        self.btn = Button(self, **kwargs)
        self.btn.grid(row=0, column=0, sticky="nsew")
        self.config = self.btn.config

        
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(tricks, labels)
#i= input("please enter your first turn")
#j= input(" enter your 2nd turn")
#print (clf.predict([[i,j]]))
def change(name):
    if name == 1:
        return 0
    else:
        return 1
def start_again(playe,win_label):
    global entries,winner,a,tie
    tie = 0
    start_button=Button(window,text="START AGAIN",width=12,height=4,bg="orange",fg="black",command=lambda:game_window(start_button,win_label))
    start_button.place(x=930,y=500)
    entries=[2,2,2,2,2,2,2,2,2]
    winner=playe       ##here "meine means 'i' "  assign the winner means first turn to player who win .
    a=playe

def tie_window():
    tie_label=Label(window,text="MATCH TIES",font="none 34 bold")
    tie_label.place(x=840,y=340)
    start_again(winner,tie_label)
    
def winner_window(playe):
    global win_sound,players
    win_sound.play()
    players[playe][2]=players[playe][2]+1 ## incresing score of match winner player  
    win_label=Label(window,text=players[playe][0]+" wins the game",font="none 34 bold")
    win_label.place(x=840,y=340)
    score1 = Label(window, text = "player "+players[0][0] +"  "+ str(players[0][2]), bg = "black" ,fg ="white" , font = "none 20 bold")
    score1.place(x = 850 , y = 100)
    score2 = Label(window, text = "player "+players[1][0] + "  " +str(players[1][2]), bg = "black" ,fg ="white" , font = "none 20 bold")
    score2.place(x = 850 , y = 150)
    start_again(playe,win_label)

def check(side_label):
    global entries,winning_patterns,tie
    for winning_pattern in winning_patterns:
        if entries[winning_pattern[0]]==entries[winning_pattern[1]]and entries[winning_pattern[1]] == entries[winning_pattern[2]]and entries[winning_pattern[0]]==0:
            side_label.destroy()
            winner_window(0)
        elif entries[winning_pattern[0]]==entries[winning_pattern[1]]and entries[winning_pattern[1]] == entries[winning_pattern[2]]and entries[winning_pattern[0]]==1:
            side_label.destroy()
            winner_window(1)
        else:
            if tie==10:
                side_label.destroy()
                tie_window()

def turns(button,side_label,ent):
    global players, winner,a,entries,tie
    if entries[ent-1] == change(a):
        try:
            pass
        except:
            print("error")
    else:
        tie += 1
        button.config(text=players[a][1],font="none 50 bold")
        entries[ent-1]=a
        a=change(a)
        side_label.config(text=players[a][0]+"  turn")
        check(side_label)
        print(entries[ent-1])

def game_window(button,label):
    button.destroy()
    label.destroy()
    global winner, players,a
    def click(button):
        global click_sound2
        click_sound2.play()
        buttons = { 1 : button1,
                    2 : button2,
                    3 : button3,
                    4 : button4,
                    5 : button5,
                    6 : button6,
                    7 : button7,
                    8 : button8,
                    9 : button9}
        turns(buttons[button],side_label,button)
    button1 = Warspyking(window, text ="1", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(1))
    button1.place(x=150,y=68)
    button2 = Warspyking(window, text ="2", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(2))
    button2.place(x=380,y=68)
    button3 = Warspyking(window, text ="3", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(3))
    button3.place(x=610,y=68)
    button4 = Warspyking(window, text ="4", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(4))
    button4.place(x=150,y=254)
    button5 = Warspyking(window, text ="5", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(5))
    button5.place(x=380,y=254)
    button6 = Warspyking(window, text ="6", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(6))
    button6.place(x=610,y=254)
    button7 = Warspyking(window, text ="7", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(7))
    button7.place(x=150,y=440)
    button8 = Warspyking(window, text ="8", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(8))
    button8.place(x=380,y=440)
    button9 = Warspyking(window, text ="9", width=150,height=150,bg = "black",fg = "blue",command=lambda:click(9))
    button9.place(x=610,y=440)
    side_label = Label(window, text = players[winner][0]+"  turn",bg="black",fg="white",font="none 34 bold")
    side_label.place(x=840,y=320)
    
def toss_window():
    global players,winner
    def choose(winner):
        global click_sound
        def x_choose(winner):
            click_sound.play()
            players[winner][1] = "X"
            players[change(winner)][1]="O"
            o_button.destroy()
            symbol_choose.destroy()
            game_window(winner_label,x_button)
        def o_choose(winner):
            click_sound.play()
            players[winner][1] = "O"
            players[change(winner)][1]="X"
            o_button.destroy()
            symbol_choose.destroy()
            game_window(winner_label,x_button)
            
        global players
        symbol_choose = Label(window, text = "what you want to choose ",font="none 35 bold",bg="black",fg = "red")
        symbol_choose.place(x=460,y=300)
        x_button = Button(window,text = "X",width=8,height=5,bg="blue",command=lambda:x_choose(winner))
        x_button.place(x=500,y=400)
        o_button = Button(window,text = "O",width=8,height=5,bg="yellow",command=lambda:o_choose(winner))
        o_button.place(x=600,y=400)
        winner_label = Label(window, text ="player " + players[winner][0] + " wins the toss",bg = "black",fg ="blue",font = "none 35 bold")    
        winner_label.place(x=460,y=10)
        
    def toss(players):
        global click_sound
        click_sound.play()
        global winner,a
        toss_button.destroy()
        num = random.randint(0, 1)
        if num==1:
            winner=1
            a=1
            choose(winner)
        else:
            winner=0
            a=0
            choose(winner)
    toss_button = Button(window, text = "TOSS",width = 7,height = 4, bg = "red", fg = "black",font = "none 20 bold",command=lambda:toss(players))
    toss_button.place(x = 600, y = 600)
    
def enter_name():
    global click_sound
    click_sound.play()
    global players
    global computer
    players[0][0] = textentry.get()
    players[1][0] = textentry2.get()
    text.destroy()
    ph.destroy()
    textentry.destroy()
    textentry2.destroy()
    button.destroy()
    print(players[0][0])
    print(players[1][0])
    toss_window()

def exiting():
    global click_sound
    def ok():
        exit_window.destroy()
        click_sound.play()
        window.destroy()
    def quiti():
        click_sound.play()
        exit_window.destroy()
    exit_window = Tk()
    exit_window.geometry("250x150+683+384")
    exit_window.configure(background = "black")
    exit_window.title("Exit Window")
    text = Label(exit_window,text = "Are you sure to exit",bg = "black",fg = "white",font = "none 12 bold")
    text.place(x = 30, y = 50)
    ok_button = Button(exit_window,text = "OK", width = 5, command = ok).place(x = 30, y = 70)
    cancel_button = Button(exit_window, text = "CANCEL", width = 6 , command = quiti).place(x = 100, y = 70)
    
window = Tk()
window.title("TIC TAC TOE GAME with MACHINE LEARNING")
window.geometry("1366x768")
window.configure(background = "black")
photo = PhotoImage(file = "Look-into-my-eyes.gif")
ph = Label(window, image = photo, bg = "black")
ph.grid(row = 0, column = 0)
text = Label(window, text = "enter your name", bg = "black" ,fg ="white" , font = "none 20 bold")
text.place(x = 600 , y = 600)
textentry = Entry(window, width = 18 , bg = "white",font = "none 20 bold")
textentry.place(x = 600 , y = 410)
textentry2 = Entry(window, width = 18 , bg = "white",font = "none 20 bold")
textentry2.place(x = 600 , y = 510)
button = Button(window, text = "SUBMIT", width = 6,command = enter_name)
button.place(x = 600, y = 550)
exit_button = Button(window, text = "EXIT", width = 5,command = exiting)
exit_button.place(x=0 , y = 0)
window.mainloop()


