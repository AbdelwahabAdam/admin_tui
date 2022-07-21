    #!/usr/bin/env python
# encoding: utf-8


# The system here is an experimental one. See documentation for details.




#!/usr/bin/env python
# encoding: utf-8

# import npyscreen
# class TestApp(npyscreen.NPSApp):
#     def main(self):
#         Options = npyscreen.OptionList()

#         # just for convenience so we don't have to keep writing Options.options
#         options = Options.options

#         options.append(npyscreen.OptionFreeText('FreeText', value='',
#         documentation="This is some documentation."))
#         options.append(npyscreen.OptionMultiChoice('Multichoice',
#         choices=['Choice 1', 'Choice 2', 'Choice 3']))
#         options.append(npyscreen.OptionFilename('Filename', ))
#         options.append(npyscreen.OptionDate('Date', ))
#         options.append(npyscreen.OptionMultiFreeText('Multiline Text', value=''))
#         options.append(npyscreen.OptionMultiFreeList('Multiline List'))

#         try:
#             Options.reload_from_file('/tmp/test')
#         except FileNotFoundError:
#             pass
#         F = npyscreen.Form(name = "Welcome to Npyscreen",)

#         ms = F.add(npyscreen.OptionListDisplay, name="Option List",
#         values = options,
#         scroll_exit=True,
#         max_height=None)

#         F.edit()

#         Options.write_to_file('/tmp/test')

# if __name__ == "__main__":
#     App = TestApp()
#     App.run()

#!/usr/bin/env python
# encoding: utf-8
#!/usr/bin/env python
# encoding: utf-8

#!/usr/bin/env python
# encoding: utf-8
#!/usr/bin/env python
# encoding: utf-8
#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: npsapp.py
import json


with open('OpenID_client_data.json', 'r', encoding="utf-8") as f:
    dictdump = json.loads(f.read())

for item in dictdump:
    name, value = item , dictdump[item]
    line = str(name) + ':'+str(value)
    # print(line)
    print("***** *******************************")


# x = '''{
# "redirectUris":["line1,nline2,nline3,n"],
# "displayName":"hopa",
# "clientSecret":"secret key",
# "Filename":"G:\\GLUU\\admin_tui\\To_git\\OpenID client data to jans-config-api\\example data_req.txt",
# "Date":"Sat Jun 25 00:00:00 2022",
# "grantTypes":["line1,nline2,nline3"],
# }'''

# line = '"Date":"Sat Jun 25 00:00:00 2022",'
# name, value = line.split(":", maxsplit=1)
# print(name)
# print(value)
# for line in x.splitlines() :
    try :
        
        if '[' in line or ']' in line:
            name, value = line.split(":", maxsplit=1)
            name = name.replace('"','')
            value = value.replace(']','').replace('[','').replace(',',r"\n").replace('"','').replace(' ','').replace("'",'')
            if value[-1] == '\\':
                value = value[:-1]
            print(name + '=' + value) 
        else :
            if 'Date' in line :
                name, value = line.split(":", maxsplit=1)
                print(name)
                print(value)
                name = name.replace('"','')
                value = value.replace(']','').replace('[','').replace(',','').replace('"','')
                if value[-1] == '\\':
                    value = value[:-1]            
                print(name + '=' + value)   
            else :
                name, value = line.split(":", maxsplit=1)
                name = name.replace('"','')
                value = value.replace(']','').replace('[','').replace(',','').replace('"','')
                if value[-1] == '\\':
                    value = value[:-1]            
                print(name + '=' + value)   

    except:
        pass