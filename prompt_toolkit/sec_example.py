
#--------------------------------------------------------------#
#------------------- prompt_toolkit ---------------------------#
#--------------------------------------------------------------#
#------------------- print_formatted_text ---------------------#
#--------------------------------------------------------------#
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit import print_formatted_text, ANSI
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit import print_formatted_text, HTML
print_formatted_text('simple prompt text')

#--------------------------------------------------------------#
#------------------- HTML TAGS - Font Type --------------------#
#--------------------------------------------------------------#
print_formatted_text(HTML('<b>This is bold</b>'))
print_formatted_text(HTML('<i>This is italic</i>'))
print_formatted_text(HTML('<u>This is underlined</u>'))
#--------------------------------------------------------------#
#------------------- HTML TAGS - Font Colors ------------------#
#--------------------------------------------------------------#
print_formatted_text(HTML('<ansired>This is red</ansired>'))
print_formatted_text(HTML('<ansigreen>This is green</ansigreen>'))
# Named colors (256 color palette, or true color, depending on the output).
print_formatted_text(HTML('<skyblue>This is sky blue</skyblue>'))
print_formatted_text(HTML('<seagreen>This is sea green</seagreen>'))
print_formatted_text(HTML('<violet>This is violet</violet>'))
#--------------------------------------------------------------#
#------------------- HTML TAGS - Font back color --------------#
#--------------------------------------------------------------#
print_formatted_text(
    HTML('<aaa fg="ansiwhite" bg="ansigreen">White on green</aaa>'))
#--------------------------------------------------------------#
#------------------- HTML TAGS - adding style sheet------------#
#--------------------------------------------------------------#
style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})
print_formatted_text(HTML('<aaa>Hello</aaa> <bbb>world</bbb>!'), style=style)
#--------------------------------------------------------------#
#------------------- ANSI for styling -------------------------#
#--------------------------------------------------------------#
print_formatted_text(ANSI('\x1b[31mhello \x1b[32mworld'))

#--------------------------------------------------------------#
#------------------- Tuple for styling ------------------------#
#--------------------------------------------------------------#
text = FormattedText([
    ('#ff0066', 'Hello'),
    ('', ' '),
    ('#44ff00 italic', 'World'),
])
print_formatted_text(text)
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#------------------- Take Input From User ---------------------#
#--------------------------------------------------------------#
text = prompt('Give me some input: ')
print('You said: %s' % text)
#--------------------------------------------------------------#
#------------------- Take Input From User Two Sessions---------#
#--------------------------------------------------------------#
# Create prompt object.
session = PromptSession()
# Do multiple input calls.
text1 = session.prompt()
text2 = session.prompt()

style = Style.from_dict({
    # User input (default text).
    '': '#ff0066',
    # Prompt.
    'username': '#884444',
    'at': '#00aa00',
    'colon': '#0000aa',
    'pound': '#00aa00',
    'host': '#00ffff bg:#444400',
    'path': 'ansicyan underline',
})
message = [
    ('class:username', 'Hopa'),
    ('class:at', '@'),
    ('class:host', 'localhost'),
    ('class:colon', ':'),
    ('class:path', '/user/hopa'),
    ('class:pound', '# '),
]
text = prompt(message, style=style)

#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#------------------- Autocompletion in prompt -----------------#
#--------------------------------------------------------------#

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>'])
text = prompt('Enter HTML: ', completer=html_completer)
print('You said: %s' % text)

#--------------------------------------------------------------#
#------------------- Nested completion in prompt --------------#
#--------------------------------------------------------------#
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
completer = NestedCompleter.from_nested_dict({
'show': {
'version': None,
'clock': None,
'ip': {
'interface': {'brief'}
}
},
'exit': None,})
text = prompt('# ', completer=completer)
print('You said: %s' % text)

#--------------------------------------------------------------#
#------------------- Cutom completion in prompt ---------------#
#--------------------------------------------------------------#
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion

class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
    # Display this completion, black on yellow.
        yield Completion('completion1', start_position=0,
        style='bg:ansiyellow fg:ansiblack')
        # Underline completion.
        yield Completion('completion2', start_position=1,
        style='underline')
        # Specify class name, which will be looked up in the style sheet.
        yield Completion('completion3', start_position=2,
        style='class:special-completion')

text = prompt('> ', completer=MyCustomCompleter())


#--------------------------------------------------------------#
#------------------- Input Validation -------------------------#
#--------------------------------------------------------------#

from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt
class NumberValidator(Validator):
    def validate(self, document):
        text = document.text
        if text and not text.isdigit():
            i = 0
            # Get index of first non numeric character.
            # We want to move the cursor here.
            for i, c in enumerate(text):
                if not c.isdigit():
                    break
            raise ValidationError(message='This input contains non-numeric characters',
            cursor_position=i)
number = int(prompt('Give a number: ', validator=NumberValidator()))
print('You said: %i' % number)
## can validate after enter key > not realtime >>> number = int(prompt(,,validate_while_typing=False))

#--------------------------------------------------------------#
#------------------- Input Validation from callback  ----------#
#------------------- Can be custom validation  ----------------#
#--------------------------------------------------------------#

from prompt_toolkit.validation import Validator
from prompt_toolkit import prompt


def is_numbera(text):
    return 'a' in text


validator = Validator.from_callable(
    is_numbera,
    error_message='This input contains non-numeric characters',
    move_cursor_to_end=True)

number = int(prompt('Give a number: ', validator=validator))
print('You said: %i' % number)
#--------------------------------------------------------------#
#------------------- History - IN Memory History --------------#
#--------------------------------------------------------------#

from prompt_toolkit import PromptSession
session = PromptSession()
while True:
    session.prompt()

#--------------------------------------------------------------#
#------------------- History - IN Memory History --------------#
#--------------------------------------------------------------#
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
session = PromptSession(history=FileHistory('./myhistory'))
while True:
    session.prompt()