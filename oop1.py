import string as s

class Alphabet:
    
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)
        
    def print(self):
    	print(self.letters)
	    
    def letters_num(self):
        return len(self.letters)
    
class EngAlphabet(Alphabet):
    
    default_lang = 'En'
    default_letters = s.ascii_uppercase
    __letters_num = len(default_letters)
    
    def __init__(self):
        super().__init__(EngAlphabet.default_lang, EngAlphabet.default_letters)
	
    def is_en_letter(self, letter):
	
        return letter.upper() in self.letters
    
    def letters_num(self):
	
        return EngAlphabet.__letters_num
    
    @staticmethod
    def example():
        print('English Example:\nTo be or ot to be?! What is the question?')
    
if __name__ == '__main__':    
    eng = EngAlphabet()
    eng.print()
    print(eng.letters_num())
    print(eng.is_en_letter('F'))
    print(eng.is_en_letter('Щ'))
    eng.example()
    
    