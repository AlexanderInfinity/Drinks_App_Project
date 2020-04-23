import pymysql
from os import environ
from classes.all_classes import Drink, Person

db_drinks_save_list = []
db_people_save_list = []

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

    # def update_sql(sql_string, args):
    #     connection = self.get_connection()
    #     try:
    #         with connection.cursor() as cursor:
    #             cursor.execute(sql_string, args)
    #         connection.commit()
    #     except Exception as error:
    #         print("Unable update or insert: \n{error}")
    #     finally:
    #         connection.close()

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
            print(f"{new_person.first_name}n added to database!")

    def add_drink_to_db(self): # need to fix like add person to db
        connection = self.get_connection()
        cursor = connection.cursor()
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
        new_drink = Drink(selection2, selection4, selection5)
        if new_drink.id == None:
            args = (new_drink.drink_name, new_drink.sugar_free, new_drink.cat)
            cursor.execute("INSERT INTO drinks (drink_name, sugar_free, cat) VALUES (%s, %s, %s)", args)
            connection.commit()
            cursor.close()
            connection.close()
            if new_drink.sugar_free == 1:
                new_drink.sugar_free = "Sugar Free"
            else:
                new_drink.sugar_free = "Full Sugar"
            print(f"{new_drink.drink_name}, {new_drink.sugar_free}, {new_drink.cat} was added to the database")

    def delete_from_people_db(self, people_to_delete):
        connection = self.get_connection()
        cursor = connection.cursor()
        for person in people_to_delete:
            args = (person.person_id)
            cursor.execute("DELETE FROM person WHERE id=%s", args)  # %s prevents SQL injection!

    def delete_from_drinks_db(self, drinks_to_delete):  # Need to fix like delete from people db.
        connection = self.get_connection()
        cursor = connection.cursor()
        for drink in drinks_to_delete:
            args = (drink.id)
            cursor.execute("DELETE FROM drinks WHERE id=%s", args)  # %s prevents SQL injection!

    def insert_both_sugar_options(drink):
        # Insert it
        drink.sugar_free = not drink.sugar_free
        # Insert it
