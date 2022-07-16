from turtle import color
import npyscreen
import os
import json
########################################################################################
######################################  Dumy Form 3 ####################################
class Form3(npyscreen.ActionForm):
    def create(self):
        self.add_handlers({"^T": self.change_forms})
        y, x = self.useable_space()
        ####################   Title of the screen      
        self.Title = self.add(npyscreen.TitleText, name="Janssen admin 3", value=None, editable = None)       

    def on_ok(self):
        self.parentApp.switchForm(None)

    def change_forms(self, *args, **keywords):

        if self.name == "Navigate 1":
            change_to = "SECOND"
        elif self.name == "Navigate 2":
            change_to = "THIRD"
        else:
            change_to = "MAIN"

        self.parentApp.change_form(change_to)
########################################################################################
######################################  Dumy Form 2 ####################################

class Form2(npyscreen.ActionForm):
    def create(self):
        self.add_handlers({"^T": self.change_forms})
        y, x = self.useable_space()
        ####################   Title of the screen      
        self.Title = self.add(npyscreen.TitleText, name="Janssen admin 2", value=None, editable = None)       

    def on_ok(self):
        self.parentApp.switchForm(None)

    def change_forms(self, *args, **keywords):

        if self.name == "Navigate 1":
            change_to = "SECOND"
        elif self.name == "Navigate 2":
            change_to = "THIRD"
        else:
            change_to = "MAIN"

        self.parentApp.change_form(change_to)
### y = 30
##############  Overwrite on the options class to write and read cutom  ################
class Options_ov(npyscreen.OptionList):
    def __init__(self, filename=None):
        super().__init__(filename)

############################  OverWrite to Write json ######################################
    def write_to_file(self, fn=None, exclude_defaults=True):
        ### will be passed to class 
        varWithList = ['redirectUris','grantTypes']
        dict = {}
        fn = fn or self.filename
        if not fn:
            raise ValueError("Must specify a filename.")

        for opt in self.options:
            dict[opt.get_real_name()] = self.serialize_option_value(opt)

        with open(fn, 'w', encoding="utf-8") as f:
            json.dump(dict, f)   
            
 ###########################  OverWrite to Read json ######################################
    def reload_from_file(self, fn=None):
        ### will be passed to class 

        fn = fn or self.filename
        try:
            with open(fn, 'r', encoding="utf-8") as f:
                dictdump = json.loads(f.read())

            for item in dictdump:
                name, value = item , dictdump[item]
                line = str(name) + ':'+str(value)
                name, value = line.split(":", maxsplit=1)
                if '[' in line or ']' in value:
                    name = name.replace('"','')
                    value = value.replace(']','').replace('[','').replace(',',r"\n").replace('"','').replace(' ','').replace("'",'')
                    if value[-1] == '\\':
                        value = value[:-1]
                    print(name + '=' + value) 
                    for option in self.options:
                        if option.get_real_name() == name:
                            option.set(self.deserialize_option_value(option, value.encode('ascii')))
                else :
                    name, value = line.split(":", maxsplit=1)
                    name = name.replace('"','')
                    value = value.replace(']','').replace('[','').replace(',','').replace('"','')
                    if value[-1] == '\\':
                        value = value[:-1]            
                    print(name + '=' + value)   
                    for option in self.options:
                        if option.get_real_name() == name:
                            option.set(self.deserialize_option_value(option, value.encode('ascii')))  

        except:
            npyscreen.notify_ok_cancel(
            "No Previous Data found!", title="Opps!", wrap=True, editw=1)
            pass
########################################################################################
class MainApp(npyscreen.ActionForm):

    def create (self):
        self.add_handlers({"^T": self.change_forms})
        self.Title = self.add(npyscreen.TitleText, name="Janssen admin 1", value=None, editable = None,color='CAUTION')       
        self.Options = Options_ov()
        # just for convenience so we don't have to keep writing Options.options
        options = self.Options.options
        options.append(npyscreen.OptionMultiFreeText('redirectUris', value=''))
        options.append(npyscreen.OptionFreeText('displayName', value=''))
        options.append(npyscreen.OptionFreeText('clientSecret', value=''))
        options.append(npyscreen.OptionMultiFreeText('grantTypes', value=''))
        options.append(npyscreen.OptionDate('Date', ))
        options.append(npyscreen.OptionFilename('Filename', ))
        try:
            self.Options.reload_from_file('./OpenID_client_data.json')
        except FileNotFoundError:
            pass        
        
        self.add(npyscreen.OptionListDisplay, name="Option List", 
                values = options, 
                scroll_exit=True,
                max_height=None,color='GREEN_BLACK')

    def on_cancel(self):
        pass
    
    def on_ok(self):
        self.Options.write_to_file('./OpenID_client_data.json')
        npyscreen.notify_ok_cancel(
            "Values Has been saved!", title="Woot!", wrap=True, editw=1)

    def change_forms(self, *args, **keywords):

        if self.name == "Navigate 1":
            self.Options.write_to_file('./OpenID_client_data.json')
            npyscreen.notify_ok_cancel(
            "Values Has been saved!", title="Woot!", wrap=True, editw=1)
            change_to = "SECOND"
        elif self.name == "Navigate 2":
            change_to = "THIRD"
        else:
            change_to = "MAIN"

        self.parentApp.change_form(change_to)
############################### All Forms in the App ###########################################
#### I added 3 form just to try the switch
class MainAllForms(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN",       MainApp, name="Navigate 1", color="CAUTION")
        self.addForm("SECOND",     Form2, name="Navigate 2", color="GOODHL",  )
        self.addForm("THIRD", Form3, name="Navigate 3", color="CAUTION",)
        
    def onCleanExit(self):
        npyscreen.notify_wait("Data Saved \n \t goodbye!")
    
    def change_form(self, name):
        self.switchForm(name)     
        self.resetHistory()

MyApp = MainAllForms()
MyApp.run()