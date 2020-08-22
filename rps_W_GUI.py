import random
import tkinter as tk
import sys

window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""
game_Count = 0


# Converting choices to the number it represents
def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps[choice]


# Converting the number tot he choice it represents
def number_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return rps[number]


# Func. For comp choice
def random_comp_choice():
    return random.choice(['rock', 'paper', 'scissor'])


# The Resuls ebign calculated and determining a winner plus updating score
def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    global game_Count
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if COMP_SCORE + USER_SCORE + game_Count >= 10:
        sys.exit()

    if user == comp:
        print("Tie! ")
        game_Count += 1

    elif (user - comp) % 3 == 1:
        print("You win!")
        USER_SCORE += 1

    else:
        print("Comp wins")
        COMP_SCORE += 1

    text_area = tk.Text(master=window, height=12, width=30, bg="#FFFF99")
    text_area.grid(column=0, row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your score : {u} \n Computer Score : {c} ".format(
        uc=USER_CHOICE, cc=COMP_CHOICE, u=USER_SCORE, c=COMP_SCORE)
    text_area.insert(tk.END, answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    global game_Count
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_comp_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    global game_Count
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_comp_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    global game_Count
    USER_CHOICE = 'scissor'
    COMP_CHOICE = random_comp_choice()
    result(USER_CHOICE, COMP_CHOICE)


button1 = tk.Button(text="       Rock       ", bg="skyblue", command=rock)
button1.grid(column=0, row=1)
button2 = tk.Button(text="       Paper      ", bg="pink", command=paper)
button2.grid(column=0, row=2)
button3 = tk.Button(text="      Scissor     ", bg="lightgreen", command=scissor)
button3.grid(column=0, row=3)

window.mainloop()
