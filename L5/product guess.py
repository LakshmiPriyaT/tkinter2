import tkinter
import math
import tkinter.messagebox
import random

root = tkinter.Tk()
root.minsize(350, 260)
root.title('Guess the product of two number game')

number1 = random.randint(1, 20)
number2 = random.randint(1, 20)

def say_hello():
    print('hello,world!')


def send_low():
    tkinter.messagebox.showinfo("messagebox", "Your guess is too low.")


def check_num():
    guess = text_guess1.get()
    guess = int(guess)
    if guess > number1*number2:
        tkinter.messagebox.showinfo("high", "Your guess is too high.")
    if guess < number1*number2:
        tkinter.messagebox.showinfo("low", "Your guess is too low.")
    if guess == number1*number2:
        tkinter.messagebox.showinfo("good", "Good job!")
        root.destroy()


def btn_confirm():
    myName = text_name.get()
    tkinter.messagebox.showinfo("name", 'Well,' + myName + ',I am thinking of the product of '+str(number1)+"*"+str(number2))


# name
label = tkinter.Label(root, text="Welcome to our game!")
label.pack()
label_name = tkinter.Label(root, text="What's your name?")
label_name.place(x=10, y=60)
text_name = tkinter.Entry(root, width=20)
text_name.place(x=10, y=90)

btnOK = tkinter.Button(root, text="OK", command=btn_confirm)
btnOK.place(x=200, y=90, height=28)

# input
instruction_label = tkinter.Label(root, text="Guess the product of these numbers")
instruction_label.place(x= 10, y= 150)
label_guess = tkinter.Label(root, text='Take a guess:')
label_guess.place(x=10, y=180)
text_guess1 = tkinter.Entry(root, width=10)
text_guess1.place(x=120, y=180)
btnCheck = tkinter.Button(root, text='Guess', command=check_num)
btnCheck.place(x=250, y=180, width=45, height=28)

root.mainloop()