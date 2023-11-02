from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://merojob.com/search/?q=python').text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'row job-card text-center text-lg-left ml-2')

for job in jobs:
    company_name = job.find('h3', class_ = 'h6').text.replace(' ', '')
#skills = jobs.find_all('span', class_ = 'badge badge-pill badge-light rounded text-muted').text
    skills = job.find('span', itemprop = 'skills').text.replace(' ', '')
    location = job.find('span', itemprop = 'addressLocality').text.replace(' ', '')
    more_info = job.find('div', class_ = 'col-8 col-lg-9 col-md-9 pl-3 pl-md-0 text-left').h1.a['href']
    with open(f'job.txt', 'a') as f:
        f.write(f"Company Name: {company_name.strip()}")
        f.write(f"Skills Required:\n{skills.strip()}")
        f.write(f"Location: {location.strip()}")
        f.write(f"More info:https://merojob.com{more_info}")
        f.write('\n')