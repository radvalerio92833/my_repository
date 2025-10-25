from tkinter import *
import random


BLACK = "#000000"
GREEN = "#00e600"
FONT_NAME = "Arial"
sentences = open('sentences.txt', 'r').read().split('\n')
seconds, accuracy, wpm,  = 0, 0, 0
avg_accuracy = 0
words_typed = 0
start_timer = 3
stage = 0
user_input = ""
chosen_sentence=""
accuracy_list = []
doTick = True

def stop():
    global doTick
    doTick = False

def start():
    global doTick
    doTick = True
def countdown(count):
    global doTick, stage
    if not doTick:
        return
    if count > 0:
        canvas.itemconfig(subtitle_text, text=f"{count}")
        tk.after(1000, countdown, count - 1)
    else:
        stage += 1
        if stage == 1:
            stop()
            begin_test()
        elif stage == 2:
            stop()
            display_result()
            stage = 0








def calculate():
    global accuracy_list, words_typed, seconds, wpm, avg_accuracy
    wpm = (words_typed / 5) / (seconds / 60)
    avg_accuracy = sum(accuracy_list)/len(accuracy_list)

def display_result():
    check()
    calculate()
    canvas.itemconfig(title_text, text="Test finished! Here are the results:", font=(FONT_NAME, 20, "normal"))
    canvas.itemconfig(subtitle_text, text="Words typed per minute: {:.2f}\n"
                                          "Accuracy: {:.2f}".format(wpm, avg_accuracy))
    return_button.grid(row=1, column=1)
    input_text.delete(1.0, END)
    input_text.grid_remove()



def next(event=None):
    global sentences, chosen_sentence
    check()
    chosen_sentence = random.choice(sentences)
    canvas.itemconfig(title_text, text=f"{chosen_sentence}", font=(FONT_NAME, 11, "normal"))

def check():
    global user_input, chosen_sentence, accuracy, words_typed, accuracy_list
    user_input = input_text.get("1.0", "end-1c")
    user_input_list = user_input.strip("\n").split(" ")
    chosen_sentence = chosen_sentence.split(" ")
    if len(user_input_list) < len(chosen_sentence):
        difference = len(chosen_sentence) - len(user_input_list)
        for i in range(difference):
            user_input_list.append(" ")
    if len(user_input_list) > len(chosen_sentence):
        user_input_list = user_input_list[:len(chosen_sentence)]
    for i in range(len(user_input_list)):
        if user_input_list[i] == chosen_sentence[i]:
            accuracy += 1
        if user_input_list[i] != " ":
            words_typed += 1
    accuracy_list.append((accuracy / len(chosen_sentence)) * 100)







def initiate(mode):
    global seconds, start_timer
    if mode == "1":
        seconds = 30

    elif mode == "2":
        seconds = 60
    else:
        seconds = 90
    thirty_sec_button.grid_remove()
    ninety_sec_button.grid_remove()
    sixty_sec_button.grid_remove()
    canvas.itemconfig(title_text, text="The test will begin in:")
    start()
    countdown(start_timer)






def begin_test():
    global chosen_sentence, seconds
    start()
    countdown(seconds)
    chosen_sentence = random.choice(sentences)
    canvas.itemconfig(title_text, text=f"{chosen_sentence}", font=(FONT_NAME, 11, "normal"))
    input_text.grid(row=1, column=1)
    tk.bind("<Return>", next)



def reset():
    global seconds, wpm, accuracy, avg_accuracy, words_typed, start_timer, user_input, accuracy_list
    seconds, accuracy, wpm = 0, 0, 0
    avg_accuracy = 0
    words_typed = 0
    start_timer = 3
    user_input = ""
    accuracy_list = []
    thirty_sec_button.grid(row=1, column=0)
    sixty_sec_button.grid(row=1, column=1)
    ninety_sec_button.grid(row=1, column=2)
    return_button.grid_remove()
    canvas.itemconfig(title_text, text="Welcome to the Typing Speed Test!")
    canvas.itemconfig(subtitle_text, text="Choose a timer to start")



tk = Tk()
tk.title("Typing speed test")
tk.config(padx=150, pady=150, bg=BLACK)
canvas = Canvas(width=550, height=300, bg=BLACK, highlightthickness=0, borderwidth=20,)
title_text = canvas.create_text(280, 125,text="Welcome to the Typing Speed Test!", font=(FONT_NAME, 25, "normal"), fill=GREEN)
subtitle_text = canvas.create_text(280, 200 ,text="Choose a timer to start", font=(FONT_NAME, 20, "normal"), fill=GREEN)
canvas.grid(row=0, column=1)

thirty_sec_button = Button(text="30 sec",  font=(FONT_NAME, 25, "normal"), bg=BLACK, fg=GREEN, command= lambda: initiate("1"))
sixty_sec_button = Button(text="60 sec",  font=(FONT_NAME, 25, "normal"), bg=BLACK, fg=GREEN, command= lambda: initiate("2"))
ninety_sec_button = Button(text="90 sec",  font=(FONT_NAME, 25, "normal"), bg=BLACK, fg=GREEN, command= lambda: initiate("3"))
thirty_sec_button.grid(row=1, column=0)
sixty_sec_button.grid(row=1, column=1)
ninety_sec_button.grid(row=1, column=2)

input_text = Text(height=7, width=60, bg=BLACK, fg=GREEN, )
return_button = Button(text="Return",  font=(FONT_NAME, 25, "normal"), bg=BLACK, fg=GREEN, command=reset)

tk.mainloop()