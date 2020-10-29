import requests
from bs4 import BeautifulSoup

#Search Query User Input
query = input("Enter Word to Search")
query = query.replace(' ', '+')       # Google expects query to be in parameters of URL and have spaces replaced with '+'
URL = f"https://google.com/search?q={query}"

# desktop user-agent -- I use Firefox 82.0.1 I guess
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/82.0.1"

headers = {"user-agent" : USER_AGENT}
resp = requests.get(URL, headers=headers) # browser response

# test request success, True = 200. If true, prints success and creates BeautifulSoup Object
if resp.status_code == 200:
    print("Initial Request Success")
    soup = BeautifulSoup(resp.content, "html.parser") # Default Python Parser

    data = soup.findAll("span", {"class": "aCOpRe"}) # assigns website preview spans to array [data]

    for b in data:
        dataNoDate = b.findAll("span",{"class": ""})
        for c in dataNoDate:
            print (c.prettify())
