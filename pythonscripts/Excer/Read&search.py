f = open('/Users/koushikpenchikala/Readcsv.py','r')
for i in f:
    if i.startswith('with'):
        print(i)
