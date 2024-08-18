from tkinter import *
import time
import Data
import random
from threading import Thread
from tkinter import messagebox

flag = bool(True)

text = random.choice(Data.var)
print(text)

background_color = "#135D66"
timer_color = "#E3FEF7"


def func(event):
    return event.char


def return_word():
    entry.delete(0, END)
    if entry.get() == "":
        list_entry_word = []
        list_my_entry_word = []
        first_word = random.choice(Data.var)
        list_entry_word.append(first_word)
        canvas.itemconfig(show_text, text=first_word)
        canvas.update()
        global flag
        time.sleep(.5)
        while flag:
            time.sleep(1.7)
            word = str(entry.get())
            size = len(word)
            list_word = list(word)
            if list_word[size - 1] == ' ':
                random_word = random.choice(Data.var)
                list_entry_word.append(random_word)
                canvas.itemconfig(show_text, text=random_word)
                canvas.update()
        entry_word=entry.get()
        list_my_entry_word=entry_word.split()
        print(list_entry_word)
        print(list_my_entry_word)
        num = int(0)
        for i in list_my_entry_word:
            for j in range(len(list_entry_word)):
                if i == list_entry_word[j]:
                    num = num + 1
        print(num)
        messagebox.showinfo(title="Result Test",message=f"Done\nYour speed is {num} words per minute")

def start_timer():
    num = int(59)
    while True:

        time.sleep(1)
        if num >= 10:

            second = num
        else:
            canvas.update()
            second = str("0" + str(num))

        canvas.itemconfig(show_time, text=f"00:{second}")

        canvas.update()
        num = num - 1
        if num < 0:
            canvas.itemconfig(show_time, text=f"00:00")
            canvas.update()
            global flag
            flag = bool(False)

            break


def do_two_function():
    p1 = Thread(target=start_timer)
    p2 = Thread(target=return_word)
    p2.start()
    p1.start()


window = Tk()
window.title('Type Test')
window.config(width=500, height=500, bg=background_color)
window.minsize(500, 500)
window.maxsize(500, 500)
canvas = Canvas(window, width=300, height=300, bg=background_color, highlightthickness=0)
show_time = canvas.create_text(155, 70, text="00:00", fill="black", font="Arial 30 bold")


show_text = canvas.create_text(155, 150, text="Text", fill="black", font=("Arial", 30))
entry = Entry(window, width=20, font=("Courier", 20))
button = Button(window, text="Start", command=do_two_function, width=5, font=("Courier", 14))
button.place(x=380, y=250)
entry.place(x=30, y=250)
canvas.pack()

window.mainloop()
