# GUI CALCULATOR

from tkinter import *


def equation(input):

    global eqn_text
    eqn_text += input
    eqn_label.set(eqn_text)


def calculate():

    global eqn_text

    try:
        eqn_label.set(eval(eqn_text))

    except SyntaxError:
        eqn_label.set("ERROR")
        eqn_text = ""
    
    except ZeroDivisionError:
        eqn_label.set("ERROR")
        eqn_text = ""


def backspace():

    global eqn_text
    l, s = [], ''

    if len(eqn_text) > 0:

        for ch in eqn_text[::-1]:
            l.append(ch)

        l.remove(l[0])

        for ch in l:
            s += ch

        eqn_text = s[::-1]
        eqn_label.set(eqn_text)


def clear():

    global eqn_text
    eqn_text = ""
    eqn_label.set(eqn_text)


window = Tk()


window.geometry("420x520")
window.title("Calculator")

eqn_text = ""

eqn_label = StringVar()

screen = Label(window, textvariable=eqn_label, font=('Ariel', 25, 'bold'), bg="green", fg="black", padx=20, pady=10, bd=10, relief=SUNKEN, width=17, height=2)
screen.pack()

frame = Frame(window)
frame.pack()

button7 = Button(frame, text='7', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('7'))
button7.grid(row=0, column=0)

button8 = Button(frame, text='8', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('8'))
button8.grid(row=0, column=1)

button9 = Button(frame, text='9', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('9'))
button9.grid(row=0, column=2)

button4 = Button(frame, text='4', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('4'))
button4.grid(row=1, column=0)

button5 = Button(frame, text='5', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('5'))
button5.grid(row=1, column=1)

button6 = Button(frame, text='6', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('6'))
button6.grid(row=1, column=2)

button1 = Button(frame, text='1', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('1'))
button1.grid(row=2, column=0)

button2 = Button(frame, text='2', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('2'))
button2.grid(row=2, column=1)

button3 = Button(frame, text='3', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('3'))
button3.grid(row=2, column=2)

button0 = Button(frame, text='0', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('0'))
button0.grid(row=3, column=0)

button_fs = Button(frame, text='.', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('.'))
button_fs.grid(row=3, column=1)

button_mod = Button(frame, text='%', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('%'))
button_mod.grid(row=3, column=2)

button_div = Button(frame, text='/', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('/'))
button_div.grid(row=3, column=3)

button_multiply = Button(frame, text='*', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('*'))
button_multiply.grid(row=0, column=3)

button_minus = Button(frame, text='-', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('-'))
button_minus.grid(row=1, column=3)

button_plus = Button(frame, text='+', height='2', width='8', font=35, bg='black', fg='white', command=lambda: equation('+'))
button_plus.grid(row=2, column=3)

button_enter = Button(frame, text='(', height='2', width='17', font=35, bg='black', fg='white', command=lambda: equation('('))
button_enter.grid(row=4, column=0, columnspan=2)

button_enter = Button(frame, text=')', height='2', width='17', font=35, bg='black', fg='white', command=lambda: equation(')'))
button_enter.grid(row=4, column=2, columnspan=2)

button_clr = Button(frame, text='CLR', height='2', width='8', font=35, bg='black', fg='white', command=lambda: clear())
button_clr.grid(row=5, column=0)

button_back = Button(frame, text='BACK', height='2', width='8', font=35, bg='black', fg='white', command=lambda: backspace())
button_back.grid(row=5, column=1)

button_enter = Button(frame, text='ENTER', height='2', width='17', font=35, bg='black', fg='white', command=lambda: calculate())
button_enter.grid(row=5, column=2, columnspan=2)

window.mainloop()
