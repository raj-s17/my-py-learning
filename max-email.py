name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mails = dict()

for line in handle:
    if not line.startswith('From '): 
        continue        
    words = line.split()
    li = words[1]
    
#    oldvalue = 0
#    if li in mails: oldvalue = mails[li]

    oldvalue = mails.get(li,0)
    mails[li] = oldvalue + 1

max_email = None
max_count = None

for email,count in mails.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count
    
print(max_email, max_count)
