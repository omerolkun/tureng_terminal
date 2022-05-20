from bs4 import BeautifulSoup
import requests
import sys

word = ""
for i in range (1, len(sys.argv)):
    word = word + sys.argv[i] + " "

url = "https://tureng.com/en/turkish-english/"+word
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
try:
    print(soup.find("h2").text)
except:
    print("no result")
    exit()
soup  = soup.find("table",{"class":"table table-hover table-striped searchResultsTable"}).text.split("\n")
result = []

for item in soup:
    if len(item) > 0:
        result.append(item)


result.pop(0)
result.pop(0)
result.pop(0)

for i in range (len(result)):
    print(result[i])