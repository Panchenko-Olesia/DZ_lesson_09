import string
class TextProcessor:
    def __init__(self, my_str):
        self.my_str = my_str
        self.__znak_punkt = ""
    def get_clean_string(self):
        for i in self.my_str:
            if i in string.punctuation:
                self.__znak_punkt = self.__znak_punkt + i
                self.my_str = self.my_str.replace(i,'')
        print(self.my_str)
    def in_puktiation(self):
        if len(self.__znak_punkt) != 0:
            return True
        else:
            return False

my_test_str = TextProcessor('vd%#nshku3+- gsfd/qao')
my_test_str.get_clean_string()