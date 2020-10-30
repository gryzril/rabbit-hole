from bs4 import BeautifulSoup, SoupStrainer
from string import punctuation
import urllib.request
import requests
import UserAgentHandler
import re
from urllib.parse import urlparse
import WordCount

def iterate_num_pages(query, num_pages):
    user_agent = UserAgentHandler.return_user_agent()
    headers = {"user-agent":user_agent}
    URL = f"https://google.com/search?q={query}"
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        print("Initial Request Success")
        soup = BeautifulSoup(resp.content, "html.parser")

        j = int(num_pages)
        i = 0;
        text = ""
        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            url = link.get('href')

            new_resp = requests.get(url, headers=headers)
            if new_resp.status_code == 200:
                print(url)
                try:
                    html = urllib.request.urlopen(url).read()
                except:
                    print("Error: Invalid URL... Moving on")
                text = WordCount.text_from_html(html).split()

                WordCount.print_common_words(text)
                print("\n")

            else:
                print("ERROR " + url)


#returns TRUE link should be iterated, else FALSE
def link_filter(url):
    return false



user_query = input("Enter Word to Search")
user_num_pages = input("Number of Pages to Parse")
user_query = user_query.replace(' ', '+')      # Google expects query to be in parameters of URL and have spaces replaced with '+'
iterate_num_pages(user_query, user_num_pages)
