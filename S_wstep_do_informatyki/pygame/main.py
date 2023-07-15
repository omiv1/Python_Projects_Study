import random
from tkinter import  *
t = Tk()
t.title("przycisk")
t.geometry("300x350")
def wstaw_p():
    ile = 8
    global przycisk
    przycisk = []
    dobry = random.randint(0,ile -1)
    for i in range(ile):
        if i == dobry:
            przyciski.append()
