import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# This is a partial listing
RATE = .0375
TERM = 30
simple =   (     RATE  * np.ones(TERM)).cumsum()
compound = ((1 + RATE) * np.ones(TERM)).cumprod() - 1

matplotlib.style.use("ggplot")
t = np.arange(1, 31)
plt.plot(t, compound)
plt.plot(t, simple)
plt.legend(["Compound", "Simple"], loc=2)
plt.xlabel("Year")
plt.ylabel("Accrued Interest")
plt.tight_layout()
plt.savefig("../images/interest.pdf")
