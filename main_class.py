from tkinter import *
import time
import Data
import random
from threading import Thread

text = random.choice(Data.var)
print(text)

background_color = "#135D66"
timer_color = "#E3FEF7"


def return_word():
    time.sleep(1)
    word = random.choice(Data.var)
    return word


def new_fun():
    print("hello")


def start_timer():
    num = int(59)
    while True:

        time.sleep(1)
        if num >= 10:
            canvas.update()
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
            break


def do_two_fun():
    p1 = Thread(target=start_timer)
    p2 = Thread(target=return_word)
    p1.start()
    p2.start()


window = Tk()
window.title('Type Test')
window.config(width=500, height=500, bg=background_color)
window.minsize(500, 500)
window.maxsize(500, 500)
canvas = Canvas(window, width=300, height=300, bg=background_color, highlightthickness=0)
show_time = canvas.create_text(155, 70, text="00:00", fill="black", font="Arial 30 bold")
show_text = canvas.create_text(155, 150, text="Text", fill="black", font=("Arial", 30))
entry = Entry(window, width=20, font=("Courier", 20))
button = Button(window, text="Start", command=do_two_fun, width=5, font=("Courier", 14))
button.place(x=380, y=250)
entry.place(x=30, y=250)
canvas.pack()

window.mainloop()
