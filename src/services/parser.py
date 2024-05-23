from base64 import b64encode
import requests 
from fake_useragent import UserAgent 
from bs4 import BeautifulSoup as BS


# file_path = '../utils/letshack.html'

# with open(file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# parser = BS(html_content, 'html.parser')

# for team_content_div in parser.find_all('a', {'class': 'team-link team-wrapper'}):
#     team_content_url = team_content_div.attrs['href']
    
#     response = requests.get(team_content_url)

#     if response.status_code != 200:
#          raise Exception(f'Erorr: {response.content}')
cookies = {
    '__ddg1_': 'IMO5PwkBuvz7fDpC4QSc',
    'XSRF-TOKEN': 'eyJpdiI6IjVCN3poRkJyUDRDNGpqampYRU90VGc9PSIsInZhbHVlIjoiRFR5N0dWZ3Q3NHE5eXluRE84WlhBV1pZN1FHM0xoOWNDWmYxTWFMT1BnSFRsK0tTMTZZL1JDSWdMQXZybWlyWGVRUWxpODVSaDFydkR2eE5JR3pqWTAvRUlxRDJrNkVEMm5GeDVyMEg3eEcxQU1meVdjY0YyOEVYcHlJZzBBcXkiLCJtYWMiOiI2ZWNkMjFlM2UxZDM1NzIwYjU1MDU0NGIzMjVkNmM0ODU1NzRlNzk0NTE1ZTNiOWIxODNiYWJlMDU5OTQ2MDZiIiwidGFnIjoiIn0%3D',
    'letshack_session': 'eyJpdiI6InQ2VWlpVFpacjFYcCt2d2dOa2JocFE9PSIsInZhbHVlIjoiNEZ2Rmg2c0VqUVBGZnp2VW9qRzhEdTdxSnFESi9oMEYrdjRmVy85VjB4K0tscmpDMlV6VXBqZElKSmFKdjltdHdUZ2N5Qmw1L1EwQ3NwdU5Gcy83YmhrMW55Smt4WE5IM1ZzeU81UmZibGVOS0RUaTFicUJZdEwvMDBxZythK0MiLCJtYWMiOiJhZTNkMTkwNDMzMTA5ZDEzMzM4YWZhMTgxNWUxZjQ1MWMxYWM0MDc5ODFlNTlhZWVmMTU5ZTRjNmM2NmUwNjM5IiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://xn--80ajqb5afw.xn--80aa3anexr8c.xn--p1acf',
    'Referer': 'https://xn--80ajqb5afw.xn--80aa3anexr8c.xn--p1acf/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': UserAgent().random,
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    '_token': 'kK0lAWXHuQ6k9ZFthyxCxCbBZxN8HawUPvaqhgy3',
    'email': 'bopleromn@gmail.com',
    'password': '0qGUJMNnNw',
}

response = requests.post('https://xn--80ajqb5afw.xn--80aa3anexr8c.xn--p1acf/login', headers=headers, data=data)

print(response.content)