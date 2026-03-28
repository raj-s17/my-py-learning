name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
dct = dict()

for line in handle:
    if not line.startswith('From '): 
        continue
        
    words = line.split()
    time = words[5]
    hour = time.split(':')[0]

    dct[hour] = dct.get(hour,0) + 1 
   
#lst = list()    
#for key,val in dct.items():
#    tup = (key, val)
#    lst.append(tup)
#lst = sorted(lst)
 
lst = sorted([ (k,v) for k,v in dct.items()])

for key,val in lst:
    print(key,val)