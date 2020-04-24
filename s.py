import menus.artwork as art
from persistence.database import Database
from persistence.database import db_drinks_save_list, db_people_save_list
import os
from classes.all_classes import Drink, Person



class App():

    def __init__(self, db=None, csv=None):
        self.db = db
        self.csv = csv

    def show_menu_and_get_selection(self):
       # art.art()
       os.system('clear')
       menu_text = """\n                                           Welcome to Alex Brewᵀᴹ
    
                            Please, select an option below by entering a number:
                            
                            [1] Get all or search people 
                            [2] Get all or search drinks
                            [3] Add person to database
                            [4] Add drink to database 
                            [5] Delete person from database
                            [6] Delete drink from database
                            [Ex] Exit
        """
       print(menu_text)

    def main_menu(self):
        self.show_menu_and_get_selection()
        selection = input("Input a search number:\n")
        if selection == "1": # need to condense the search function
            self.selection_1()
        elif selection == "2":
            self.selection_2()
        elif selection == "3":
            self.selection_3()
        elif selection =="4":
            self.selection_4()
        elif selection =="5":
            self.selection_5()
        elif selection == "6":
            self.selection_6()
        elif selection == "Ex":
            exit()

    def selection_1(self):
        self.db.load_person()
        selection1a = input("Would you like to search for a person or return all people?\n(S)earch\n(A)ll\n(Ex)it\n")
        if selection1a.lower() == "s":
            self.selection_1a()
        elif selection1a.lower() == "ex":
            self.main_menu()
        else:
            self.selection_1b()

    def selection_1a(self): # search people list
        selection1b = str(input("Please enter the name or age you'd like to search for or exit:\n(Ex)it\n").capitalize())
        for person in db_people_save_list:
            if selection1b in (person.first_name, person.last_name, person.age):
                print(f"{person.first_name} {person.last_name} {person.age}")
            elif selection1b == "Ex":
                self.main_menu()
            else:
                continue
        self.selection_1a()

    def selection_1b(self): # print entire people list
        print(f"ID, FIRSTNAME, LASTNAME , AGE")
        for person in db_people_save_list:
            print(f"{person.person_id} {person.first_name} {person.last_name} {person.age}")
        self.selection_1()

    def selection_2(self):
        self.db.load_drinks()
        selection1a = input("Would you like to search for a drink or return all drinks?\n(S)earch\n(A)ll\n(Ex)it\n")
        if selection1a.lower() == "s":
            self.selection_2a()
        elif selection1a.lower() == "ex":
            self.main_menu()
        else:
            self.selection_2b()

    def selection_2a(self): # Drinks searcher
        selection1b = input("Please enter the drink you'd like to search for:\n").capitalize()
        for drink in db_drinks_save_list:
            if selection1b in (drink.drink_name):
                print(f"Drink: {drink.drink_name} Sugar Free: {drink.sugar_free} Category: {drink.cat}")  # need to fix this bit
            elif selection1b == "Ex":
                self.main_menu()
            else:
                continue
        self.selection_2()

    def selection_2b(self): # all drinks
        print(f"\nDRINK, SUGAR FREE/REDUCED, CATEGORY")
        for drink in db_drinks_save_list:
            print(f"{drink.drink_name}, {drink.sugar_free}, {drink.cat}, {drink.id}")
        self.selection_2()

    def selection_3(self):
        selection2 = input("Please enter their firstname:\n(Ex)it\n")
        if selection2.lower() == "ex":
            self.main_menu()
        selection3 = input("Please enter their lastname:\n")
        selection4 = input("Please enter their age:\n")
        new_person = Person(selection2, selection3, selection4)
        self.selection_3a(new_person)
        return (new_person)

    def selection_3a(self, new_person):
        try:
            self.db.add_person_to_db(new_person)
            self.selection_3()
        except Exception as error:
            print(f"Duplicate entry!\nTechnical things: {error}")
            self.selection_3()

    def selection_4(self):
        selection2 = input("Please enter the drink name:\n(Ex)it\n")
        if selection2.lower() == "ex":
            self.main_menu()
        selection4 = input("Is the drink sugar free or reduced sugar?:\n(Y)es\n(N)o\n")
        if selection4.lower() == "y":
            selection4 = 0
        else:
            selection4 = 1
        selection5 = input("Please enter the drink catergory:\n(A)lcoholic\n(S)oft Drink\n(H)ot Drink\n")
        if selection5.lower() == "a":
            selection5 = "Alcoholic"
        elif selection5.lower() == "s":
            selection5 = "Soft Drink"
        else:
            selection5 = "Hot Drink"
        new_drink = Drink(selection2, selection4, selection5)
        self.selection_4a(new_drink)
        return(new_drink)

    def selection_4a(self, drink_object):
        try:
            self.db.add_drink_to_db(drink_object)
            self.selection_4()
        except Exception as error:
            print(f"Duplicate entry!\n Technical things: {error}")
            self.selection_4()

    def selection_5(self):
        self.db.load_person()
        selection1b = str(input("Please enter the name or age you'd like to search for and delete:\n(Ex)it\n").capitalize())
        people_delete_list = []
        for person in db_people_save_list:
            if selection1b == person.first_name:
                people_delete_list.append(person)
            elif selection1b == "Ex":
                self.main_menu()
            else:
                continue
        print(people_delete_list)
        self.selection_5a(people_delete_list)

    def selection_5a(self, people_to_delete):
        try:
            self.db.delete_from_people_db(people_to_delete)
        except Exception as error:
            print(f"{error}")
            self.main_menu()
        print("The following entries were deleted:")
        for person in people_to_delete:
            print(f"{person.first_name} {person.last_name}")
        self.selection_5()
        return(people_to_delete)

    def selection_6(self):
        self.db.load_drinks()
        selection1b = input("Please enter the drink you wish to delete:\n(E)xit\n")
        drinks_delete_list = []
        for drink in db_drinks_save_list:
            if selection1b == drink.drink_name:
                drinks_delete_list.append(drink)
            elif selection1b == "Ex":
                self.main_menu()
            else:
                continue
        self.selection_6a(drinks_delete_list)

    def selection_6a(self, drinks_to_delete):
        try:
            self.db.delete_from_drinks_db(drinks_to_delete)
        except Exception as error:
            print(f"{error}")
            self.main_menu()
        print("The following entries were deleted:")
        for drink in drinks_to_delete:
            print(f"{drink.drink_name} was deleted!")
        self.selection_6()
        return (drinks_to_delete)


if __name__ == '__main__':

    app = App(db=Database())
    app.main_menu()







