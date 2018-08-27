import urllib.request, re
from collections import Counter

# Talk to the user and the Internet
url = input("Enter the URL: ")
try:
    page = urllib.request.urlopen(url)
except:
    print("Cannot open %s" % url)
    quit()

# Read and partially normalize the page
doc = page.read().decode().lower()

# Split the text into words
words = re.findall(r"\w+", doc)

# Build a counter and report the answer
print(Counter(words).most_common(10))
