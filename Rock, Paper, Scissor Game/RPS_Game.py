import random
from tkinter import *

rules = {
    "Rock": {"Rock": 1, "Paper": 0, "Scissor": 2},
    "Paper": {"Rock": 2, "Paper": 1, "Scissor": 0},
    "Scissor": {"Rock": 0, "Paper": 2, "Scissor": 1}
}
comp_score = 0
player_score = 0

def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcome = ['Rock', 'Paper', 'Scissor']
    random_number = random.randint(0,2)
    computer_choice = outcome[random_number]
    score = rules[user_choice][computer_choice]

    player_choice_label.config(fg='red', text='Player Choice: '+str(user_choice))
    computer_choice_label.config(fg='green', text='Computer Choice: '+str(computer_choice))

    if score == 2:
        player_score = player_score + 2
        player_score_label.config(text= 'Player: '+str(player_score))
        outcome_label.config(fg='blue', text= 'Outcome: Player Won')
    elif score == 1:
        player_score = player_score + 1
        comp_score = comp_score + 1
        player_score_label.config(text= 'Player: '+str(player_score))
        computer_score_label.config(text= 'Computer: '+str(comp_score))
        outcome_label.config(fg='blue', text= 'Outcome: Draw')
    elif score == 0:
        comp_score = comp_score + 2
        computer_score_label.config(text= 'Computer: '+str(comp_score))
        outcome_label.config(fg='blue', text= 'Outcome: Computer Won')

# Main Screen
master = Tk()
master.title('Rock, Paper, Scissor Game')

# Score, Choice, Outcome Labels
Label(master, text= 'Rock, Paper, Scissors', font=('Calibri',14)).grid(row=0,sticky=N,pady=10,padx=200)
Label(master, text= 'Please Select an Option', font=('Calibri',12)).grid(row=1,sticky=N)

player_score_label = Label(master, text= 'Player: 0', font=('Calibri',12))
player_score_label.grid(row=2,sticky=W)
computer_score_label = Label(master, text= 'Computer: 0', font=('Calibri',12))
computer_score_label.grid(row=2,sticky=E)

player_choice_label = Label(master, font=('Calibri',12))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label = Label(master, font=('Calibri',12))
computer_choice_label.grid(row=3,sticky=E)

outcome_label = Label(master, font=('Calibri',12))
outcome_label.grid(row=3,sticky=N)

# Buttons
Button(master, text='Rock', width=15, command=lambda:outcome_handler('Rock')).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text='Paper', width=15, command=lambda:outcome_handler('Paper')).grid(row=4, sticky=N, pady=5)
Button(master, text='Scissor', width=15, command=lambda:outcome_handler('Scissor')).grid(row=4, sticky=E, padx=5, pady=5)

Label(master).grid(row=5)

master.mainloop()