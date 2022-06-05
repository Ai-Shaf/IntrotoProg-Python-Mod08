# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# AShafique,6.2.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strData = ''

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AShafique, 6.2.2022,Modified code to complete assignment 8
    """

    # ---Constructor--- #
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    # ---Overwrite the string method--- #
    def __str__(self):
        return self.product_name + ' | ' + self.product_price

    # ---Properties of Class: Accessor and Mutator--- #
    # ---Product Name Getter--- #
    @property
    def product_name(self):
        return str(self.__product_name).title()

    # ---Product Name Setter--- #
    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product name cannot be numeric!")

    # ---Product Price Getter--- #
    @property
    def product_price(self):
        return str(self.__product_price)

    # ---Product Price Setter--- #
    @product_price.setter
    def product_price(self, value):
        if bool(float(value)) is True:  # check if string value can be converted to float
            self.__product_price = value
        else:
            raise Exception("Product price must be a float!")


# Data -------------------------------------------------------------------- #
# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AShafique,6.2.2022,Modified code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        with open(file_name, 'w') as file:
            for row in list_of_product_objects:
                file.write(row.__str__() + '\n')
            file.close()

    @staticmethod
    def read_data_from_file(file_name):
        list_of_product_objects = []
        try:
            file = open(file_name, 'r')
            for each in file:
                name, price = each.split('|')
                name = name.strip()
                price = price.strip()
                product_obj = Product(name, price)
                list_of_product_objects.append(product_obj)


        except FileNotFoundError as e:
            print("File not found. You can add data and create file.")
        except Exception as e:
            print("No data.")
        finally:
            return list_of_product_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Takes input from user and outputs processed data:

    methods:
        display_menu() -> prints out menu of options for user to choose from
        menu_choice() -> returns the user's choice from menu
        display_file_data(file_name) -> displays the data from the file
        display_table_data(list_table) -> iterates over list and displays the line items
        get_user_data() -> returns inputted user data
    changelog: (Who, When, What)
        RRoot, 1.1.2030, Created Class
        AShafique, 6.2.2022, Added code to complete assignment 8
    """

    @staticmethod
    def display_menu():
        print(
            """
            Menu of Options:
                1 - Display current data in table
                2 - Add data
                3 - Save data to file
                4 - Read data from file
                5 - Clear data from list
                6 - Exit
            """
        )

    @staticmethod
    def menu_choice():
        choice = input("Enter choice from menu (1,2,3,4, 5, or 6): ")
        return choice

    @staticmethod
    def display_file_data(file_name):
        print('Product Name' + '|' + 'Product Price')
        try:
            table_lst = FileProcessor.read_data_from_file(file_name)
            for each in table_lst:
                print(each)
        except FileNotFoundError as err:
            print("File or data not found.")
            print(err)
        except TypeError as err:
            print("Empty list is not iterable")
            print(err)
        except Exception as err:
            print(err)

    @staticmethod
    def display_table_data(list_table):
        try:
            print('Product Name' + '|' + 'Product Price')
            for line in list_table:
                print(line.__str__())
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)


    @staticmethod
    def get_user_data():
        try:
            name = input("Name a product to enter: ")
            price = (input("Name a price for the product: ")).strip('$')
            data = Product(name, price)  # creates an instance of the Product class, using user inputted data
        except Exception as ee:  # if the user inputted data does not conform to the class properties, it throws an exception
            print("Product name must be letters and product price must be numerical(decimals ok).")
        else:
            return data  # if there are no exceptions, the function returns the string for the object instance

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #


# Load data from file into a list of product objects when script starts
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
except AttributeError as e:
    print("Empty data.")
except TypeError as e:
    print("No data yet to iterate.")
except Exception as e:
    print("Error: ")
    print(e)


while True:
    # Show user a menu of options
    IO.display_menu()

    # Get user's menu option choice
    strChoice = IO.menu_choice()

    # Show user current data in the list of product objects
    if strChoice == '1':
        IO.display_table_data(lstOfProductObjects)

    # Let user add data to the list of product objects
    elif strChoice == '2':
        strData = IO.get_user_data()
        if bool(strData) == True:
            lstOfProductObjects.append(strData)
            IO.display_table_data(lstOfProductObjects)
        else:
            print("Item not added. Check inputted product name and price.")
        continue

    # let user save current data to file and exit program
    elif strChoice == '3':
        try:
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("Data Saved!")
        except FileNotFoundError as error:
            print("File not found. Data not saved.")
            print(error)
        except Exception as error:
            print("Some error. Data not saved.")
            print(error)
        continue

    # Display data from file to user
    elif strChoice == '4':
        IO.display_file_data(strFileName)

    # Clear data from list
    elif strChoice == '5':
        lstOfProductObjects.clear()

    # Allow user to exit the program
    elif strChoice == '6':
        strExit = input("Exit without saving? 'y' or 'n': ")
        if strExit.lower() == 'y':
            print("Exiting program. Data NOT saved.")
            break
        else:
            continue

    else:
        print("Choose only 1, 2, 3, 4, or 5!")

# Main Body of Script  ---------------------------------------------------- #

