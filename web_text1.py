import urllib
from bs4 import BeautifulSoup
from google import search
import thread

def extract_text_from_html(weblink):

	#url = "https://www.tutorialspoint.com/python/list_len.htm"
	url=weblink
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html,"html5lib")

	# kill all script and style elements
	for script in soup(["script", "style"]):
	    script.extract()    # rip it out

	# get text
	text = soup.get_text()


	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())

	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)

	#print(text.encode('utf-8'))
	x=text.encode('utf-8')
	finaltext=x.split("\n")

	reducedpassage=""

	for i in finaltext:
		if len(i)>20 and i.find(".")!=-1 and i.find("<")!=0 and i.find("#")==-1 and  i.find("@")==-1 i.find("@")==-1 :
			reducedpassage+=i+'\n'
	return reducedpassage


def get_links( search_query):
	list1=[]
	for url in search(search_query, stop=10):
		list1.append(url.encode('utf-8'))
	#print list1
	return list1


def text_summarizer():

	return

def main():
	detailed_result_list=[]
	search_result=get_links('Barcelona')
	for i in search_result:
		detailed_result_list.append(extract_text_from_html(search_result[0]))
	#print detailed_result_list
	print len(detailed_result_list)
	print '\n'
	print detailed_result_list[0]
	return

if __name__ == '__main__':
	main()
