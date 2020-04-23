import menus.artwork as art
from persistence.database import Database
from persistence.database import db_drinks_save_list, db_people_save_list

### TO DO ###
# Fix the class imports and move them from database.py to their own module in own folder etc.
# Try to standaridze the DB lists, currently one is class one is tuple
# Unit test for everything
# Change the search/add/remove etc function such that it searches through SQL #
# upload SQL into a list, operate onto that list and every time it's appended or changed have a function ready to change it in sql!
# have the lists use instances of a class. #
# work onto their id numbers then #
### Write up a read me ###

class App():

    def __init__(self, db=None, csv=None):
        self.db = db
        self.csv = csv

    def show_menu_and_get_selection(self):
        # art.art()
        menu_text = """Welcome to Alex Brew(tm)
    
        Please, select an option below by entering a number:
        [1] Get all or search people 
        [2] Get all or search drinks
        [3] Add person to database
        [4] Add drink to database 
        [5] Delete person from database
        [6] Delete drink from database
        [7]
        [11] Exit
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
        elif selection == "7":
            self.selection_7()

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
        print(f"ID | FIRSTNAME | LASTNAME | AGE")
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
        print(f"\nDRINK | SUGAR FREE | CATEGORY | EXTRA")
        for drink in db_drinks_save_list:
            if drink.sugar_free == 1:
                sugar_free = "Sugar Free"
            else:
                sugar_free = "Full Fat"
            print(f"{drink.drink_name}, {sugar_free}, {drink.cat}, {drink.id}\n")
        self.selection_2()

    def selection_3(self):
        try:
            self.db.add_person_to_db()
        except Exception as error:
            print(f"Duplicate entry! {error}")
            self.main_menu()

    def selection_4(self): # need to fix like 3
        self.db.add_drink_to_db()
        self.main_menu()

    def selection_5(self):
        self.db.load_person()
        selection1b = str(input("Please enter the name or age you'd like to search for and delete:\n(Ex)it\n").capitalize())
        people_to_delete = []
        for person in db_people_save_list:
            if selection1b in (person.first_name, person.last_name, person.age):
                people_to_delete.append(person.person_id)
            elif selection1b == "Ex":
                self.main_menu()
            else:
                continue
        return(people_to_delete)
        print
        selection_5a()

    def selection_5a(self):
        people_to_delete = self.selection_5()
        try:
            self.db.delete_from_people_db(people_to_delete)
        except Exception as error:
            print(f"{error}")
            self.main_menu()
        print("The following entries were deleted:")
        for person in people_to_delete:
            print(f"{person.first_name}")

    def selection_6(self):
        db.get_connection()
        db.load("drinks")
        selection1 = input("Please enter the name and/or age of the person(s) you wish to delete:\n(E)xit\n")
        for drinks_tuple in db_drinks_list:
            drink_name, sugar_free, cat = drinks_tuple
            if selection1 in drinks_tuple:
                print(f"{drink_name} {sugar_free} {cat}")  # need to fix this bit
                db.delete_from_people_db(drink_name, sugar_free, cat)
                db_drinks_list.remove(drinks_tuple)
            elif selection1 == "Ex":
                self.main_menu()
            else:
                continue

if __name__ == '__main__':

    app = App(db=Database())
    app.main_menu()







