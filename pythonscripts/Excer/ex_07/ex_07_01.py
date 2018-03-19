fh = open('mbox-short.txt','r')
for lx in fh:
    ly=lx.strip()
    print(ly.upper())
