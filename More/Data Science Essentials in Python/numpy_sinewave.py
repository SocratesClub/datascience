# Import all good things
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# The constants define the signal, noise, and "instrument"
# properties
SIG_AMPLITUDE = 10; SIG_OFFSET = 2; SIG_PERIOD = 100
NOISE_AMPLITUDE = 3
N_SAMPLES = 5 * SIG_PERIOD
INSTRUMENT_RANGE = 9

# Construct a sine wave and mix it with some random noise
times = np.arange(N_SAMPLES).astype(float)
signal = SIG_AMPLITUDE * np.sin(2 * np.pi * times / SIG_PERIOD) + SIG_OFFSET
noise = NOISE_AMPLITUDE * np.random.normal(size=N_SAMPLES)
signal += noise

# Truncate spikes that are outside of the instrument range
signal[signal > INSTRUMENT_RANGE] = INSTRUMENT_RANGE
signal[signal < -INSTRUMENT_RANGE] = -INSTRUMENT_RANGE



# Plot the results
matplotlib.style.use("ggplot")
plt.plot(times, signal)
plt.title("Synthetic sine wave signal")
plt.xlabel("Time")
plt.ylabel("Signal + noise")
plt.ylim(ymin = -SIG_AMPLITUDE, ymax = SIG_AMPLITUDE)

# Save the plot
plt.savefig("../images/signal.pdf")
