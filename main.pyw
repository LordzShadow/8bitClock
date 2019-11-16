import time
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Digital Clock")
window.wm_attributes("-transparentcolor", "white")
window.config(bg="white")
window.overrideredirect(True)

w = 700
h = 300
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
x = ws - w
y = hs - h
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

canvas = Canvas(window, width=w+20, height=h+20, bg="white")
canvas.config(bg="white")
canvas.place(relx=0, rely=0, x=-2, y=-2)
# üks number 80px lai, 140 px kõrge?
nr_w = 80
nr_h = 140
algus = 5
alg_y = 60
vahe = 35
numbrid = ["1111110", "0110000", "1101101", "1111001", "0110011", "1011011", "1011111", "111000", "1111111", "1111011"]
y_asukoht = [alg_y, alg_y+5, alg_y+nr_h/2+5, alg_y+nr_h, alg_y+nr_h/2+5, alg_y+5, alg_y+nr_h/2]
y_asukoht_lopp = [alg_y, alg_y+nr_h/2-5, alg_y+nr_h-5, alg_y+nr_h, alg_y+nr_h-5, alg_y+nr_h/2-5, alg_y+nr_h/2]
white = "white"
orange = "orange"
def joonista(nr, x, y):
    x_asukoht = [x+5, x + nr_w, x + nr_w, x+5, x, x, x+5]
    x_asukoht_lopp = [x+nr_w-5, x+nr_w, x+nr_w, x+nr_w-5, x, x, x+nr_w-5]
    for bit in range(len(numbrid[nr])):
        if numbrid[nr][bit] == "0":
            pass
        else:
            canvas.create_line(x_asukoht[bit], y_asukoht[bit], x_asukoht_lopp[bit], y_asukoht_lopp[bit], fill="orange", width=3)

def check():
    canvas.delete("all")
    aeg = time.localtime()
    hour, minute, second = "{:02d}".format(aeg.tm_hour), "{:02d}".format(aeg.tm_min), "{:02d}".format(aeg.tm_sec)
    joonista(int(hour[0]), algus, alg_y)
    joonista(int(hour[1]), algus+nr_w+vahe, alg_y)
    joonista(int(minute[0]), algus + 2*(nr_w+vahe)+vahe/4, alg_y)
    joonista(int(minute[1]), algus + 3*(nr_w+vahe)+vahe/4, alg_y)
    joonista(int(second[0]), algus + 4*(nr_w+vahe)+vahe/2, alg_y)
    joonista(int(second[1]), algus + 5*(nr_w+vahe)+vahe/2, alg_y)

    window.after(1000, check)
check()
window.mainloop()
