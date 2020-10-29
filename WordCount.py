import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from string import punctuation
import urllib.request


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


def print_common_words(text):
    commonWords = []
    for i in text:
        if text.count(i) >= 20 and commonWords.count(i) == 0:
            commonWords.append(i)
    if len(commonWords) > 0:
        print('The common words are:')
        for i in commonWords:
            print(i)
    else:
        print('no words used 5 or more times')


html = urllib.request.urlopen('https://en.wikipedia.org/wiki/StarCraft').read()
text = text_from_html(html).split()
print_common_words(text)


