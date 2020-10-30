import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from string import punctuation
import urllib.request
import user_input


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


# finds all common words, if there are more than var:usr occurrences they are printed to stdout
def print_common_words(text):
    usr = int(user_input.get_user_input("Enter a min amount of occurrences to count as common:\n"))
    common_words = []
    for i in text:
        if text.count(i) >= usr and common_words.count(i) == 0:
            common_words.append(i)
    if len(common_words) > 0:
        print('The common words are:')
        for i in common_words:
            print(i)
    else:
        print('no words used 5 or more times')


def list_popular_words(website):
    html = urllib.request.urlopen(website).read()
    text = text_from_html(html).split()
    print_common_words(text)
