#ofile = input('Enter a file name: ')
dfile = open('mbox-short.txt')

date = dict()
largest = None
minimum = None

for line in dfile:
    if line.startswith('From '):
        try:
            words = line.rstrip().split()
            time = words[5].split(':')
            for stime in time[:1]:
                date[stime] = date.get(stime,0) +1
        except IndexError:
            pass

lit = list()

for k,v in list(date.items()):
    lit.append((k,v))

lit.sort()

for k,v in lit:
    print(k,v)