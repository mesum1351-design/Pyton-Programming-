import tkinter as tk

windows = tk.Tk()
windows.title("PAI LAB")
windows.geometry("500x500")
windows.mainloop()

root = tk.Tk()
root.title("PAI LAB")
root.geometry("500x500")
text = tk.Label(root, text = "HELLO WELCOME TO MY PAGE ")
text.grid(row = 10, column = 1000)

text.pack()
root.mainloop()

#Button
#The Button widget is used to display the buttons in your application.

root = tk.Tk()
root.title("PAI LAB")
root.geometry("500x500")
def display():
    print("HELLO WORLD")

my_button = tk.Button(root, text = "Click Me", command = display)



# .pack() — Blocks: Stacks widgets one after another (top-to-bottom, or side="left" / "bottom")
#.grid() — Table: Places widgets in rows and columns (row=0, column=1) like a matrix
#.place() — Coordinates: Places widgets at exact (x, y) pixel positions (x=50, y=50).
my_button.pack()
my_button.grid(row = 2, column = 2)
my_button.place(x = 200, y = 200)
root.mainloop()



