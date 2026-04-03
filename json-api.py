import urllib.request, urllib.parse
import json, ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1: 
        break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'features' not in js:
        print('==== Download error ====')
        print(data)
        break
    
    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break
    
    # print(json.dumps(js, indent=4))

    pc = js['features'][0]['properties']['plus_code']
    print('Plus code', pc)