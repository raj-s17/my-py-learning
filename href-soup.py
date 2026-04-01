# http://py4e-data.dr-chuck.net/known_by_Fikret.html (Sample Problem)
# http://py4e-data.dr-chuck.net/known_by_Denise.html (Actual Problem)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
count = int(input('Enter count: '))
posi = int(input('Enter position: '))

for i in range(count):   
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    
    tag = tags[posi - 1]
    url = tag.get('href', None)
    
    print("Retrieving:", url)