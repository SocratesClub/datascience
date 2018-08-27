import pandas as pd, numpy as np
import sklearn.cluster, sklearn.preprocessing
import matplotlib, matplotlib.pyplot as plt

# Read the data
mosn = pd.read_csv('mosn.csv', thousands=',',
                   names=('Name', 'Description', 'Date', 'Registered Users',
                          'Registration', 'Alexa Rank'))
columns = ['Registered Users', 'Alexa Rank']

# Eliminate rows with missing data and zeros
good = mosn[np.log(mosn[columns]).notnull().all(axis=1)].copy()

# Do clustering
kmeans = sklearn.cluster.KMeans()
kmeans.fit(np.log(good[columns]))
good["Clusters"] = kmeans.labels_

# Which one is the Facebook?
fb = good.set_index('Name').ix['Facebook']['Clusters']

# Select a good-locking style
matplotlib.style.use("ggplot")

# Display the results
ax = good.plot.scatter(columns[0], columns[1], c="Clusters", 
                       cmap=plt.cm.Accent, s=100)
plt.title("Massive online social networking sites")
plt.xscale("log")
plt.yscale("log")

# Annotate the most prominent sites
def add_abbr(site):
    if site['Clusters'] == fb:
        _ = ax.annotate(site["Name"], site[columns], xytext=(1, 5), 
                        textcoords="offset points", size=8,
                        color="darkslategrey")
good.apply(add_abbr, axis=1)

plt.savefig("../images/mosn.png")
