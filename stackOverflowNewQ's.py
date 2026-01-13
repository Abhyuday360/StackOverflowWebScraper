import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text,"html.parser")

selector = soup.select(".s-post-summary")

print(type(selector))

for i in selector:
    print(i.select_one(".s-link").get_text())
    print("Votes: ",i.select_one(".s-post-summary--stats-item-number").get_text())

