import requests
from bs4 import BeautifulSoup
import pprint

def get_content_of_page(url):
    response = requests.get(url)
    return  BeautifulSoup(response.text, "html.parser")

response = requests.get("https://news.ycombinator.com/newest")
soup = BeautifulSoup(response.text, "html.parser")

def retrieve_content(soup, class_name):
    return soup.select(f".{class_name}")





def sort_by_votes(custom_news):
    return sorted(custom_news, key=lambda k:k["votes"], reverse=True)

def create_custom_hacker_news(links, votes):
    hacker_news = []
    for index, link in enumerate(links):
        title = link.getText()
        link_of_title = link.get("href")
        points = list_of_votes[index].getText()
        point = int(points.split(" ")[0])
        if point > 99:
            hacker_news.append({"title":title, "votes":point, "link":link_of_title})
    return sort_by_votes(hacker_news)

soup = get_content_of_page("https://news.ycombinator.com/newest")
list_of_links = retrieve_content(soup, "titlelink")
list_of_votes = retrieve_content(soup, "score")
next_page = retrieve_content(soup, "morelink")


customized_content = []
first_page_content = create_custom_hacker_news(list_of_links, list_of_votes)
customized_content.append(first_page_content)
# pprint.pprint(customized_content)

while len(next_page) != 0:
    soup = get_content_of_page(f'https://news.ycombinator.com/{next_page[0].get("href")}')
    list_of_links = retrieve_content(soup, "titlelink")
    list_of_votes = retrieve_content(soup, "score")
    next_page = retrieve_content(soup, "morelink")
    page_content = create_custom_hacker_news(list_of_links, list_of_votes)
    customized_content.append(page_content)

pprint.pprint(customized_content)