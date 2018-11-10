from bs4 import BeautifulSoup as soup
import requests
import csv

csv_file = open('result.csv','w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Head Line','Summary'])
	

with open('sample.html') as html_file:
	html_soup = soup(html_file, 'lxml')

for article in html_soup.find_all('div',class_='article'):
	head_line = article.h2.a.text
	print(head_line)

	summary = article.p.text
	print(summary)
	
	print("")
	
	csv_writer.writerow([head_line,summary])

csv_file.close()
