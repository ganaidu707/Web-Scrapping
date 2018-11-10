from bs4 import BeautifulSoup as soup
import requests as uriReq
import csv

csv_file = open('result.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Language','Date','Description'])

html_source = uriReq.get('https://github.com/ganaidu707?tab=repositories').text
html_soup = soup(html_source,'lxml')

for article in html_soup.find_all('li', class_='col-12 d-block width-full py-4 border-bottom public source'):

	title = article.find('div', class_='d-inline-block mb-1').text
	print(title)

	Language = article.find('span',itemprop='programmingLanguage').text
	print(Language)
	
	Date = article.find('relative-time').text
	print(Date)
	
	Description = article.find('p').text
	print(Description)
	csv_writer.writerow([title, Language, Date, Description])

csv_file.close()
