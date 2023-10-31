from pprint import pprint
import requests
from bs4 import BeautifulSoup
import lxml
import fake_headers
from datetime import datetime
import json
from month_in_int import month_in_int

headers_gen = fake_headers.Headers(browser='chrome', os='win')
page = 1
data_dict = {}
while True:
    url = f'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&item_on_page=20&page={page}'
    page += 1
    response = requests.get(url, headers=headers_gen.generate())
    if response.status_code == 404:
        break
    html_data = response.text
    soup = BeautifulSoup(html_data, 'lxml')
    vacancy_id = soup.find('div', id='a11y-main-content')
    vacancy_list = vacancy_id.find_all('div', class_='serp-item')
    i = 0
    for vacancy in vacancy_list:
        header_vacancy = vacancy.find('a')
        header = header_vacancy.text
        marks = ''',()-_/+|'''
        for j in header:
            if j in marks:
                header = header.replace(j, " ")
        header_split = header.split()
        if 'Django' in header_split or 'Flask' in header_split:
            ref = header_vacancy['href']
            response_vacansy = requests.get(ref, headers=headers_gen.generate())
            html_vacansy = response_vacansy.text
            soup_vacansy = BeautifulSoup(html_vacansy, 'lxml')
            creation_time_vacancy = soup_vacansy.find('p', class_='vacancy-creation-time-redesigned')
            if creation_time_vacancy != None:
                creation_time_vacancy = creation_time_vacancy.find('span')
                date = creation_time_vacancy.text
            else:
                date = ''
            if date != '':
                date = month_in_int(date)
            today = str(datetime.now().date())
            if date == today:
                vacancy_title = soup_vacansy.find('div', class_='vacancy-title')
                salary_title = vacancy_title.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite')
                if salary_title != None:
                    salary_str = salary_title.text
                    salary_list = salary_str.split()
                    if 'от' in salary_list:
                        salary_nim = salary_list[1]
                    else:
                        salary_nim = ' - '
                    if 'до' in salary_list:
                        salary_index = salary_list.index('до')
                        salary_max = salary_list[salary_index + 1]
                    else:
                        salary_max = ' - '
                    salary = f'от {salary_nim} до {salary_max} т.р.'
                else:
                    salary = 'не указана'
                company_vacansy = vacancy.find('div',class_='bloko-v-spacing-container bloko-v-spacing-container_base-2')
                company = company_vacansy.text
                info_vacansy = vacancy.find('div', class_='vacancy-serp-item__info')
                all_text_vacansy = info_vacansy.find_all('div', class_='bloko-text')
                city_vacansy = all_text_vacansy[1]
                city = city_vacansy.text
                city = city.split()[0]
                data_str = f'Зарплата - {salary}, Компания - {company}, Город - {city}, Ссылка - {ref}, Дата - {date}'
                data_dict[header] = data_str
data_json = json.dumps(data_dict,ensure_ascii=False)
with open('data_vacansy.json', 'w',encoding='utf-8') as f:
    f.write(data_json)



