import matplotlib, matplotlib.pyplot as plt
import pickle, pandas as pd
import sklearn.cluster, sklearn.preprocessing

# The NIAAA frame has been pickled before
alco2009 = pickle.load(open("alco2009.pickle", "rb"))
# States" abbreviations
states = pd.read_csv("states.csv", 
                     names=("State", "Standard", "Postal", "Capital"))
columns = ["Wine", "Beer"]
# Initialize the clustering object, fit the model
kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco2009[columns])
alco2009["Clusters"] = kmeans.labels_
centers = pd.DataFrame(kmeans.cluster_centers_, columns=columns)

# Select a good-looking style
matplotlib.style.use("ggplot")

# Plot the states and cluster centroids
ax = alco2009.plot.scatter(columns[0], columns[1], c="Clusters", 
                           cmap=plt.cm.Accent, s=100)
centers.plot.scatter(columns[0], columns[1], color="red", marker="+", 
                     s=200, ax=ax)

# Add state abbreviations as annotations
def add_abbr(state):
    _ = ax.annotate(state["Postal"], state[columns], xytext=(1, 5), 
                    textcoords="offset points", size=8,
                    color="darkslategrey")

alco2009withStates = pd.concat([alco2009, states.set_index("State")], 
                               axis=1)
alco2009withStates.apply(add_abbr, axis=1)

# Add the title, save the plot
plt.title("US States Clustered by Alcohol Consumption")
plt.savefig("../images/clusters.pdf")
