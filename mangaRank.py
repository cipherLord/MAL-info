import sys
import requests
from bs4 import BeautifulSoup

r = requests.get("https://myanimelist.net/topmanga.php")
c = r.content
soup = BeautifulSoup(c, "html.parser")
ranking_list = soup.find_all("tr", {"class" : "ranking-list"})

rank = int(input("Enter the RANK :: "))
if rank in range(0,9):
    rank_page = str('lightLink top-anime-rank-text rank1')
elif rank in range(10,50):
    rank_page = str('lightLink top-anime-rank-text rank2')

print('Name :: ' + ranking_list[rank-1].find("a", "hoverinfo_trigger fs14 fw-b").text)
print('Volumes :: ' + ranking_list[rank-1].find("div", "information di-ib mt4").text)
print('Score :: ' + ranking_list[rank-1].find("div", "js-top-ranking-score-col di-ib al").find("span").text)
