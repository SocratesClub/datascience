import pandas as pd
from scipy.stats import pearsonr

# Read the data
sap = pd.read_csv("sapXXI.csv").set_index("Date")

# Calculate and report all stats
print("Mean:", sap["Close"].mean())
print("Standard deviation:", sap["Close"].std())
print("Skewness:", sap["Close"].skew())
print("Correlation:\n", sap[["Close", "Volume"]].corr())
_, p = pearsonr(sap["Close"], sap["Volume"])
print("p-value:", p)
