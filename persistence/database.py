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

    def load_person(self):
        db_people_save_list.clear()
        sql_string = f"SELECT * FROM person"
        class_arguements = self.sql_load_all(sql_string)
        for tuple in class_arguements:
            new_person = Person(tuple[1], tuple[2], tuple[3], tuple[0])
            db_people_save_list.append(new_person)
        return db_people_save_list


    def load_drinks(self):
        db_drinks_save_list.clear()
        sql_string = "SELECT * FROM drinks"  # prevent sql injection
        class_arguements = self.sql_load_all(sql_string)
        for tuple in class_arguements:
            new_drink = Drink(tuple[1], tuple[2], tuple[3], tuple[0])
            db_drinks_save_list.append(new_drink)
        return db_drinks_save_list

    def sql_load_all(self, sql_string):
        connection = self.get_connection()
        sql_load_list = []
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_string)
            connection.commit()
            while True:
                row = cursor.fetchone()
                if row == None:
                    break
                else:
                    sql_load_list.append(row)
            return(sql_load_list)
        except Exception as error:
            print(f"Unable to return all: \n{error}")
        finally:
            connection.close()

    def add_person_to_db(self, new_person):
        if new_person.person_id == None:
            db_people_save_list.append(new_person)
            args = (new_person.first_name, new_person.last_name, new_person.age)
            sql_string = "INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)"
            self.update_sql(sql_string, args)
            print(f"{new_person.first_name} added to database!")

    def add_drink_to_db(self, new_drink): # need to fix like add person to db
        if new_drink.id == None:
            args = (new_drink.drink_name, new_drink.sugar_free, new_drink.cat)
            sql_string = "INSERT INTO drinks (drink_name, sugar_free, cat) VALUES (%s, %s, %s)"
            self.update_sql(sql_string, args)
            if new_drink.sugar_free == 1:
                new_drink.sugar_free = "Sugar Free"
            else:
                new_drink.sugar_free = "Full Sugar"
            print(f"{new_drink.drink_name}, {new_drink.sugar_free}, {new_drink.cat} was added to the database")

    def insert_both_sugar_options(self):
        # Insert it
        drink.sugar_free = not drink.sugar_free
        # Insert it

    def delete_from_people_db(self, people_to_delete):
        for person in people_to_delete:
            args = (person.person_id)
            sql_string = "DELETE FROM person WHERE id=%s"  # %s prevents SQL injection!
            self.update_sql(sql_string, args)

    def delete_from_drinks_db(self, drinks_to_delete):  # Need to fix like delete from people db.
        sql_string = "DELETE FROM drinks WHERE id=%s"  # %s prevents SQL injection!
        for drink in drinks_to_delete:
            args = (drink.id)
            self.update_sql(sql_string, args)

    def update_sql(self, sql_string, args):
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_string, args)
            connection.commit()
        except Exception as error:
            print("Unable update or insert: \n{error}")
        finally:
            connection.close()

