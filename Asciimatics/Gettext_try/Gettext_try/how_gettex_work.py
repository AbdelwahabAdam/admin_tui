global LANGUAGE


def _(s):
    spanishStrings = {'Hello world!': 'Hola Mundo!'}
    frenchStrings = {'Hello world!': 'Bonjour le monde!'}
    germanStrings = {'Hello world!': 'Hallo Welt!'}

    if LANGUAGE == 'English':
        return s
    if LANGUAGE == 'Spanish':
        return spanishStrings[s]
    if LANGUAGE == 'French':
        return frenchStrings[s]
    if LANGUAGE == 'German':
        return germanStrings[s]


LANGUAGE = 'English'
print('Hello world!')

LANGUAGE = 'Spanish'
print(_('Hello world!'))
