import requests
from bs4 import BeautifulSoup

response = requests.get("https://myanimelist.net/topanime.php")
soup = BeautifulSoup(response.content,'lxml')

datas = soup.find_all("div", class_ = "detail")
scores = soup.find_all("div", class_= "js-top-ranking-score-col di-ib al")
i=1
for data in datas :
    print(i,end ="") 
    print(". ",end ="")
    print(data.find("a",class_= "hoverinfo_trigger fl-l fs14 fw-b").text.replace("\n",""))
    print(data.find("div",class_="information di-ib mt4").text.replace("\n",""))
    print("\n")
    i= i+1
    # print(data.find_all("div", class_="information di-ib mt4")).text
