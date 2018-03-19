f = open('/Users/koushikpenchikala/Desktop/Excer/ex_07/mbox-short.txt')
for line in f:
    line = line.rstrip()
    if not line.startswith ('From') :
        continue
    if len(line.split()) < 7 :
        continue
    Totallist = line.split()
    Email = Totallist[1]
    words = Email.split('@')
    print(words)



f = open('/Users/koushikpenchikala/Desktop/Excer/ex_07/mbox-short.txt')
for line in f:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])
