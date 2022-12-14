
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
	 
	data = [
    json.loads(x.string) for x in soup.find_all("script", type="application/ld+json")
]
	 
# the result is a JSON string:
	print(product_title)
	 
	for d in data:
    		for x in d['@graph']:
    			if(x['@type']=='Product'):
    				print(x['sku'])
	time.sleep(2);
	
sitemap = requests.get("https://www.supermarketcy.com.cy/en/sitemap/products.xml")
result = BeautifulSoup(sitemap.content, "xml")

urls_from_xml = []

loc_tags = result.find_all('loc')
for loc in loc_tags:
	
	 
	if 'https://www.supermarketcy.com.cy/' in loc.get_text():
		print("----------"+loc.get_text()+"---------");
		my_function(loc.get_text());   
 
