import sys

def read():
    names = []
    for line in sys.stdin.readlines():
        line.strip()
        #names.append(line[0:-1].split(','))
        names.append(line.rsplit(','))
        names[-1][2] = int(names[-1][2])
    
    print sorted(filter(lambda n: n[1]=='F',names),key=lambda n: n[2],reverse=True)[1]

read()
