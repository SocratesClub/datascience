import os, pandas as pd
import urllib.request

# Some "constants"
SRC_HOST = "https://vincentarelbundock.github.io"
FILE = "/lynx.csv"
SRC_NAME = SRC_HOST + "/Rdatasets/csv/datasets" + FILE
CACHE = "cache"
DOC = "doc"

# Prepare the directories, if needed
if not os.path.isdir(CACHE):
    os.mkdir(CACHE)
if not os.path.isdir(DOC):
    os.mkdir(DOC)

# Check if the file is cached; cache it if it's not
if not os.path.isfile(CACHE + FILE):
    try:
        src = urllib.request.urlopen(SRC_NAME)
        lynx = pd.read_csv(src)
    except:
        print("Cannot access %f." % SRC_NAME)
        quit()
    # Create a data frame
    lynx.to_csv(CACHE + FILE)
else:
    lynx = pd.read_csv(CACHE + FILE)

# Add the "decade" column
lynx["decade"] = (lynx['time'] / 10).round() * 10

# Aggregate and sort
by_decade = lynx.groupby("decade").sum()
by_decade = by_decade.sort_values(by="lynx", ascending=False)

# Save the results
by_decade["lynx"].to_csv(DOC + FILE)
