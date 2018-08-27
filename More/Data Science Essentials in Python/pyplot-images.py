import matplotlib, matplotlib.pyplot as plt
import pickle, pandas as pd

# The NIAAA frame has been pickled before
alco = pickle.load(open("alco.pickle", "rb"))
del alco["Total"]
columns, years = alco.unstack().columns.levels

# The state abbreviations come straight from the file
states = pd.read_csv(
    "states.csv", 
    names=("State", "Standard", "Postal", "Capital"))
states.set_index("State", inplace=True)

# Alcohol consumption will be sorted by year 2009
frames = [pd.merge(alco[column].unstack(), states,
                   left_index=True, right_index=True).sort_values(2009) 
          for column in columns]

# How many years are covered?
span = max(years) - min(years) + 1

# Select a good-looking style
matplotlib.style.use("ggplot")

STEP = 5
# Plot each frame in a subplot
for pos, (draw, style, column, frame) in enumerate(zip(
        (plt.contourf, plt.contour, plt.imshow), # (1)
        (plt.cm.autumn, plt.cm.cool, plt.cm.spring), 
        columns, frames)):
    
    # Select the subplot with 2 rows and 2 columns
    plt.subplot(2, 2, pos + 1) # (2)

    # Plot the frame
    draw(frame[frame.columns[:span]], cmap=style, aspect="auto") # (3)

    # Add embellishments
    plt.colorbar() # (4)
    plt.title(column)
    plt.xlabel("Year")
    plt.xticks(range(0, span, STEP), frame.columns[:span:STEP])
    plt.yticks(range(0, frame.shape[0], STEP), frame.Postal[::STEP])
    plt.xticks(rotation=-17)

plt.tight_layout()
plt.savefig("../images/pyplot-all.pdf")
#plt.show()
