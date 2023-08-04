from bs4 import BeautifulSoup
import requests

url = 'https://google.com/search?q=how+to+cook+pizza'
r = requests.get(url)

try:
    soup = BeautifulSoup(r.content, "html.parser")
    searchTitles = soup.find_all("h3")
    for title in searchTitles:
        print(title.text.strip())
    print('\n\n', "It's a successful Get request")

except requests.ConnectionError:
    print('The server returned the Status code: ', r.status_code)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
