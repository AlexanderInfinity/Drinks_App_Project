import menus.artwork as art
from persistence.database import Database
from persistence.database import db_drinks_save_list, db_people_save_list
import os
from classes.all_classes import Drink, Person
import datetime
import csv


class App():

    def __init__(self, db=None, csv=None):
        self.db = db
        self.csv = csv

    def show_menu_and_get_selection(self):
       os.system('clear')
       menu_text = """\n                                           Welcome to AlexBrewᵀᴹ
    
                            Please, select an option below by entering a number:
                            
                            [1] Get all or search people 
                            [2] Get all or search drinks
                            [3] Add person to database
                            [4] Add drink to database 
                            [5] Delete person from database
                            [6] Delete drink from database
                            [7] Round Creatorᵀᴹ
                            [8] Get all or search rounds 
                            [Ex] Exit
        """
       print(menu_text)

    def main_menu(self):
        self.show_menu_and_get_selection()
        selection = input("Input a search number:\n")
        if selection == "1": # need to condense the search function
            self.selection_1c()
        elif selection == "2":
            self.selection_2c()
        elif selection == "3":
            self.selection_3()
        elif selection =="4":
            self.selection_4b_drink_input_getter()
        elif selection =="5":
            self.selection_5()
        elif selection == "6":
            self.selection_6()
        elif selection == "7":
            self.selection_7c_round_builder()
        elif selection == "8":
            self.selection_8_input()
        elif selection.lower() == "ex":
            exit()

    def selection_1c(self):
        print("                   Person Searcher")
        selection1a = input("Would you like to search for a person or return all people?\n(S)earch\n(A)ll\n(Ex)it\n")
        self.selection_1(selection1a)

    def selection_1(self, selection1a):
        person_list = self.db.load_person()
        if selection1a.lower() == "s":
            selection1b = input("Please enter the name or age you'd like to search for or exit:\n(Ex)it\n").title()
            self.selection_1a(selection1b, person_list)
            return(person_list)
        elif selection1a.lower() == "a":
            self.selection_1b(person_list)
        else:
            self.main_menu()

    def selection_1a(self, selection1b, person_list): # search people list
        print(f"+=========================+")
        print(f"Firstname | Lastname | Age")
        print(f"+=========================+")
        for person in person_list: #### NEED TO FIX SEARCH FUNCTION ###
            if selection1b in person.first_name + " " + person.last_name:
                print(f"{person.first_name} {person.last_name} {person.age}")
            elif selection1b == str(person.age):
                print(f"{person.first_name} {person.last_name} {person.age}")
            elif selection1b == person.first_name + " " + str(person.age):
                print(f"{person.first_name} {person.last_name} {person.age}")
            elif selection1b == person.last_name + " " + str(person.age):
                print(f"{person.first_name} {person.last_name} {person.age}")
            elif selection1b == str(person.age):
                print(f"{person.first_name} {person.last_name} {person.age}")
            elif selection1b == person.first_name + " " + person.last_name + " " + str(person.age):
                print(f"{person.first_name} {person.last_name} {person.age}")
            elif selection1b == "Ex":
                self.main_menu()
                return
            else:
                continue
        print(f"")
        self.selection_1c()
        return (f"{person.first_name} {person.last_name} {person.age}")

    def selection_1b(self, person_list): # print entire people list
        for person in person_list:
            print(f"{person.first_name} {person.last_name} {person.age}")
        print(f"")
        self.selection_1c()  ### NEED TO FIX, DOESNT REACH THIS, BUT RETURN IS FOR TEST ###
        return(f"{person.person_id} {person.first_name} {person.last_name} {person.age}")
        self.show_menu_and_get_selection()  ### NEED TO FIX, DOESNT REACH THIS, BUT RETURN IS FOR TEST ###

    def selection_2c(self):
        print("                   Drink Searcher")
        selection1a = input("Would you like to search for a drink or return all drinks?\n(S)earch\n(A)ll\n(Ex)it\n")
        self.selection_2(selection1a)

    def selection_2(self, selection1a):
        drinks_list = self.db.load_drinks()
        if selection1a.lower() == "s":
            selection1b = input("Please enter the drink you'd like to search for:\n").title()
            self.selection_2a(selection1b, drinks_list)
        elif selection1a.lower() == "a":
            self.selection_2b(drinks_list)
        else:
            self.main_menu()

    def selection_2a(self, selection1b, drinks_list): # Drinks searcher
        print(f"+================================================+")
        print(f"Drink | Sugar Free or Reduced Sugar | Catergory")
        print(f"+================================================+")
        for drink in drinks_list:
            if selection1b in drink.drink_name:
                if drink.sugar_free == 1:
                    drink.sugar_free = "Reduced/No Sugar"
                else:
                    drink.sugar_free = "Full Sugar"
                print(f"{drink.drink_name}, {drink.sugar_free}, {drink.cat}")  # need to fix this bit
            elif selection1b == "Ex":
                self.main_menu()
                return
            else:
                continue
        print(f"")
        self.selection_2c()
        return(f"{drink.drink_name}, {drink.sugar_free}, {drink.cat}")
        self.selection_2c()

    def selection_2b(self, drinks_list): # all drinks
        print(f"+================================================+")
        print(f"Drink | Sugar Free or Reduced Sugar | Catergory")
        print(f"+================================================+")
        for drink in drinks_list:
            if drink.sugar_free == 1:
                drink.sugar_free = "Reduced/No Sugar"
            else:
                drink.sugar_free = "Full Sugar"
            print(f"{drink.drink_name}, {drink.sugar_free}, {drink.cat}")
        print(f"")
        self.selection_2c()
        return(f"{drink.drink_name}, {drink.sugar_free}, {drink.cat}")
        self.selection_2c()

    def selection_3(self):
        print("                   Person Adder")
        selection2 = input("Please enter their firstname:\n(Ex)it\n")
        selection2 = selection2.title()
        if selection2 == "Ex":
            self.main_menu()
            return
        selection3 = input("Please enter their lastname:\n").title()
        selection4 = input("Please enter their age:\n")
        self.selection_3a(selection2, selection3, selection4)

    def selection_3a(self, selection2, selection3, selection4):
        new_person = Person(selection2, selection3, selection4)
        self.selection_3b(new_person)
        return (new_person)

    def selection_3b(self, new_person):
        try:
            self.db.add_person_to_db(new_person)
            self.selection_3()
        except Exception as error:
            print(f"Duplicate entry! Technical things: {error}")
        self.selection_3()

    def selection_4(self, selection2, selection4, selection5):
        new_drink = Drink(selection2, selection4, selection5)
        self.selection_4a(new_drink)
        return(new_drink.drink_name)

    def selection_4b_drink_input_getter(self):
        print("                   Drink Adder")
        selection2 = input("Please enter the drink name:\n(Ex)it\n")
        selection2 = selection2.title()
        if selection2.lower() == "ex":
            self.main_menu()
            return
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
        self.selection_4(selection2, selection4, selection5)

    def selection_4a(self, drink_object):
        try:
            self.db.load_drinks()
            self.db.add_drink_to_db(drink_object)
            self.selection_4b_drink_input_getter()
        except Exception as error:
            print(f"Duplicate entry! Technical things: {error}")
        self.selection_4b_drink_input_getter()

    def selection_5(self):
        print("                   Person Deleter")
        db_people_save_list = self.db.load_person()
        selection1b = str(input("Please enter the name or age you'd like to search for and delete:\n(Ex)it\n").title())
        people_delete_list = []
        for person in db_people_save_list:
            if selection1b in person.first_name + " " + person.last_name:
                people_delete_list.append(person)
            if selection1b == str(person.age):
                people_delete_list.append(person)
            if selection1b == person.first_name + " " + str(person.age):
                people_delete_list.append(person)
            if selection1b == person.last_name + " " + str(person.age):
                people_delete_list.append(person)
            if selection1b == str(person.age):
                people_delete_list.append(person)
            elif selection1b == "Ex":
                self.main_menu()
                return
            else:
                continue
        self.selection_5a(people_delete_list)

    def selection_5a(self, people_to_delete):
        try:
            self.db.delete_from_people_db(people_to_delete)
        except Exception as error:
            print(f"{error}")
            self.main_menu()
        print("The following entries were deleted:")
        print(f"+=========================+")
        print(f"Firstname | Lastname | Age")
        print(f"+=========================+")
        for person in people_to_delete:
            print(f"{person.person_id} {person.first_name} {person.last_name} {person.age}")
        self.selection_5()
        return(people_to_delete)

    def selection_6(self): ### Currently a bit broken ###
        self.db.load_drinks()
        print("                   Drink Deleter")
        selection1b = input("Please enter the drink you wish to delete:\n(E)xit\n").title()
        drinks_delete_list = []
        for drink in db_drinks_save_list:
            if selection1b in drink.drink_name:
                drinks_delete_list.append(drink)
                if drink.sugar_free == 1:
                    drink.sugar_free = "Reduced/No Sugar"
                else:
                    drink.sugar_free = "Full Sugar"
                print(f"{drink.drink_name}, {drink.sugar_free} has been deleted!")
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
        self.selection_6()
        return (drinks_to_delete)

    def selection_7_get_brewer_id(self):
        found_person = None
        people_list = self.db.load_person()
        while found_person == None:
            selection1 = input("Please enter the brewer's first name:\n(Ex)it\n").capitalize()
            if selection1 == "Ex":
                self.main_menu()
            selection2 = input("Please enter the brewer's last name:\n").capitalize()
            for person in people_list:
                if selection1 + " " + selection2 == person.first_name + " " + person.last_name:
                    found_person = person
            if found_person == None:
                print(f"Sorry, {selection1} could not be found, try again:")
        return found_person


    def selection_7a_get_drinker_id(self):
        found_person = None
        people_list = self.db.load_person()
        while found_person == None:
            selection1 = input("Please enter the drinker's first name:\n(Ex)it\n").capitalize()
            if selection1 == "Ex":
                self.main_menu()
            selection2 = input("Please enter the drinkers last name:\n").capitalize().strip()
            for person in people_list:
                if selection1 == person.first_name and selection2 == person.last_name:
                    found_person = person
            if found_person == None:
                print(f"Sorry, {selection1} could not be found, try again:")
        return found_person

    def selection_7b_get_drink_id(self):
        found_drink = None
        drink_list = self.db.load_drinks()
        while found_drink == None:
            selection1 = input("Please enter the drink:\n(Ex)it\n").title().strip()
            if selection1 == "Ex":
                self.main_menu()
            for drink in drink_list:
                if selection1 == drink.drink_name:
                    found_drink = drink
            if found_drink == None:
                print(f"Sorry, {selection1} could not be found, try again:")
        return (found_drink)

    def selection_7c_round_builder(self):
        brewer_info = []
        csv_brewer_info=[]
        round_list = []
        csv_round_list = []
        person = self.selection_7_get_brewer_id()
        brewer_info.append(person)
        csv_brewer_info.append(f"Round master: {person.first_name}")
        DT_tuple = self.selection_7d_date_getter()
        date_raw = DT_tuple[0]
        date = "Date created: " + DT_tuple[0]
        brewer_info.append(date_raw)
        csv_brewer_info.append(date)
        raw_ID = DT_tuple[1]
        brewer_info.append(raw_ID)
        ID = "round CSV ID: " + DT_tuple[1]
        brewer_info.append(ID)
        csv_brewer_info.append(ID)
        selection = 'y'
        while selection != 'n':
            drinker = self.selection_7a_get_drinker_id()
            drink = self.selection_7b_get_drink_id()
            round_list.append((drinker, drink))
            csv_round_list.append((drinker.first_name, drinker.last_name, drink.drink_name))
            selection = input("would you like to add a drinker and drink?:\n(Y)es\n(N)o\n").lower()
        selection = input("Would you like generate a CSV?:\n(Y)es\n(N)o\n").lower()
        if selection == 'y':
            filename = f"{person.first_name} {date} {ID}"
            self.save_round_csv(csv_brewer_info, csv_round_list, filename)
        selection = input("Would you like to save to database?:\n(Y)es\n(N)o\n").lower()
        if selection == 'y':
            self.save_round_to_db(brewer_info, round_list)
        print(f"Build again or exit!")
        self.main_menu()

    def save_round_csv(self, brewer_info, round_list, file_name):
        try:
            with open(file_name, "w") as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                csv_writer.writerow(brewer_info)
                csv_writer.writerow("")
                for line in round_list:
                    csv_writer.writerow(line)
                print(f"Round saved as CSV of filename {file_name}")
        except Exception as error:
            print(f"Sorry, failed: {error}")

    def save_round_to_db(self, round_info, round_list):
        self.db.round_to_db(round_info, round_list)

    def selection_7d_date_getter(self):
        now = datetime.datetime.now()
        date = now.strftime(f"%Y-%m-%d")
        ID = now.strftime(f"%H%M%S")
        return((date, ID))

    def selection_8_input(self):
        selection1 = input("Would you like to search you return all previous rounds:\n(A)ll\n(S)earch\n(Ex)it\n").lower()
        if selection1 == 'a':
            self.selection_8_return_all()
        elif selection1 == 's':
            self.selection_8_input_search()
        else:
            self.main_menu()

    def selection_8_return_all(self):
        raw_round_list = self.db.all_round()
        print(f"+==================================================+")
        print(f"Round ID, Drinker, Drink, Brewer name, Date of Round")
        print(f"+==================================================+")
        for line in raw_round_list:
            print(f"ID: {line[4]}, {line[6]} {line[7]}, {line[5]}, {line[8]} {line[9]}, Date: {line[3]}")
        print(f"+==================================================+")
        self.selection_8_input()

    def selection_8_input_search(self):
        raw_round_list = self.db.all_round()
        selection1 = input("Please enter the name of the brewer, drinker, date of creation or unique round ID:\n(Ex)it\n").title()
        if selection1 == 'Ex':
            self.main_menu()
        print(f"+==================================================+")
        print(f"Round ID, Drinker, Drink, Brewer name, Date of Round")
        print(f"+==================================================+")
        for line in raw_round_list:
            if str(selection1) in str(line):
                print(f"ID: {line[4]}, {line[6]} {line[7]}, {line[5]}, {line[8]} {line[9]}, Date: {line[3]}")
        print(f"+==================================================+")
        self.selection_8_input_search()

if __name__ == '__main__':
    app = App(db=Database())
    art.art()
    app.main_menu()