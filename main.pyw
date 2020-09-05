from tkinter import *

# Initial config

root = Tk()
frame = Frame(root, width=600, height=800, padx=20, pady=20)
frame.pack()

numbers_on_screen = StringVar()
numbers_on_screen.set("0 ")
numbers_on_back = StringVar()

expr = ""


# Get input and evaluate the expresion

def key_pressed(key):
    global expr
    try:
        if key in ["+", "-", "*", "/"] and expr[len(expr) - 2] in ["+", "-", "*", "/"]:
            if expr[len(expr) - 2] in ["+", "-", "*", "/"]:
                lexpr = list(expr)
                lexpr[len(expr) - 2] = key
                expr = "".join(lexpr)
                numbers_on_screen.set(expr.strip() + " ")
        else:
            if numbers_on_screen.get() == "0 ":
                numbers_on_screen.set(key)
                numbers_on_screen.set(numbers_on_screen.get() + " ")
                expr = key
                try:
                    numbers_on_back.set(eval(expr))
                    numbers_on_back.set(numbers_on_back.get().strip() + " ")
                except SyntaxError:
                    pass
            else:
                numbers_on_screen.set(numbers_on_screen.get().strip() + key + " ")
                expr = numbers_on_screen.get()
                try:
                    numbers_on_back.set(eval(expr))
                    numbers_on_back.set(numbers_on_back.get().strip() + " ")
                except SyntaxError:
                    pass
    except IndexError:
        pass


# Put in front screen the result of the current expresion

def equal():
    numbers_on_screen.set(numbers_on_back.get())
    numbers_on_back.set("")


# Clear the screen

def clear():
    numbers_on_screen.set("0 ")
    numbers_on_back.set("")


# Define Entry & position

entry_output = Entry(frame, font=('Consolas', 30), bd=0, disabledbackground="white",
                     justify="right", textvariable=numbers_on_back, state="disabled")
entry_output.grid(row=0, column=0, columnspan=4, ipady=10, sticky=N + S + W + E)

entry_input = Entry(frame, font=('Consolas', 30), bd=0, disabledbackground="white", disabledforeground="black",
                    justify="right", textvariable=numbers_on_screen, state="disabled")
entry_input.grid(row=1, column=0, columnspan=4, pady=(0, 10), sticky=N + S + W + E, ipady=10)
entry_input.insert(0, " ")

# Define buttons

button_0 = Button(frame, text="0", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("0"))
button_coma = Button(frame, text=".", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                     activebackground="#E0E0E0", command=lambda: key_pressed("."))

button_1 = Button(frame, text="1", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("1"))
button_2 = Button(frame, text="2", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("2"))
button_3 = Button(frame, text="3", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("3"))
button_equal = Button(frame, text="=", width=10, height=5, font=('Consolas', 15), bd=0, bg="#7BDFF2",
                      activebackground="#45D1ED", command=lambda: equal())

button_4 = Button(frame, text="4", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("4"))
button_5 = Button(frame, text="5", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("5"))
button_6 = Button(frame, text="6", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("6"))

button_7 = Button(frame, text="7", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("7"))
button_8 = Button(frame, text="8", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("8"))
button_9 = Button(frame, text="9", width=10, height=5, font=('Consolas', 15), bd=0, bg="white",
                  activebackground="#E0E0E0", command=lambda: key_pressed("9"))
button_plus = Button(frame, text="+", width=10, height=5, font=('Consolas', 15), bd=0, bg="#B2F7EF",
                     activebackground="#7EF1E4", command=lambda: key_pressed("+"))

button_clear = Button(frame, text="C", width=10, height=5, font=('Consolas', 15), bd=0, bg="#B2F7EF",
                      activebackground="#7EF1E4", command=lambda: clear())
button_div = Button(frame, text="/", width=10, height=5, font=('Consolas', 15), bd=0, bg="#B2F7EF",
                    activebackground="#7EF1E4", command=lambda: key_pressed("/"))
button_mul = Button(frame, text="*", width=10, height=5, font=('Consolas', 15), bd=0, bg="#B2F7EF",
                    activebackground="#7EF1E4", command=lambda: key_pressed("*"))
button_sub = Button(frame, text="-", width=10, height=5, font=('Consolas', 15), bd=0, bg="#B2F7EF",
                    activebackground="#7EF1E4", command=lambda: key_pressed("-"))

# Define buttons position

button_0.grid(row=6, column=0, columnspan=2, sticky=N + S + W + E, padx=2, pady=2)
button_coma.grid(row=6, column=2, sticky=N + S + W + E, padx=2, pady=2)

button_1.grid(row=5, column=0, sticky=W + E, padx=2, pady=2)
button_2.grid(row=5, column=1, sticky=W + E, padx=2, pady=2)
button_3.grid(row=5, column=2, sticky=W + E, padx=2, pady=2)
button_equal.grid(row=5, column=3, rowspan=2, sticky=N + S + W + E, padx=2, pady=2)

button_4.grid(row=4, column=0, sticky=W + E, padx=2, pady=2)
button_5.grid(row=4, column=1, sticky=W + E, padx=2, pady=2)
button_6.grid(row=4, column=2, sticky=W + E, padx=2, pady=2)

button_7.grid(row=3, column=0, sticky=W + E, padx=2, pady=2)
button_8.grid(row=3, column=1, sticky=W + E, padx=2, pady=2)
button_9.grid(row=3, column=2, sticky=W + E, padx=2, pady=2)
button_plus.grid(row=3, column=3, rowspan=2, sticky=N + S + W + E, padx=2, pady=2)

button_clear.grid(row=2, column=0, sticky=W + E, padx=2, pady=2)
button_div.grid(row=2, column=1, sticky=W + E, padx=2, pady=2)
button_mul.grid(row=2, column=2, sticky=W + E, padx=2, pady=2)
button_sub.grid(row=2, column=3, sticky=W + E, padx=2, pady=2)

root.mainloop()
