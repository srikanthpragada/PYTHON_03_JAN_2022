import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com"
response = requests.get(URL)
if response.status_code != 200:
    print("Sorry! Could not get details!!!")
    exit(1)

bs = BeautifulSoup(response.text, "html.parser")

for link in bs.find_all("a"):
    href = link['href']
    if href == "#":
        continue

    if not href.startswith("http"):
        href = URL + "/" + href

    print(href)




