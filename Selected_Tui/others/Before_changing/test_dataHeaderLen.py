from re import I


headers=['Cliend ID', 'Client Name',
                         'Grant Type', 'Access Token']
                         

data=[
                    ['12345678', '1234567',
                     '123', '123456789'],
                    ['1234', '12345',
                     '123456789', '1234567'],
            
                ]


datalen = []
for dataline in range(len(data)) :
    line = []
    for i in  data[dataline]:
        line.append(len(i))
    datalen.append(line)
dict = {}
for num in range(len(datalen[0])) :
    dict[num] = []

for k in range(len(datalen)) :
    for i in range(len(datalen[k])):
        dict[i].append(datalen[k][i])

for i in dict :
    print(max(dict[i]))


