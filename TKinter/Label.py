import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Label")
my_label = tk.Label(root, text = "WELCOME")
my_label.pack()
root.mainloop()
