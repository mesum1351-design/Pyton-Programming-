import tkinter
import tkinter as tk

window = tkinter.Tk()
window.title("Message")
window.geometry("400x300")

tk.Label(window, text = "Write Message").grid(row=0, column=0)
tk.Text(window, height = 5, width = 20).grid(row=1, column=0)

window.mainloop()
