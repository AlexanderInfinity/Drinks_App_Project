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
            args = (new_person.first_name, new_person.last_name, new_person.age)
            sql_string = "INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)"
            self.update_sql(sql_string, args)
            print(f"{new_person.first_name} added to database!")

    def add_drink_to_db(self, new_drink): # need to fix like add person to db
            args = (new_drink.drink_name, new_drink.sugar_free, new_drink.cat)
            sql_string = "INSERT INTO drinks (drink_name, sugar_free, cat) VALUES (%s, %s, %s)"
            self.update_sql(sql_string, args)
            args = (new_drink.drink_name, self.insert_both_sugar_options(new_drink), new_drink.cat)
            self.update_sql(sql_string, args)
            print(f"{new_drink.drink_name}, {new_drink.sugar_free}, {new_drink.cat} was added to the database")

    def insert_both_sugar_options(self, new_drink):
        if new_drink.sugar_free == 1:
            new_drink.sugar_free = 0
        else:
            new_drink.sugar_free = 1
        return(new_drink.sugar_free)

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

    def round_to_db(self, round_info, drinker_info):
        for drinker in drinker_info:
            args = round_info[0].person_id, round_info[1], drinker[0].person_id, drinker[1].id, round_info[2]
            sql_string = "INSERT INTO round(round_master_person_id, date, person_id, drink_id,  unique_id) VALUES (%s, %s, %s, %s, %s)"
            self.update_sql(sql_string, args)
        print(f"{round_info[0].first_name}'s round was saved to the db!")

    def load_round(self):
        sql_string = f"SELECT * FROM round"
        round_table = self.sql_load_all(sql_string)
        return round_table

    def all_round(self):
        loaded_round_list = self.load_round()

        clean_round_list = []
        for line in loaded_round_list:
            person_id, drink_id, brewer_id, date, unique_id = line[1:6]
            date = str(date)
            date.replace("-", " ")
            clean_round_list.append((person_id, drink_id, brewer_id, date, unique_id))

        people_join_list = self.get_all_people_joins()

        drink_join_list = self.get_all_drink_joins()

        clean_drink_join_list = []
        for line in drink_join_list:
            clean_drink_join_list.append((line[0],))

        brewer_join_list = self.get_all_brewer_joins()

        zip_clean_round_list = zip(clean_round_list, clean_drink_join_list, people_join_list, brewer_join_list)
        clean_list = []
        for tuple in zip_clean_round_list:
            tuple_list = [element for tupl in tuple for element in tupl]
            clean_list.append(tuple_list)
        return(clean_list)

    def get_all_drink_joins(self):
        sql_string = f"SELECT d.drink_name FROM round r JOIN drinks d ON r.drink_id = d.id;"
        drink_join_list = self.sql_load_all(sql_string)
        return(drink_join_list)

    def get_all_people_joins(self):
        sql_string = f"SELECT p.first_name, p.last_name FROM round r JOIN person p ON r.person_id = p.id;"
        people_join_list = self.sql_load_all(sql_string)
        return(people_join_list)

    def get_all_brewer_joins(self):
        sql_string = f"SELECT p.first_name, p.last_name FROM round r JOIN person p ON r.round_master_person_id = p.id;"
        brewer_join_list = self.sql_load_all(sql_string)
        return(brewer_join_list)

    def update_sql(self, sql_string, args):
        connection = self.get_connection()
        with connection.cursor() as cursor:
            cursor.execute(sql_string, args)
        connection.commit()
        connection.close()