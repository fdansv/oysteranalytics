import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup as BS
cookies = cookielib.CookieJar()
data = urllib.urlencode({'j_username': '', 'j_password': ''})
u = urllib2.urlopen('https://oyster.tfl.gov.uk/oyster/security_check', data)
req = urllib2.Request(u)
soup = BS(u.read())
cards = []
for op in soup.form.findAll('option'):
    if op['value']:
        cards.append(op['value'])
print cards
cookies.extract_cookies(um,req)