data1= ['69574504-28f0-4e96-a0ec-fffdd0f26ea0', 'Support portal','authorization_code', 'JWT']

data2 =['c64bc7a2-ff35-4166-8174-9436f74d4c38', 'Ecommerce Support Site','authorization_code', 'Reference']

data=[data1,data2]


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


# print((dict))
# for i in range(len(dict)) :
#     print(max(dict[i]))

# for i in range(len(data)):
#     for k in  range(len(data[i])):
#         print(data[i][k])
# spaces = []

# for i in dict :
#     spaces.append(max(dict[i]))

# for i in range(len(data)):
#     for k in  range(len(spaces)):
#         if len(data[i][k]) != spaces[k]:
#             print( spaces[k])
#             print(data[i][k])
#             print((spaces[k] -len(data[i][k]) ))
#             print(data[i][k] + "*"* (spaces[k] -len(data[i][k]) ))
#         else :
#             print(data[i][k])

headers=['Cliend ID', 'Client Name',  'Grant Type', 'Access Token']
print(max(headers, key=len))




#--------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------#
# class ListBox2():

#     def __init__(self, myparent, headers, data=None):
#         self.myparent = myparent
#         self.headers = headers
#         self.dialog_visible = False
#         self.selectes = 1
#         self.data = data

#         self.ClientID = TextArea(height=1, multiline=False)
#         self.ClientName = TextArea(height=1, multiline=False)
#         self.GrantType = TextArea(height=1, multiline=False)
#         self.AccessToken = TextArea(height=1, multiline=False)
#         self.Helper = TextArea(height=1, multiline=False, focusable=False)

#         if self.data == None:
#             self.data = [['No Cliend ID', 'No Client Name',
#                           'No Grant Type', 'No Access Token']]

#         self.dialog = Dialog(
#             title="Add New user",
#             body=HSplit(
#                 [
#                     VSplit([Label(text="Please type Client ID:", dont_extend_height=True),
#                             self.ClientID, ]),
#                     Window(height=1, char="."),
#                     VSplit([Label(text="Please type Client Name:", dont_extend_height=True),
#                             self.ClientName, ]),
#                     Window(height=1, char="."),
#                     VSplit([Label(text="Please type Grant Type:", dont_extend_height=True),
#                             self.GrantType, ]),
#                     Window(height=1, char="."),
#                     VSplit([Label(text="Please type Access Token:", dont_extend_height=True),
#                             self.AccessToken, ]),
#                     Window(height=1, char="."),
#                     self.Helper,

#                 ],
#                 padding=Dimension(preferred=1, max=1),
#             ),
#             buttons=[
#                 Button(
#                     text="OK",
#                     handler=self.save_dialog,
#                 ),
#                 Button(
#                     text="Cancel",
#                     handler=self.hide_dialog,
#                 ),
#             ],
#             with_background=True,
#             width=100,
#         )

#         self.container = FloatContainer(
#             content=HSplit([
#                 VSplit([
#                     self.getTitledText("Search:", name='displayName'),
#                     Button(text='Add Client', left_symbol='',
#                            right_symbol='', handler=partial(self.add_client))
#                 ]),
#                 Window(height=1),
#                 Window(height=1, char="."),
#                 Window(height=1),
#                 Window(
#                     content=FormattedTextControl(
#                         text=self._get_head_text,
#                         focusable=False,
#                         style='green',
#                     ),
#                     style="class:select-box",
#                     height=Dimension(preferred=1, max=1),
#                     cursorline=False,
#                 ),
#                 Window(height=1),
#                 Window(
#                     content=FormattedTextControl(
#                         text=self._get_formatted_text,
#                         focusable=True,
#                         key_bindings=self._get_key_bindings(),
#                         style='white',
#                     ),
#                     style="class:select-box",
#                     height=Dimension(preferred=5, max=5),
#                     cursorline=True,
#                     right_margins=[ScrollbarMargin(display_arrows=True), ],
#                 ),
#                 Window(height=10),



#             ]
#             ),
#             floats=[
#                 Float(
#                     ConditionalContainer(
#                         Shadow(self.dialog),
#                         filter=Condition(lambda: self.dialog_visible),

#                     )
#                 )
#             ],


#         )
# #--------------------------------------------------------------------------------------#
# #--------------------------------------------------------------------------------------#

#     def hide_dialog(self):
#         self.dialog_visible = False
#         get_app().layout.focus(self.container)

#     def save_dialog(self):

#         if self.ClientID.text and self.ClientName.text and self.GrantType.text and self.AccessToken.text:
#             if len(self.ClientID.text) == 36:
#                 x = []
#                 x.append(self.ClientID.text)
#                 x.append(self.ClientName.text)
#                 x.append(self.GrantType.text)
#                 x.append(self.AccessToken.text)

#                 self.data.append(x)
#                 self.dialog_visible = False
#                 get_app().layout.focus(self.container)
#             else:
#                 self.Helper.text = 'Please Insert valid Clined ID'
#         else:
#             self.Helper.text = 'Please Fill All fields'
# #--------------------------------------------------------------------------------------#
# #--------------------------------------------------------------------------------------#

#     def getTitledText(self, title, name, height=1):
#         multiline = height > 1
#         ta = TextArea(multiline=multiline)
#         ta.window.jans_name = name
#         return VSplit([Label(text=title, width=len(title)+1), ta], height=height)

#     def _get_head_text(self):
#         result = []
#         # result.append(self.heading)
#         # result.append("\n")
#         y = ''
#         for k in range(len(self.headers)):
#             y += self.headers[k] + ' ' * \
#                 (len(self.data[0][k]) - len(self.headers[k]) + 5)
#         result.append(y)
#         result.append("\n")

#         return merge_formatted_text(result)
# #--------------------------------------------------------------------------------------#
# #--------------------------------------------------------------------------------------#

#     def add_client(self):
#         self.dialog_visible = True
#         # event.app.layout.focus(self.dialog)
# #--------------------------------------------------------------------------------------#
# #--------------------------------------------------------------------------------------#

#     def _get_formatted_text(self):
#         result = []
#         for i, entry in enumerate(self.data):
#             if i == self.selectes:
#                 result.append([("[SetCursorPosition]", "")])
#             result.append('     '.join(entry))
#             result.append("\n")

#         return merge_formatted_text(result)
# #--------------------------------------------------------------------------------------#
# #--------------------------------------------------------------------------------------#

#     def _get_key_bindings(self):
#         kb = KeyBindings()

#         @kb.add("up")
#         def _go_up(event) -> None:
#             self.selectes = (self.selectes - 1) % len(self.data)

#         @kb.add("down")
#         def _go_up(event) -> None:
#             self.selectes = (self.selectes + 1) % len(self.data)

#         @kb.add("enter")
#         def _(event):

#             self.dialog_visible = True
#             event.app.layout.focus(self.dialog)

#         return kb

#     def __pt_container__(self):
#         return self.container

