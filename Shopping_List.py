#Import sqlite3 and initiate connection
import sqlite3
connection = sqlite3.connect('shoppinglist.db')
cursor = connection.cursor()

#while true loop to restart the program
while True:
    # Select action - user input requird
    menu = input("What would you like to do: (Add = 1 / Update = 2 / List = 3 / Delete = 4 / Quit = 5) \n")
    option = (menu)

    #To INSERT
    if option == '1':
        item = input("What item do you want to add? ")
        qty = input("How many (default=1)? ")
        cursor.execute("INSERT into Shopping_List (Name, Qty) VALUES (?,?)", [item.capitalize(), qty])
        connection.commit()
        print("Done")

    #To UPDATE
    elif option == '2':
        item = input("What item do you want to modify? ").capitalize()
        item_new = input("What do you want to replace it with? ")
        qty = input("How many (default=1)? ")
        cursor.execute("UPDATE Shopping_List SET Name = ?, Qty = ? WHERE Name = ?", [item_new.capitalize(), qty, item])
        connection.commit()
        print("Done")

    #To SELECT
    elif option == '3':
        cursor.execute("SELECT Name, Qty FROM Shopping_List")
        items = cursor.fetchall()
        print("Total number of rows = ", len(items), "\n")
        print("Shopping List: \n")
        for row in items:
            item = row[0]
            qty = row[1]
            print(qty, item)
        #connection.commit()   Not needed for SELECT

    #To DELETE
    elif option == '4':
        clear = input("Do you want to delete the whole list? 'yes or no' \n").lower()
        if clear == 'yes':
            cursor.execute("DELETE from Shopping_List")
            print("Shopping list deleted successfully")
            connection.commit()
        else:
            item = input("What item do you want to delete? ")
            check = input(f"Are you sure you wan to delete {item}? 'yes or no' \n").lower()
            if check == 'yes':
                cursor.execute("DELETE FROM Shopping_List WHERE Name = ?", [item.capitalize()])
                print(f"{item} deleted")
                connection.commit()
            else:
                print("No changes have been made")

    #To QUIT
    elif option == '5':
        break
    # If option (number) not part of the menu--->
    else:
        print("This option is not available, select another option")
