from requests import post, Session
from fake_useragent import UserAgent

link = 'https://passport.yandex.com/auth'
user = UserAgent().random

headers = {
    'user-agent': user
}

data = {
    'login': 'InfinityProblem@yandex.ru',
    'passwd': 'Problem39113911d'
}

session = Session()

response = session.post(link, headers=headers, data=data)

with open('response.html', 'w') as file:
    file.write(response.text)
