import urllib.request, urllib.parse
import bs4 as BeautifulSoup

# Talk to the user and the Internet
base = input("Enter the URL: ")
try:
    page = urllib.request.urlopen(base)
except:
    print("Cannot open %s" % base)
    quit()

# Cook the soup
soup = BeautifulSoup.BeautifulSoup(page)

# Extract the links as (name, url) tuples
links = [(link.string, link["href"]) 
         for link in soup.find_all("a")
         if link.has_attr("href")]

# Try to open each link
broken = False
for name, url in links:
    # Combine the base and the link destinatuon
    dest = urllib.parse.urljoin(base, url)
    try:
        page = urllib.request.urlopen(dest)
        page.close()
    except:
        print("Link \"%s\" to \"%s\" is probably broken." % (name, dest))
        broken = True

# Good news!
if not broken:
    print("Page %s does not seem to have broken links." % base)
        
