from database import initialize_database
from database import new_Connection
import models.models

def add_transaction():
    #Prompt user for attributes of transaction
    #TODO: Ensure attribute types given by user are of expected type 
    name = input("Name of transaction: ")
    date = input("Date of transaction (dd/mm/yy): ")

    #Prompt user for category, supplying available categories and prompting user until they provide a category that exists
    category = input(f"Please enter category from available options {models.models.categories}: ")
    category.lower()
    while category not in models.models.categories:
        category = input(f"Please enter category from available options {models.models.categories}: ")
    cost = input("Cost of transaction: ")
    
    #Create instance of transaction
    new_transaction = models.models.Transaction(name, category, cost, date)
    
    #TODO: fix order of attributes in constructor and user prompts to match sql table
    connect = new_Connection()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO record_book VALUES(name, category, cost, date)")
    cursor.close()
    connect.close()


def edit_transaction():
    givenID = input("Please provide id of transaction you wish to edit: ")
    connect = new_Connection()
    cursor = connect.cursor()
        


def main():
    #Create new table record book if not existent 
    initialize_database()


    
