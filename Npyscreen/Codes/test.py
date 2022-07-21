import npyscreen

data = [['9', '000008', 'Allagor, Joseph Kyle', '11', '5', '3431', '21I', 'Algebra 1A', 'Some Notes'] , ]


class CustomButton(npyscreen.CheckboxBare):
    def __init__(self, parent, passedvalue = None, title = None,*args, ** keywords):
        super(CustomButton, self).__init__(parent, *args, ** keywords)
        self.target = passedvalue
        self.title = title

    def whenToggled(self):
        if self.target:
            if self.value:
                self.title.value = str(self.title.value) + str('1')

                self.target.value = int(self.target.value) - 3
                
            else :
                self.target.value = int(self.target.value) + 3
            self.target.display()

def Display( *args):
    F = npyscreen.Form(name = "Daily Entry")
    F.add(npyscreen.TitleText, name = "Name       Daily Points     Tardy/Absent  Phone   Behavior      Notes", editable = False, max_width = 20 )
    points = F.add(npyscreen.TitleText, name = ' ', relx = 20, rely = 5, value = '10', editable = False)
    Title = F.add(npyscreen.TitleText, name="Jassan admin", value=None, editable = None)
    absTar = F.add(CustomButton, relx = 50, rely = 5, scroll_exit = True, name = 'attendance' , value = False, passedvalue = points ,title = Title)
    phone  = F.add(CustomButton, relx = 60, rely = 5, scroll_exit = True, name = 'phone'      , value = False, passedvalue = points ,title = Title)
    dist   = F.add(CustomButton, relx = 70, rely = 5, scroll_exit = True, name = 'distraction', value = False, passedvalue = points ,title = Title)
    notes  = F.add(npyscreen.TitleText, relx = 77, rely = 5, scroll_exit = True, name = ' '   , value = data[0][8] )
    points.entry_widget.ENSURE_STRING_VALUE = False
    F.edit()

if __name__ == '__main__':
    print(npyscreen.wrapper_basic(Display))

# #!/usr/bin/env python

# import yaml
# import json
# data = {}
# with open("jans-config-api-swagger.json", "r") as stream:
#     try:
#         data = yaml.safe_load(stream)
#         print(yaml.safe_load(stream))
#     except yaml.YAMLError as exc:
#         print(exc)
# print(data['jwks'])