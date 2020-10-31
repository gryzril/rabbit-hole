from bs4 import BeautifulSoup, SoupStrainer
from string import punctuation
import urllib.request
import requests
import UserAgentHandler
import re
from urllib.parse import urlparse
import WordCount

#iterates each page with a prompt for every single individual page
def iterate_num_pages_per_page(query, num_pages):
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
            #while i < j:
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
                i = i - 1  #Compensate for URL not being passed through

            i = i + 1
    else:
        print("Error Connecting to Google")

def iterate_num_pages_total(query, num_pages):
    user_agent = UserAgentHandler.return_user_agent()
    headers = {"user-agent": user_agent}
    URL = f"https://google.com/search?q={query}"
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        print("Initial Request Success")
        soup = BeautifulSoup(resp.content, "html.parser")

        j = int(num_pages)
        i = 0;
        append_list = []
        text = ""
        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            #while i < j:
            url = link.get('href')

            new_resp = requests.get(url, headers=headers)
            if new_resp.status_code == 200:
                print(url)
                try:
                    html = urllib.request.urlopen(url).read()
                except:
                    print("Error: Invalid URL... Moving on")

                text = WordCount.text_from_html(html).split()
                append_list = append_list + text
        WordCount.print_common_words(append_list)




    else:
        print("Error connecting to Google")





    print("Test")



#returns TRUE link should be iterated, else FALSE
def link_filter(url):
    return false



user_query = input("Enter Word to Search")

valid_select = False;
while (not valid_select):
    try:
        per_or_total = input("(1) Each Individual Page Calculated, or (2) All Pages Calculated As One")
        valid_select = True;
    except:
        print("Incorrect Selection, Please Select: (1) Each Individual Page Calculated, or (2) All Pages Calculated As One")

user_num_pages = input("Number of Pages to Parse")
user_query = user_query.replace(' ', '+')      # Google expects query to be in parameters of URL and have spaces replaced with '+'

if(per_or_total == "1"):
    iterate_num_pages_per_page(user_query, user_num_pages)
else:
    iterate_num_pages_total(user_query, user_num_pages)






