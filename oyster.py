import urllib, urllib2
from BeautifulSoup import BeautifulSoup as BS

data = urllib.urlencode({'j_username':'FDANSV','j_password':'Fdv090190'})
u = urllib2.urlopen('https://oyster.tfl.gov.uk/oyster/security_check',data)
soup = BS(u.read())
for op in soup.form.findAll('option'):
    if op['value']:
        print op['value']
