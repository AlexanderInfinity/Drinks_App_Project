# this is all of ETL to split the customers csv into first name, last name and age and add to the person table on SQL!

import pymysql
from os import environ
from datetime import date
from ETL.Extract.extract import csv_load

title_list = ["miss","ms","mrs","mr","dr"]

def process_customers(data):
    temp_list=[]
    for row in data:
        if len(row) == 0 or row[0] == "Name": # check for empty rows or rows indicating table headers
            continue # if the above is the case skips that row
        try:
            age = age_gen(row[1]) # try to generate an age from the DOB
        except ValueError: # if that fails gives a value error
            continue # then skips that row
        first_name, last_name = name_breaker(row[0]) # assigning the values in the tuple
        customer_tuple = (first_name, last_name, age) # making a new tuple with the age and masked ccn
        temp_list.append(customer_tuple) # appending aforementioned tuple to the customer_list
    return temp_list # returns list

def name_breaker(name): # Function to reformat names into the order "title","first name", "last name"
    breaking_name = name.strip().lower().replace(".", "") # Strip away unwanted things e.g leading and trailing spaces, \n etc, formats all to lowercase and replaces any "." with ""
    broken_name = breaking_name.split(" ") # Takes breaking_name and splits where there are " " into seperate values
    last_name = broken_name[-1].title() # looks up the final index (-1) and formats it using "title" which recognises irish and double barrelled names.
    if broken_name[0] in title_list: # if the first value in broken_name is a title from the list above in title_list then continue
        title = broken_name[0].capitalize() # defining the first value as "title" and capitalising it
        first_name = broken_name[1].capitalize() # the remainin value is then defined as the "first_name"
    else:
        title = None # if there is no title then None
        first_name = broken_name[0].capitalize() #  the remainin value is then defined as the "first_name"
    return (first_name, last_name) # Either way, return the define values: title, first_name, last_name

def age_gen(dob): # generate an age from a dob
    days_in_year = 365.2425 # defines how many days are a year including leap years
    y, m, d = int(dob[:4]), int(dob[5:7]), int(dob[-2:]) # essentially splitting the dob according to the index and defining the y, m, d varibles.
    birth_date = date(y, m, d) # defining the variable "birth_date" in the "date" format using the y, m, d varables from above.
    age = int((date.today() - birth_date).days / days_in_year) # Defining variable age as: todays date subtract the birth_date, format this in number of days and divide by the days in the year.
    return age # returns age in years

def get_connection():  # function to get the connection string using: pymysql.connect(host, username, password, database)
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

def save_from_csv_to_db(list):
        connection = get_connection()
        cursor = connection.cursor()
        for tuple in list:
            first_name, last_name, age = tuple
            args = (first_name, last_name, age)
            try:
                cursor.execute("INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)", args)  # %s prevents SQL injection!
            except Exception as err: # catches any duplicate errors, preventing it crashing out upon a duplicate.
                print("Error: {}".format(err))
        connection.commit() # updates the db, stack up the queries then commit at the end to be the most efficent.
        cursor.close()
        connection.close()



load_list = csv_load("customer.csv")
transformed_list = process_customers(load_list)
print(transformed_list)
save_from_csv_to_db(transformed_list)