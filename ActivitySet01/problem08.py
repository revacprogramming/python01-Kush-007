# Files

fname = input("Enter filename:")
if len(fname)==0:
    fname ="mbox-short.txt"
fh = open(fname)
count  =0
total =0
y =0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count= count +1
    num=float(line[21:])
    total=num+total
    y=total/count
    print("average spam confidence:",y)
