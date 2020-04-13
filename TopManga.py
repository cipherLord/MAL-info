import sys
import requests
from bs4 import BeautifulSoup

rank = number = int(input("Enter the RANK :: "))
digits = 0
while(number > 0):
    number = number // 10
    digits = digits + 1
rank_page = str('lightLink top-anime-rank-text rank' + str(digits))

limit = str(50 * int(rank / 50))
r = requests.get("https://myanimelist.net/topmanga.php?limit=" + limit)
c = r.content
soup = BeautifulSoup(c, "html.parser")
ranking_list = soup.find_all("tr", {"class" : "ranking-list"})

print('Name :: ' + ranking_list[(rank-1) % 50].find("a", "hoverinfo_trigger fs14 fw-b").text)
print('Volumes :: ' + ranking_list[(rank-1) % 50].find("div", "information di-ib mt4").text)
print('Score :: ' + ranking_list[(rank-1) % 50].find("div", "js-top-ranking-score-col di-ib al").find("span").text)