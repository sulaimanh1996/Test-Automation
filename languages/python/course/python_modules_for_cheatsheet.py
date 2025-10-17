class character:
    def __init__(self, first_name, family_name, gender, race, class_character):
        self.first_name = first_name
        self.family_name = family_name
        self.gender = gender
        self.race = race
        self.class_character = class_character

    def first_greeting(self):
        print (F"Dear {self.gender} {self.first_name} {self.family_name}, you have chose as race {self.race} and your character class will be {self.class_character}")

character_1 = character(input("What is your first name? "), input("What is your family name? "), input("What is your gender? "), input("What is your race? "),input("What is your class? "))
character_1.first_greeting()