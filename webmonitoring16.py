#dont forget to run the pip install 
#easy_install pip  
#pip install BeautifulSoup4
#https://pages.github.com/
#pip install bs4
#pip install twilio 
	
from twilio.rest import Client
from datetime import datetime

account_sid = 'XXX'
auth_token = 'XXX'
twilio_phone_number = 'XXX'
my_phone_number = 'XXX'

client = Client(account_sid, auth_token)
 
def main ():


		import urllib2
		from bs4 import BeautifulSoup
		quote_page = 'http://bobphysicsone.blogspot.com/'
		page = urllib2.urlopen(quote_page)
		soup = BeautifulSoup(page, 'html.parser')
		name_box = soup.find('li', attrs={'class': 'archivedate'})
		name = name_box.text.strip() # strip() 
		print name
		price_box = soup.find('div', attrs={'class':'widget-content'})
		price = price_box.text
		print price 
		
		#Text your the information.
		body = name + ', ' + price + ', ' + str(datetime.now())
		client . messages.create(
			body=body,
			to=my_phone_number,
			from_=twilio_phone_number
		)
		
		#export to excel csv
		
#		import csv
#		with open('index.csv', 'a') as csv_file:
#			writer = csv.writer(csv_file)
#			writer.writerow([name, price, datetime.now()])
#		quote_page = ['http://bobphysicsone.blogspot.com/', ‘http://bobphysicsone.blogspot.com/']
		
#		data = [] 
#		for pg in quote_page:
#		page = urllib2.urlopen(pg)
#		soup = BeautifulSoup(page, 'html.parser')
#		name_box = soup.find('li', attrs={'class': 'archivedate'})
#		name = name_box.text.strip() 
#		price_box = soup.find('div', attrs={'class':'widget-content'})
#		price = price_box.text
#		data.append((name, price))
#		with open('index.csv', 'a') as csv_file:
#			writer = csv.writer(csv_file)
#		for name, price in data:
#		writer.writerow([name, price, datetime.now()])
		
		
 
if __name__ == "__main__":
	main()
