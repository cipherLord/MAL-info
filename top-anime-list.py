import requests
from bs4 import BeautifulSoup

i=1
baseUrl = "https://myanimelist.net/topanime.php?limit="

for iterator in range (0,10,1) :
    response = requests.get(baseUrl + str(iterator*50))
    soup = BeautifulSoup(response.content,'lxml')
    ranking_list = soup.find_all("tr",class_= "ranking-list")

    for data in ranking_list:
        print(i,end ="") 
        print(". ",end ="")
        print(data.find("div", class_ = "detail").find("a",class_= "hoverinfo_trigger fl-l fs14 fw-b").text.replace("\n",""))
        print(data.find("div", class_ = "detail").find("div",class_="information di-ib mt4").text.replace("\n",""))
        print("        Score: " + data.find("div", class_= "js-top-ranking-score-col di-ib al").find("span").text.replace("\n",""))
        print("\n")
        i= i+1
