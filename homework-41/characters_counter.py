from pathlib import Path

'''
DOTAZY:
- porad se opakuje volani funkce open_file(), neda se nejak vyresit, optimalizovat?
'''


class CharCounter():
    def __init__(self, file):
        self.input_file = file

    
    def open_file(self):
        with open(self.input_file, mode='r', encoding='utf-8') as file:
            return file.read()
    

    def get_number_of_letter(self, chosen_letter, text):
        number_of_chosen_letters = text.count(chosen_letter)
        return number_of_chosen_letters
    

    def get_number_of_spaces(self):
        text = self.open_file()
        number_of_spaces = text.count(' ')
        return number_of_spaces
    

    def get_dict_info(self):
        text = self.open_file()
        detailed_info = {}

        for letter in text:
            if letter not in detailed_info.keys():
                detailed_info.update({letter: 0})

        for key in detailed_info.keys():
            number_of_character = text.count(key)
            detailed_info.update({key: number_of_character})

        return detailed_info
    

    def get_number_of_numbers(self):
        dict_info = self.get_dict_info()
        number_of_numbers = 0

        for key in dict_info.keys():
            if key.isdigit():
                number_of_numbers += dict_info[key]
        
        return number_of_numbers
    
    
    def get_number_of_all_letters(self):
        dict_info = self.get_dict_info()
        number_of_letters = 0
    
        for key in dict_info.keys():
            if key.isalpha():
                number_of_letters += dict_info[key]
        
        return number_of_letters


    def print_info(self):
        dict_info = self.get_dict_info()
        digits = self.get_number_of_numbers()
        total_characters = len(self.open_file())
        spaces = dict_info[' ']
        new_lines = dict_info['\n']
        letters = self.get_number_of_all_letters()

        message = f'''
The text contains a total of {total_characters} characters.
Of that, {spaces} are spaces and {new_lines} are new lines.
There are {digits} numerals in total, and {letters} letters.
'''
        print(message)




if __name__ == '__main__':
    my_txt_file = r'/Users/vbrothanek/Documents/some-file.txt'
    file = CharCounter(my_txt_file)
    file.print_info()