
#!/usr/bin/env python3
import curses
from email import message
import npyscreen

######################### Classes to inherit from ########################

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        # self.add_event_hander("event_inputbox_send", self.message_send)

        # window size
        y, x = self.useable_space()

        self.chatBoxObj = self.add(ChatBox, name="side nav", value=0, relx=1, max_width=x // 5, rely=2,
                                   max_height=-5)

        self.messageBoxObj = self.add(MessageBox, rely=2, relx=(x // 5) + 1, max_height=-5, editable=True,
                                      custom_highlighting=True, highlighting_arr_color_data=[0])

        self.FunctionalBox = self.add(FunctionalBox, name="Other", value=0, relx=1, max_width=x // 5,
                                      max_height=-5, )
        self.FunctionalBox.values = ["🕮  Othre"] 

        self.inputBoxObj = self.add(InputBox, name="Input", relx=(x // 5) + 1, rely=-7)
        new_handlers = {
            # exit

            # send message
            "^S": self.message_send,

        }
        self.add_handlers(new_handlers)
        self.messageBoxObj.update_messages(0)
        self.chatBoxObj.update_chat()

    # handling methods
    def message_send(self, event):
        current_user = self.chatBoxObj.value
        message = self.inputBoxObj.value.strip()
        if message != "":
            self.messageBoxObj.update_messages(current_user)

            self.inputBoxObj.value = ""
            self.inputBoxObj.display()
    ### y = 30
    ### x = 119
class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit
class FunctionalBox(npyscreen.BoxTitle):
    pass

class ChatBox(npyscreen.BoxTitle):

    def create(self, **kwargs):
        self.emoji = False



    def update_chat(self):
        current_user = self.value
        unread = 0

        color_new_message = self.parent.theme_manager.findPair(self, 'DANGER')
        color_online = self.parent.theme_manager.findPair(self, 'IMPORTANT')
        color_data = []

        data = []

        if unread != 0:
            self.parent.name = self.parent.app_name + " " + "[" + str(unread) + "]"
        else:
            self.parent.name = self.parent.app_name

        self.values = data
        self.entry_widget.custom_highlighting = True
        self.entry_widget.highlighting_arr_color_data = color_data

        # this event update all boxes
        # self.parent.parentApp.queue_event(npyscreen.Event("event_update_main_form"))


class MessageBox(npyscreen.BoxTitle):
    #### need to add handler on enter >> !
    # like a __init__
    def create(self, **kwargs):
        self.emoji = False
        self.aalib = False


    def when_value_edited(self):
        if self.value is not None:
            self.parent.parentApp.getForm("MESSAGE_INFO").update()
            self.parent.parentApp.switchForm("MESSAGE_INFO")

    def when_cursor_moved(self):
        self.parent.parentApp.queue_event(npyscreen.Event("event_messagebox_change_cursor"))
    def update_messages(self, current_user):
        messages = self.get_messages_info(current_user)

        color_data = []
        data = []
        for i in range(len(messages) - 1, -1, -1):
            # replace empty char
            messages[i].message = messages[i].message.replace(chr(8203), '')

            data.append(messages[i].name + " " + messages[i].message)
            color_data.append(messages[i].color)

        self.entry_widget.highlighting_arr_color_data = color_data

        self.values = data

        if len(messages) > self.height - 3:
            self.entry_widget.start_display_at = len(messages) - self.height + 3
        else:
            self.entry_widget.start_display_at = 0

        self.entry_widget.cursor_line = len(messages)

        self.name = "hopa"
        self.footer = "footer"
        
        self.display()

    def get_messages_info(self, current_user):
        messages = client.get_messages(current_user)

        # get user info
        users, dialog_type, max_name_len = self.get_user_info(messages, current_user)
        max_read_mess = client.dialogs[current_user].dialog.read_outbox_max_id

        # # check buffer
        # buff = self.buff_messages[current_user]
        # if buff is not None and messages is not None and \
        #         len(buff) != 0 and len(messages) != 0 and \
        #         len(messages) != len(buff) and \
        #         buff[0].id == messages[0].id and max_read_mess == self.buf_max_read_mess:
        #     return buff

        self.buf_max_read_mess = max_read_mess
        out = []
        for i in range(len(messages)):
            date = messages[i].date
            mess_id = messages[i].id

            if self.emoji:
                read = "⚫ " if max_read_mess < mess_id and messages[i].out else "  "
            else:
                read = "* " if max_read_mess < mess_id and messages[i].out else "  "

            # get name if message is forwarding
            prepare_forward_message = self.prepare_forward_messages(messages[i])

            # if chat or interlocutor
            if dialog_type == 1 or dialog_type == 2:
                user_name = users[messages[i].sender.id].name
                user_name = user_name if prepare_forward_message is False else prepare_forward_message
                if (len(user_name) != 0):
                    user_name = "hopa"
                else:
                    user_name = "Deleted Account"
                offset = " " * (max_name_len - (len(user_name)))
                name = read + user_name + ":" + offset
                color = (len(read) + len(user_name)) * [users[messages[i].sender.id].color]

            # if channel
            elif dialog_type == 3:
                user_name = client.dialogs[current_user].name
                user_name = user_name if prepare_forward_message is False else prepare_forward_message
                user_name = "hopa"

                name = user_name + ": "
                color = len(user_name) * [self.parent.theme_manager.findPair(self, 'WARNING')]

            else:
                name = ""
                color = [0]

            media = messages[i].media if hasattr(messages[i], 'media') else None
            mess = messages[i].message if hasattr(messages[i], 'message') \
                                          and isinstance(messages[i].message, str) else None

            image_name = ""
            if self.aalib and media is not None and hasattr(media, 'photo'):
                image_name = name
                name = len(name) * " "

            # add message to out []
            self.prepare_message(out, mess, name, read, mess_id, color, date)

            # add media to out []
            self.prepare_media(out, media, name, image_name, read, mess_id, color, date)

        # update buffer
        self.buff_messages[current_user] = out

        # return Message obj
        return out

   
    # structure for out message
    class Messages:
        def __init__(self, name, date, color, message, id, read):
            self.name = name
            self.date = date
            self.color = color
            self.message = message
            self.id = id
            self.read = read
class TelegramApi:
    client = None
    dialogs = []
    messages = []

    need_update_message = 0
    need_update_online = 0
    need_update_current_user = -1
    need_update_read_messages = 0

    def __init__(self):
        messages = ""

        return None


client = TelegramApi()


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="")


MyApp = App()
MyApp.run()


