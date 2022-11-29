
# Import Module
from bs4 import BeautifulSoup
import requests
import json
import time
import re
import gzip
import urllib.request
 
def my_function(URL):  
	headers = {'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'}

# class list set
	class_list = set(URL)
  
# Page content from Website URL
	page = requests.get( URL, headers=headers )
 
	soup = BeautifulSoup( page.content , 'html.parser')
	
	product_title=soup.find('title').text;
	print(product_title);
	product_price=soup.find(class_='product__price product__price--pdp-xlarge text-pdp-primary').text
	print(product_price);
	if(soup.find(class_='product__price--initial') is not None ):
		product_price_offer=soup.find(class_='product__price--initial').text.strip()
		
	else:
		product_price_offer='None'
		
	print(product_price_offer);
	product_desc=soup.find(class_='table').text
	print(product_desc);
	product_desc=soup.find(class_='product__sku').text
	print(product_desc);
	time.sleep(15);
url="https://www.public.cy/sitemap/sitemap_public_products_0.xml.gz";	
def download_file(url):
       out_file = './public.xml'

       # Download archive
       try:
          # Read the file inside the .gz archive located at url
          with urllib.request.urlopen(url) as response:
             with gzip.GzipFile(fileobj=response) as uncompressed:
                file_content = uncompressed.read()

          # write to file in binary mode 'wb'
          with open(out_file, 'wb') as f:
             f.write(file_content)
             return 0

       except Exception as e:
          print(e)
          return 1
download_file(url);
with open('public.xml', 'r') as f:
    data = f.read()
 
# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
result = BeautifulSoup(data, "xml")


urls_from_xml = []

loc_tags = result.find_all('loc')
for loc in loc_tags:
	
	 
	if 'https://www.public.cy/product/' in loc.get_text():
		print("----------"+loc.get_text()+"---------");
		my_function(loc.get_text());   
 

