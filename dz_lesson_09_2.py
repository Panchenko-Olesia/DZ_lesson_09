import string
class TextProcessor:
    # змінні: передається строка my_str, znak_punkt - змінна в яку будуть складатись усі знаки пунктуаціі
    def __init__(self, my_str):
        self.my_str = my_str
        self.znak_punkt = ""
    def get_clean_string(self):
        for i in self.my_str:
            if i in string.punctuation:
                self.znak_punkt = self.znak_punkt + i
                self.my_str = self.my_str.replace(i,'')
        return self.my_str

    def __in_puktiation(self):
        if len(self.znak_punkt) != 0:
            return True
        else:
            return False
    # Метод нижче для виводу результату попреднього прихованого методу
    def get_print(self):
        return self.__in_puktiation()
class TextLoader(TextProcessor):
    def __init__(self,text_processor):
        self.__text_processor = TextProcessor(text_processor)
        self.__clean_string = ""
    @property
    def set_clean_string(self):
        self.__clean_string = self.__text_processor.get_clean_string()
        print(f"Очищена строка: {self.__clean_string}")

# Для перешої та другоі частини завдання:
my_test_str = TextProcessor('vd%#nshku3+- gsfd/qao')

# Закоментований рядок нижче для перевірки False, якщо у рядку немає символів
#my_test_str = TextProcessor('vdnshku3 gsfdqao')
print(my_test_str.get_clean_string())
print(my_test_str.get_print())

# Для третьої частини завдання:
my_test_str_2 = TextLoader('woru&^hvsud) hf')
my_test_str_2.set_clean_string
