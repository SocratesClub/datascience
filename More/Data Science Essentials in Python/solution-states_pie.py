import pandas as pd
import matplotlib, matplotlib.pyplot as plt

def initial(word):
    return word[0]

# Read the state names (use whatever source you like!)
states = pd.read_csv("states.csv", 
                     names=("State", "Standard", "Postal", "Capital"))

# Select a good-locking style
matplotlib.style.use("ggplot")

# Plotting
plt.axes(aspect=1)
states.set_index('Postal').groupby(initial).count()['Standard'].plot.pie()
plt.title("States by the First Initial")
plt.ylabel("")

plt.savefig("../images/states-pie.pdf")
