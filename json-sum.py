# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_2365290.json (Sum ends with 0)

import json
import urllib.request

url = input("Enter location: ")
  
print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieved", len(data), "charaters")
info = json.loads(data)

total = 0
count = 0
for item in info['comments']:
    total = total + item['count']
    count += 1
    
print("Count:", count)
print("Sum:", total)