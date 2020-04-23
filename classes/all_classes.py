
class Drink:
    def __init__(self, drink_name, sugar_free, cat, id=None):  # drinks class, person and drink class needs to be seperate or it becomes more complex
        self.drink_name = drink_name
        self.sugar_free = sugar_free
        self.cat = cat
        self.id = id

class Round:
    def __init__(self, brewer, person_id=None, drink_id=None):
        self.brewer = brewer
        self.person_id = person_id
        self.drink = drink_id
        self.orders = {}

class Person:
    def __init__(self, first_name, last_name, age, person_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.person_id = person_id

    def get_person_info(self):
        if self.person_id != None:
            person_string = f"Name: {self.first_name} {self.last_name} Age: {self.age} ID: Set"
        else:
            person_string = f"Name: {self.first_name} {self.last_name} Age: {self.age} ID: None"
        return(person_string)