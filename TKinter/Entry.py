import tkinter as tk

window = tk.Tk()
window.title("Entry")
window.geometry("500x500")

tk.Label(window, text="Username").grid(row=0, column=0)
tk.Entry(window).grid(row=0, column=1)

tk.Label(window, text="Password").grid(row=1, column=0)
tk.Entry(window).grid(row=1, column=1)


window.mainloop()
