import urllib
import urllib2
import cookielib
from BeautifulSoup import BeautifulSoup as BS
print 'Oyster chekah 1 loading...'
cookies = cookielib.CookieJar()
data = urllib.urlencode({'': '', '': ''})
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
res = opener.open('https://oyster.tfl.gov.uk/oyster/security_check', data)
soup = BS(res.read())
cards = []
for op in soup.form.findAll('option'):
    if op['value']:
        cards.append(op['value'])
datacard = urllib.urlencode({'method':'input', 'cardId':'056347247367'})
res = opener.open('https://oyster.tfl.gov.uk/oyster/selectCard.do', datacard)
journeyhistorydata = urllib.urlencode({'dateRange':'01/03/2013 00:00:00-04/05/2013 23:59:59','offset':'0','rows':'0','customDateRangeSel':'false','isJSEnabledForPagenation':'true'})
res = opener.open('https://oyster.tfl.gov.uk/oyster/journeyHistory.do', journeyhistorydata)
history = BS(res.read()).find('table', 'journeyhistory')
for roudata in history.findAll('tr'):
	if str(roudata.find('status-1')!=-1):
		try:
			print roudata.findAll('td')[1].string
		except:
			pass
	try:
		if roudata.findAll('td')[1].string == None:
			print roudata.findAll('td')[0].string
	except:
		pass