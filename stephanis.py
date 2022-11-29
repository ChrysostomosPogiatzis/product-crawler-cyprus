
# Import Module
from bs4 import BeautifulSoup
import requests
import json
import time
import re

 
def my_function(URL):  
# class list set
	class_list = set(URL)
  
# Page content from Website URL
	page = requests.get( URL )
 
	soup = BeautifulSoup( page.content , 'html.parser')

	product_title=soup.find('title').text;
	product_specifications=soup.find(class_='tab-specifications').text
	product_sku_number=soup.find("span", {"id": "sku-number"}).text

	if(soup.find(class_='item-price')=='None'):
		product_price=soup.find(class_='large-was-price').text
		product_offer_price=soup.find(class_='with-sale').text
	else:
		product_price=soup.find(class_='item-price').text
		product_offer_price='None';
	
	
	results = soup.find_all('div', attrs={"class":"stock-location-text"})
	results1 = soup.find_all('div', attrs={"class":"stockstatus"})
 
	store_list=[];
	status_list=[]
	for stores in results:
	 
		store_list.append(stores.text);
	for status in results1:
	 
		status_list.append(status.text);

	x = {
	  "name": product_title,
	  "price": product_price,
	  "offer": product_offer_price,
	   "sku_number": product_sku_number,
	    "specifications": product_specifications,
	    "stores": store_list,
	     "status": status_list,
	     "image":""
	}

# convert into JSON:
 

# the result is a JSON string:
	print(x)
	time.sleep(2);
	
sitemap = requests.get("https://www.stephanis.com.cy/sitemap.xml")
result = BeautifulSoup(sitemap.content, "xml")

urls_from_xml = []

loc_tags = result.find_all('loc')
for loc in loc_tags:
	
	 
	if 'https://www.stephanis.com.cy/en/products/' in loc.get_text():
		print("----------"+loc.get_text()+"---------");
		my_function(loc.get_text());   
 

