import bs4 as BeautifulSoup
import urllib.request
import networkx as nx
import community

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_land_borders"
with urllib.request.urlopen(URL) as source:
    soup = BeautifulSoup.BeautifulSoup(source)

table = soup.findAll("table", {"class": "wikitable sortable"})[0]

G = nx.Graph()

for row in table.findAll("tr")[1:]:
    row = row.findAll('td')
    countryA = list(row[0].strings)[1]
    try:
        length = float(row[1].text.replace(",",""))
    except:
        length = 0.0
    if countryA[0] != '[':
        G.add_node(countryA)
        G.node[countryA]["l"] = length
        for countryB in [x.string for x in row[4].findAll('a') 
                         if x["href"][0] != '#' 
                         and x.string != None 
                         and x.string[0] != '[']:
            G.add_edge(countryA, countryB)
        
G.remove_nodes_from(nx.isolates(G))
G.remove_nodes_from(["Palestine", "Antártica Chilena Province",
                     "West Bank", "Gaza Strip", "European Union"])

part = community.best_partition(G)
community.modularity(part, G)

with open("borders-1.graphml", "wb") as graph:
	nx.write_graphml(G, graph)
