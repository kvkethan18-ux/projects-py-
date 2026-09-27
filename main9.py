from abc import ABC, abstractmethod

class instument(ABC):
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
        print(f"instrument name: {self.name}")
        print(f"instrument category {self.category}")

    @abstractmethod
    def play_sound(self):
        pass

class Guitar(instument):
    def __init__(self, name, category, strings):
        super().__init__(name, category)
        self.strings = strings

    def play_sound(self):
        print(f"{self.name} has {self.strings} strings & sounds like Strum Strum!")

class Drum(instument):
    def __init__(self, name, category, company):
        super().__init__(name, category)
        self.company = company

    def play_sound(self):
        print(f"{self.name} is a {self.name} made by {self.company} & sounds like: Boom Boom!")

class flute(instument):
    def __init__(self, name, category, material):
        super().__init__(name, category)
        self.material = material

    def play_sound(self):
        print(f"{self.name} is made up of {self.material} and sounds like: Toot Toot!")

instument_1 = Guitar("Electric guitar", "String Instrument", 6)
instrument_2 = Drum("Drum", "Precussion Instrument", "Donner")
instument_3 = flute("Flute", "Wind Instrument", "Bamboo")

print("===== Music Instrument Sound Show =====")
print("By: Kethan")
print("=====================================================================================")
instument_1.display_info()
instument_1.play_sound()
print("=====================================================================================")
instrument_2.display_info()
instrument_2.play_sound()
print("======================================================================================")
instument_3.display_info()
instument_3.play_sound()