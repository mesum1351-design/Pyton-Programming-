import matplotlib.pyplot as plt
import numpy as ap
import pandas as pd

students = ["Ali", "Mesum","Haseeb", "Ahmed"]
marks = [80,85,90,95]

plt.plot(students,marks,)
plt.plot(students,marks,"o")
plt.xlabel("Students")
plt.ylabel("marks")
plt.title("STUDENTS MARKS")
plt.show()