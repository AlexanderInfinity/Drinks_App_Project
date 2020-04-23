import pymysql
# from classes.all_classes import Person, Drink, Round, Alcoholic, Soft, Hot
from os import environ
from classes.all_classes import Drink, Person

db_people_save_list = []
db_drinks_save_list = []

class Database():

    def get_connection(self):  # function to get the connection string using: pymysql.connect(host, username, password, database)
        try:
            db_connection = pymysql.connect(
                environ.get("DB_HOST"),  # host
                environ.get("DB_USER"),  # username
                environ.get("DB_PW"),  # password
                environ.get("DB_NAME")  # database
            )
            return db_connection
            print("worked")
        except Exception as error:
            print(f"didn't work lol {error}")
            app.main_menu()

    def load_person(self):
        db_people_save_list.clear()
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM person")  # prevent sql injection
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            else:
                new_person = Person(row[1], row[2], row[3], row[0])  # row 0 last because it's a default
                db_people_save_list.append(new_person)
        return db_people_save_list
        cursor.close()
        connection.close()

    def load_drinks(self):
        db_drinks_save_list.clear()
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM drinks")  # prevent sql injection
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            else:
                new_drink = Drink(row[1], row[2], row[3], row[0])
                db_drinks_save_list.append(new_drink)
        return db_drinks_save_list
        cursor.close()
        connection.close()

    # def save_people_list(self): # Shouldn't ever have to save the list, all alterations to be made on SQL, then the list reloaded each time
    #     try:
    #         connection = self.get_connection()
    #         cursor = connection.cursor()
    #         for person in db_people_save_list:
    #             if person.person_id == None:
    #                 args = (person.first_name, person.last_name, person.age)
    #                 cursor.execute("INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)",
    #                                args)  # %s prevents SQL injection!
    #                 # db_people_save_list.remove(person)
    #         connection.commit()  # updates the db, stack up the queries then commit at the end to be the most efficent.
    #         cursor.close()
    #         connection.close()
    #     except Exception as error:
    #         print(f"Error: {error}")
    #
    # def save_drinks_list(self): # Shouldn't ever have to save the list, all alterations to be made on SQL, then the list reloaded each time
    #     try:
    #         connection = self.get_connection()
    #         cursor = connection.cursor()
    #         for drink in db_drinks_save_list:
    #             if drink.id == None:
    #                 args = (drink.drink_name, drink.sugar_free, drink.cat, drink.extra)
    #                 cursor.execute("INSERT INTO drinks (drink_name, sugar_free, cat, extra) VALUES (%s, %s, %s, %s)",
    #                                args)  # %s prevents SQL injection!
    #                 # db_drinks_save_list.remove(drink)
    #         connection.commit()  # updates the db, stack up the queries then commit at the end to be the most efficent.
    #         cursor.close()
    #         connection.close()
    #     except Exception as error:
    #         print(f"Error: {error}")

    def add_person_to_db(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        selection2 = input("Please enter their firstname:\n")
        selection3 = input("Please enter their lastname:\n")
        selection4 = input("Please enter their age:\n")
        new_person = Person(selection2, selection3, selection4)
        if new_person.person_id == None:
            db_people_save_list.append(new_person)
            args = (new_person.first_name, new_person.last_name, new_person.age)
            cursor.execute("INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)", args)
            connection.commit()
            cursor.close()
            connection.close()

    def add_drink_to_db(self): # need to fix like add person to db
        selection2 = input("Please enter the drink name:\n")
        selection4 = input("Is the drink sugar free?:\n(Y)es\n(N)o\n")
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
        selection6 = input("Please enter any extras:\nHit return to skip\n")
        new_drink = Drink(selection2, selection4, selection5, selection6)
        args = (new_drink.drink_name, new_drink.sugar_free, new_drink.cat)
        self.cursor.execute("INSERT INTO drink (drink_name, sugar_free, cat) VALUES (%s, %s, %s)", args)
        try:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            print(f"{new_drink.drink_name}, {new_drink.sugar_free}, {new_drink.cat} was added to the database")
        except Exception as error:
            print(f"{error}")

    def delete_from_people_db(self, delete_people_list):
        connection = self.get_connection()
        cursor = connection.cursor()
        for person in delete_people_list:
            args = (person.person_id)
            cursor.execute("DELETE FROM person WHERE id=person.person_id)", args)  # %s prevents SQL injection!

    def delete_from_drinks_db(drink_name, sugar_free, cat):
        connection = get_connection()
        cursor = connection.cursor()
        args = (drink_name, sugar_free, cat)
        try:
            cursor.execute("DELETE FROM drinks WHERE (drink_name, sugar_free, cat) VALUES (%s, %s, %s)",
                           args)  # %s prevents SQL injection!
        except Exception as err:  # catches any duplicate errors, preventing it crashing out upon a duplicate.
            print("Error: {}".format(err))

    def insert_both_sugar_options(drink):
        # Insert it
        drink.sugar_free = not drink.sugar_free
        # Insert it

    #### function to generate all the permitations of a drink ####
    # def add_permutations(drink):
    #     if drink.cat == "soft":
    #         insert_both_sugar_options(drink)
    #     if drink.cat == "hot":
    #         insert_both_sugar_options(drink)
    #         drink.cat = "cold"
    #         insert_both_sugar_options(drink)
