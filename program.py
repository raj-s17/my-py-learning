# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
fsc = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    sep = line.find(':')
    sc = float(line[sep+1:].strip())
    count = count + 1
    fsc = float(fsc + sc)
asc = fsc/count
print("Average spam confidence:", asc)
