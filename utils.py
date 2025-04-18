import html
import string

valid_tags = {
    '<p>': '</p>',
    '<h>': '</h>',
    '<s>': '</s>',
    '<b>': '</b>',
    '<i>': '</i>',
    '<u>': '</u>',
    '<q>': '</q>',
}

class State:
    def __init__(self, name: str, outgoing: dict, type: int):
        self.name = name
        # defines the unique key of a state

        self.outgoing = outgoing
        # defines the outgoing arrows together with the input
        # format of the dictionary -> 'input' : 'what state it is going'

        self.type = type
        # defines the type of state
        # can be 'initial', 'final', 'normal'

def classify_chars(input_string):
    result = ""
    i = 0

    while i < len(input_string):
        c = input_string[i]

        # Handle special HTML entities like &amp;, &lt;, etc.
        if c == '&':
            semicolon_index = input_string.find(';', i)
            if semicolon_index != -1:
                entity = input_string[i:semicolon_index+1]
                if html.unescape(entity) != entity:
                    result += 'S'
                    i = semicolon_index + 1
                    continue

        # Classify character
        if c in string.ascii_letters:
            result += 'L'
        elif c in string.digits:
            result += 'N'
        elif c in string.whitespace:
            result += 'W'
        elif c in string.punctuation and c not in ['<', '>', '/', '?', '!']:
            result += 'P'
        elif ord(c) > 127: 
            result += 'U'
        else:
            result += c

        i += 1

    return result

def process_input_string(input_string):
    # handle 'h1'
    if input_string.find('h1'):
        # replace the string
        input_string = input_string.replace('h1', 'h')

    # handle opening tag
    opening = input_string[:3]
    # check if opening tag is in valid_tags
    if not opening in valid_tags.keys():
        return False

    # cut the opening tag
    input_string = input_string[3:]

    # handle closing tag
    closing = input_string[-4:]
    # check if closing tag is in valid_tags
    if not closing in valid_tags.values():
        return False
    
    # closing and opening must be the same
    if not opening[1] == closing[2]:
        return False 
    
    # cut the closing tag
    input_string = input_string[:-4]

    # contains the content of a tag: # tranforming content into (LE, NE, PE, WE, UE, SE)
    content = classify_chars(input_string)

    res = opening + content + closing

    return res