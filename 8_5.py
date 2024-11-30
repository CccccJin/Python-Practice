fname = input('Enter the file name: ')
fhand = open(fname)

count = 0

for line in fhand:
    if line.startswith('From:'):
        list = line.split()
        count += 1
        account = list[1:4]
        pure_account = account[0].strip("[]")
        print(pure_account)

print('There were',count,'lines in the file with From as the first word')

