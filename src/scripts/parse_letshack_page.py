import json
import emoji.unicode_codes
import requests 
from bs4 import BeautifulSoup as BS
import re


EMAIL = 'bopleromn@gmail.com'
PASSWORD = '0qGUJMNnNw'


def get_auth_token(session: requests.Session) -> str:
    response = session.get(url='https://xn--80ajqb5afw.xn--80aa3anexr8c.xn--p1acf/')

    parser = BS(response.text, 'html.parser')
    
    return parser.find('input', {'name': "_token"})['value']


def authorize(session: requests.Session, token: str) -> str:
    response = session.post(
        url='https://xn--80ajqb5afw.xn--80aa3anexr8c.xn--p1acf/login',
        data = {
            'email': EMAIL,
            'password': PASSWORD,
            '_token': token
        },
    )
    
    return response.text


def get_teams_link(session: requests.Session, html_content: str) -> str:
    parser = BS(html_content, 'html.parser')
    teams_link = None
    
    for side_bar_items in parser.find_all('li', {'class': 'nav-item'}):
        if side_bar_items.text.strip() == 'Команды':
            teams_link = side_bar_items.find('a')['href']
    
    # if there is not such item, then user is not authorized
    if teams_link is None:
        raise Exception('Не авторизован')
    
    return teams_link


def get_teams_pages_links(session: requests.Session, teams_page_link: str) -> list:
    html_content = session.get(teams_page_link).text
    parser = BS(html_content, 'html.parser')
    
    teams_urls = []

    for team_content_div in parser.find_all('a', {'class': 'team-link team-wrapper'}):
        teams_urls.append(team_content_div['href'])

    return teams_urls

def get_page_info(session: requests.Session, teams_page_link: str) -> str:
    html_content = session.get(teams_page_link).text
    parser = BS(html_content, 'html.parser')
    
    name: str = parser.find('div', {'class': 'team-title title-text-small'}).text
    
    for team_widget_card in parser.find_all('div', {'class': 'team-widget-card'}):
        if team_widget_card.find('h6') and team_widget_card.find('h6').text == 'Описание команды':
            description: str = team_widget_card.find('div', {'class': 'body-text-medium'}).text
            
    users: list = []
    
    for list_item in parser.find_all('a', {'class': 'team-item user-profile-link'}):
        user_name = list_item.find('div', {'class': 'team-item-name body-text-large'}).text.strip()
        photo_url = list_item.find('img')['src'] 
        
        users.append({
            'user_name': user_name,
            'photo': photo_url if photo_url != '/images/user-default.png' else 'default'
        })
        
    return {
        'name': name.strip(),
        'description': remove_emojis(description.strip().replace('\n', '').replace('\r', '').replace('.', '. ')),
        'users': users
    }
    
def remove_emojis(text: str):
    emoji_pattern = re.compile('['
                               u'\U0001F600-\U0001F64F'
                               u'\U0001F300-\U0001F5FF'  
                               u'\U0001F680-\U0001F6FF'  
                               u'\U0001F1E0-\U0001F1FF' 
                               ']+', flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)

def write_to_file(data: list):
    with open('parsed_info.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        
        
if __name__ == '__main__':
    with requests.Session() as session:        
        token = get_auth_token(session)
        
        page_content = authorize(session, token)
        
        teams_link = get_teams_link(session, page_content)
        
        teams_pages_links = get_teams_pages_links(session, teams_link)
        
        pages_info = []
        
        for teams_pages_link in teams_pages_links:
            pages_info.append(get_page_info(session, teams_pages_link))
            
        write_to_file({'data': pages_info})