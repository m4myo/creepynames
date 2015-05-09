import urllib, json, socket, webbrowser, csv
socket.setdefaulttimeout(60)

with open('names.csv', 'w') as csvfile:
	fieldnames = ['first_name', 'last_name','gender']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

def crawl_ppl(startfrom=100005033137443,until = 10000):
	last = startfrom+until
	cnt=1
	print "Starting..."
	while(startfrom<last):
		try:
			data = urllib.urlopen("https://graph.facebook.com/"+str(startfrom))
			text = data.read()
			js_text = json.loads(text)
			if "first_name" in js_text:
				fn = js_text['first_name'].encode('utf-8')
				ln = js_text['last_name'].encode('utf-8')
				gender= js_text['gender'].encode('utf-8')
				print cnt,' - ',fn,ln, ' - ',gender
				
				with open('names.csv', 'a') as csvfile:
					writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
					writer.writerow({'first_name':fn,'last_name':ln,'gender':gender})
			cnt+=1 
			startfrom+=1
		except IOError, e:
			print e.errno

def crawl_page(startfrom,until=10000):
	print "TBC"
	
if __name__ == "__main__":
	print """Facebook User Data Collection"""
	prompt = raw_input("Wanna start with default values? y/n(press random keys and script will take to 2 stupid pages) - ")
	if prompt=='y':
		crawl_ppl()
	elif prompt=='n':
		startId = int(raw_input("Starting ID? - "))
		total = int(raw_input("How many accounts to crawl? - "))
		crawl(startfrom=startId,until=total)
	else:
		webbrowser.open_new_tab("http://bit.ly/18IYWs2")