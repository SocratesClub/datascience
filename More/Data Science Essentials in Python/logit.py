from scipy.stats import logistic
import numpy as np
import matplotlib, matplotlib.pyplot as plt

# Select a nice plotting style
matplotlib.style.use("ggplot")

# Show several diffenet logit curves
x = np.arange(-10, 10.1, 0.05)
scales = (0.01, 0.5, 1, 2)
for scale in scales:
    plt.plot(x, logistic.cdf(x, 0, scale))

# Add decorations
plt.xlabel("x")
plt.ylabel("CDF(x)")
plt.title("Logistic function")
plt.ylim(ymin=-0.05, ymax=1.05)
plt.xlim(xmin=-10.05, xmax=10.05)
plt.legend(["Scale=%.2f" % scale for scale in scales], loc="lower right")

# Save the plot
plt.savefig("../images/logit.pdf")
