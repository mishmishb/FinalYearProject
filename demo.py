import logging
import re
import sys

logging.basicConfig(
    filename='test.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

co = logging.StreamHandler()
co.setLevel(logging.INFO)
logging_def = logging.getLogger('default')
logging_def.addHandler(co)


class Analyser:
    def __init__(self, pass_string, looking_for):
        self.pass_string = pass_string
        self.looking_for = looking_for

    def character_type(self):
        if self.looking_for == 'l':
            return 'letter'
        elif self.looking_for == 'n':
            return 'number'
        elif self.looking_for == 's':
            return 'symbol'

    def find_characters(self):
        if self.looking_for == 'l':
            character_list = []
            for i in list(self.pass_string):
                if i.isalpha():
                    character_list.extend(i)
            return character_list
        elif self.looking_for == 'n':
            number_list = []
            for i in list(self.pass_string):
                if i.isdigit():
                    number_list.extend(i)
            return number_list
        elif self.looking_for == 's':
            symbol_list = []
            for i in list(self.pass_string):
                if not (i.isalpha() or i.isdigit()):
                    symbol_list.extend(i)
            return symbol_list

    def find_position(self):
        if self.looking_for == 'l':
            return [(str(i + 1), char) for i, char in enumerate(self.pass_string)
            if char.isalpha()]
        elif self.looking_for == 'n':
            return [(str(i + 1), num) for i, num in enumerate(self.pass_string)
            if num.isdigit()]
        elif self.looking_for == 's':
            return [(str(i + 1), sym) for i, sym in enumerate(self.pass_string)
            if not (sym.isalpha() or sym.isdigit())]


def input_func():
    raw_input = input('Input: ')
    for i in list(raw_input):
        if i == ' ':
            print("Passwords must not contain spaces")
            input_func()
    return raw_input


def main():

    password = input_func()

    analyser_letters = Analyser(password, 'l')
    analyser_numbers = Analyser(password, 'n')
    analyser_symbols = Analyser(password, 's')

    logging_def.info(f'The length of \'{password}\' is {len(password)}')
    logging_def.info(f'As a list it looks like this {list(password)}')

    for i in (analyser_letters, analyser_numbers, analyser_symbols):
        if i.find_characters():
            logging_def.info(f'The {i.character_type()}s in this password are: '
            f'{i.find_characters()}')
            for j in i.find_position():
                ordinal_indicator = list(j[0])[-1]
                if ordinal_indicator == '1':
                    logging_def.info(f'The \'{j[1]}\' was the 1st character')
                elif ordinal_indicator == '2':
                    logging_def.info(f'The \'{j[1]}\' was the 2nd character')
                elif ordinal_indicator == '3':
                    logging_def.info(f'The \'{j[1]}\' was the 3rd character')
                else:
                    logging_def.info(f'The \'{j[1]}\' was the {j[0]}th character')
            logging_def.info('\n')
        else:
            logging_def.info(f'There are no {i.character_type()}s in this password')


if __name__ == "__main__":
    main()
