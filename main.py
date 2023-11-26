from tkinter import *
import random

def next_turn(row,column):
    global player

    #Check winner to deactivate button when the winner has been announced
    if buttons[row][column]['text'] == "" and check_winner() is False:
        

        if player == players[0]:
            
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1] #switch player
                label.config(text=(players[1] + " turn"))
            
            elif check_winner() is True:
                label.config(text=player[0] + " wins!")
            
            elif check_winner() == "tie":
                label.config(text="tie!")
        
        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0] #switch player
                label.config(text=(players[0] + " turn"))
            
            elif check_winner() is True:
                label.config(text=players[1] + " wins!")
            
            elif check_winner() == "tie":
                label.config(text="tie!")


def check_winner():
    
    #Horizontal win
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
    
    #Vertical win
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True
        
    #R-L Diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    #R-L Diagonal
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    elif empty_space() is True:
        return "tie"

    else:
        return False


def empty_space():
    empty_count = 0

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                empty_count += 1
    
    if empty_count <= 0:
        return True
    else:
        return False

def new_game():
    
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""

    player = random.choice(players)
    label.config(text=player + " turn")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
          [0,0,0],
          [0,0,0]]

label = Label(text= player + " turn",font=('consolas',50))
label.pack(side="top")

reset_btt = Button(text="restart",font=('consolas',30), command=new_game)
reset_btt.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame,text="",font=('consolas',30),width=5,height=2,
                                      command= lambda row=row,column=column, : next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
                
window.mainloop()
