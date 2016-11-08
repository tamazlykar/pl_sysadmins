import sys
import re

if len(sys.argv)  < 2:
	print("You should set path to the log file")
	sys.exit()

try:
    f = open(sys.argv[1], 'r')
except IOError:
    print("cannot open file " + sys.argv[1])
    sys.exit()

matchSubnet = re.findall(r'(?:(?:25[0-5]|[0-2]?\d\d?|2[0-4]\d)\.){3}(?:25[0-5]|[012]?\d\d?)', f.read(), flags=0)
f.close()

subnetsSet = set()

for subnet in matchSubnet:
    subnetsSet.add(subnet)

subnetsDict = {} 

for subnet in subnetsSet:
    ip = subnet
    while ip[len(ip)-1] != '.':
        ip = ip[0:-1]
    ip = ip[0:-1]
    if ip not in subnetsDict.keys():
        subnetsDict[ip] = []
    dl = subnetsDict[ip]
    dl.append(subnet)


f = open('result.txt', 'w')

f.write("In " + sys.argv[1] + " file was found " + str(len(subnetsSet)) + " in " + str(len(subnetsDict)) + " subnets\n\n") 
for subnet in subnetsDict:
    mylist = subnet
    f.write(subnet + " subnet" + "\n")
    for ip in subnetsDict[subnet]:
        f.write("\t" + ip + "\n")
    f.write("\n")

f.close()