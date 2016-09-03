# -*- coding:utf-8 -*- 
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
	# /view/123.htm
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		#links = soup.find_all('ul',href = re.compile(r"/view/\d+\.htm"))
		links = soup.find('ul',class_="pagelist cl").find_all('a',href = re.compile(r"/list/index"))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)

			#test
			print new_full_url

		return new_urls

	def _get_new_datas(self,page_url,soup):
		if soup == None:
			print 'err'
			return 
		datas = []	
	
		links = soup.find_all('div',class_="item cl")
		for link in links:
			title = link.find('b')
			if title == None:
				break
			grade = link.find('p',class_="rt2").find('strong')
			print "find: "+title.get_text()
			res_data={}
			res_data['title'] = title.get_text()
			res_data['grade'] = grade.get_text()
			res_data['url'] = page_url
			datas.append(res_data)
		print "endPage"

		#print datas

		return datas

	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return	
		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		try:
			new_urls = self._get_new_urls(page_url,soup)
			new_datas = self._get_new_datas(page_url,soup)
		except Exception, e:
			print e.message
		return new_urls, new_datas