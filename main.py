from database import initialize_database
from database import new_Connection
from database import modifiable_attributes
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
    cursor.execute("INSERT INTO record_book (NAME, CATEGORY, COST, DATE) VALUES (?, ?, ?, ?)", (name, category, cost, date))
    connect.commit()
    cursor.close()
    connect.close()



def edit_transaction():
    given_ID = input("Please provide id of transaction you wish to edit: ")
    connect = new_Connection()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM record_book WHERE ID = ?", (given_ID))
    row = cursor.fetchone()
    if row is None:
        print("A transaction with that ID does not exist. Please provide an existing ID")
    else:
        print("Transaction found! ")
        while True:
            print("1) Name      2) Category      3) Cost      4) Date       5) Quit")
            attribute = input("Please select a number from the list above. If no more edits requested, please type 5: ")
            if attribute == "5":
                return False
            while attribute not in ["1", "2", "3", "4", "5"]:
                print("1) Name      2) Category      3) Cost      4) Date       5) Quit\n")
                attribute = input("Please select a number from the list above. If no more edits requested, please type 5: ")

            match attribute:
                case "1":
                    new_name = input("What would you like new name to be?: ")
                    cursor.execute("UPDATE record_book SET NAME = ? WHERE ID = ?", (new_name, given_ID))
                    connect.commit()
                case "2":
                    new_cat = input("What would you like new category to be?: ")
                    print(f"Available categories: {models.models.categories}")
                    cursor.execute("UPDATE record_book SET CATEGORY = ? WHERE ID = ?", (new_cat, given_ID))
                    connect.commit()
                case "3":
                    new_cost = input("What would you like new cost to be?: ")
                    cursor.execute("UPDATE record_book SET COST = ? WHERE ID = ?", (new_cost, given_ID))
                    connect.commit()
                case "4":
                    new_date = input("What would you like new date to be?: ")
                    cursor.execute("UPDATE record_book SET DATE = ? WHERE ID = ?", (new_date, given_ID))
                    connect.commit()
                case "5":
                    return False
        #END OF WHILE
    connect.commit()
    cursor.close()
    connect.close()


def main():
    #Create new table record book if not existent 
    initialize_database()
    #add_transaction()
    edit_transaction()


main()
    