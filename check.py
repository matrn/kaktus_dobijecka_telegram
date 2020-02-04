#pip3 install selectolax
import requests
import time
from selectolax.parser import HTMLParser
from datetime import datetime




class Dobijecka:
	def __init__():
		self.url = 'https://www.mujkaktus.cz/chces-pridat'
def get_data():
	try:
		return requests.get(URL).text
	except requests.exceptions.RequestException as e:
		return None

'''
def parse_data(data):
	for line in data.lower().split('>'):
		line = line.strip()
		if 'pokud si dnes' in line:
			line = line.partition('<')[0]
			if 'od' in line and 'do' in line:
				return line
'''

def parse_data_html(html):
	data = None
	for node in HTMLParser(html).css('div.wrapper > h2.uppercase + h3.uppercase.text-drawn'):
		node_data = node.text().strip().lower()
		if 'pokud si dneska' in node_data and 'od' in node_data and 'do' in node_data:
			data = node_data
			break
	return data
	
	

def parse_date(data):
	def try_next(list, i, max_i):
		if i < max_i: return list[i]
		else: return None

	data = data.replace('  ', ' ').replace('. ', '.').replace(': ', ':')
	list = data.split(' ')
	count = 0
	date = None
	start = None
	stop = None
	max_i = len(list)
	for i in range(max_i):
		if 'dneska' == list[i]:
			date = try_next(list, i+1, max_i)

		elif 'od' == list[i]:
						start = try_next(list, i+1, max_i)

		elif 'do' == list[i]:
						stop = try_next(list, i+1, max_i)


	print(data)
	print("%s from %s, to %s" % (date, start, stop))
	return date, start, stop


def is_date_today(date):
	try:
		if datetime.strptime(date, '%d.%m.%Y').date() == datetime.today().date():
			return True
		else:
			return False
	except ValueError:
		return None
		

def is_dobijecka():
	html = get_data()
	if not data: return None, { 'error':'GET req failed' }

	data = parse_data_html(html)
	if not data: return None, { 'error':'HTML parse failed', 'raw':html }

	date, start_time, stop_time = parse_date(data)
	if not date: return None, { 'error':'DATE parsing failed', 'raw':data }
	
	return is_date_today(date), { 'date':date, 'start':start_time, 'stop':stop_time, 'msg':data}



		


'''
start = time.time()
parse_data(data)
stop = time.time()
print("%f ms" % ((stop-start)*1000))
'''


print(is_dobijecka())