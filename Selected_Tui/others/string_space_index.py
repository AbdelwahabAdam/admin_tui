

from requests import head


x="69574504-28f0-4e96-a0ec-fffdd0f26ea0     Support Portal     authorization_code     JWT"

data =['69574504-28f0-4e96-a0ec-fffdd0f26ea0', 'Support Portal',
                         'authorization_code', 'JWT']


headers=['Cliend ID', 'Client Name',
                         'Grant Type', 'Access Token']


for i in range(len(data)):
    print(x.find(data[i]))     

print(x)

y = ''
for k in range(len(headers)):
    y += headers[k] + ' '*(len(data[k]) - len(headers[k]) + 5)

print( y)                   