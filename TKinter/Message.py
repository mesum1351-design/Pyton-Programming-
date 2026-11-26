import tkinter
import tkinter as tk

window = tkinter.Tk()
window.title("Message")
window.geometry("700x700")

#Text: Used to display or accept text in multiple lines
tk.Message(window, text="Paragraphs, instructions,"
                        " or multi-line static messages on screen.").grid(row=0, column=0)
tk.Label(window, text = "Write Message" ).grid(row=5, column=0)
tk.Text(window, height = 10, width = 40).grid(row=6, column=0)

window.mainloop()
