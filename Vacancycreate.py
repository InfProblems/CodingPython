import requests
import json

vac_data = {
        "company": 2,
        "department": "Prospective Developments",
        "role": 119,
        "salary": "2000-4000",
        "gender": "All",
        "matching": 52.0,
        "location": {
            "country": "United Arab Emirates",
            "city": "Abu Hail"
        },
        "company_size": "1001-5000",
        "benefits": ["Medical insurance", "Vacation", "Plushki"],
        "work_experience": {
            "Backend developer": "3 years",
            "languages": "Kotlin"
        },
        "skills": [{
            "skill_id": 7,
            "required_years": 1
        }, {
            "skill_id": 87,
            "required_years": 2
        }],
        "languages_levels": [{
            "level": "B2&Upper",
            "language": {
                "id": 1,
                "name": "English"
            }
        }],
        "work_format": ["Part-time", "Full-time"],
        "occupation": "Develop high-load services",
        "description": "ChatGPT5 description...",
    }

payload = {
    'upload_file': json.dumps(vac_data)
}

url = 'https://d5dmvqknguqq0pikophn.apigw.yandexcloud.net/vacancies/'

url_token = "https://d5dmvqknguqq0pikophn.apigw.yandexcloud.net/api/token/"
creds = {"username": "test_owner_1", "password": "passpass"}
response_token = requests.post(url_token, data=creds)
token = response_token.json()["access"]
token = f"Bearer {token}"
headers = {"Authorization": token}

for i in range(299):
    response = requests.post(url, headers=headers, json=vac_data)
