import os, sys
import requests
from xml.dom import minidom
from prettytable import PrettyTable

# Reader is a terminal application that greets old friends warmly,
#   and remembers new friends.

def display_title_bar():
        # Clears the terminal screen, and displays a title bar.
        os.system('clear')
                  
        print("\t**********************************************")
        print("\t***  Reader - A terminal app for searching and downloading books!  ***")
        print("\t**********************************************")

def get_user_input():
        # Let users know what they can do.
        print("\n[1] Sugamya Pustakalya")
        print("[2] Bookshare")
        print("[3] Gutenberg")
        print("[4] Local Books")
        print("[q] Quit")
        return input("What would you like to do? ") # change input to raw_input if using python 2.7


class SugamyaPustakalya():

    KEY = 'D72551A2C3319E892DF355AAB1C55FCEEAE91A2236C39B931513155440537'
    URL = 'https://library.daisyindia.org/NALP/rest/NALPAPIService/getNALPData/'

    ### FUNCTIONS ###

    def __init__(self):
        self.userid = ''
        self.password = ''
        
    def get_user_choice(self):
        # Let users know what they can do.

        print("\n\t***  SUGAMYA PUSTAKALYA  ***")
        print("\t**********************************************")

        print("\n[1] Latest books")
        print("[2] Popular books")
        print("[3] Search Books")
        print("[4] Book Categories")
        print("[5] Downloads")
        print("[6] Login")
        print("[b] Go Back")
        print("[q] Quit")
        
        return input("What would you like to do? ") # change input to raw_input if using python 2.7

    def process_user_choice(self):
        choice = ''
        display_title_bar()

        while choice != 'b':    
            # Respond to the user's choice.
            choice = self.get_user_choice()
            display_title_bar()
            if choice == '1':
                self.get_latest_books()
            elif choice == '2':
                self.get_popular_books()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.get_book_categories()
            elif choice == 'q':
                print("\nThanks for using Reader. Bye.")
                sys.exit(0)
            elif choice == 'b':
                print("\nHome")
            else:
                print("\nInvalid choice.\n")
        

    def get_latest_books(self):
        # Get latest books from Sugamya Pustakalya
        try:
            data = requests.get(self.URL + "latest/page/1/limit/20/format/JSON?API_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e);
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('title')
            if(len(books) == 0):
                print("No books found")
            else:
                for book in books:
                    print(book.firstChild.nodeValue)
        else:
            print("Error, server replied with", data.status_code)


    def get_popular_books(self):
        # Get popular books from Sugamya Pustakalya
        try:
            data = requests.get(self.URL + "popularbooks/noOfTimesDelivered/1/startDate/2017-01-01/endDate/2017-12-15/page/1/limit/17/format/xml?API_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('title')
            if(len(books) == 0):
                print("No books found")
            else:
                for book in books:
                    print(book.firstChild.nodeValue)
        else:
            print("Error, server replied with", data.status_code)


    def get_book_categories(self):
        # Get popular books from Sugamya Pustakalya
        try:
            data = requests.get(self.URL + "categorylist/page/1/limit/52/format/xml?API_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            categories = parsedData.getElementsByTagName('title')
            if(len(categories) == 0):
                print("No books found")
            else:
                for category in categories:
                    print(category.firstChild.nodeValue)
        else:
            print("Error, server replied with", data.status_code)


    def search_book(self):
        # Search books by Title/Author from user given user input
        search = input("Enter book Title/Author: ")
        try:
            data = requests.get(self.URL + "authortitle/" + search + "/page/1/limit/25/format/xml?API_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('title')
            if(len(books) == 0):
                print("No books found")
            else:
                for book in books:
                    print(book.firstChild.nodeValue)
        else:
            print("Error, server replied with", data.status_code)


    def login():
        USERID = input("User ID/ Email: ")
        PASSWORD = input("Password: ")


class Bookshare():

    KEY = 'xj4d2vektus5sdgqwtmq3tdc'
    URL = 'https://api.bookshare.org/book/'

    def __init__(self):
        self.userid =''
        self.password =''

    def get_user_choice(self):
        # Let users know what they can do.
        print("\n\t***  BOOKSHARE  ***")
        print("\t**********************************************")

        print("\n[1] Latest books")
        print("[2] Popular books")
        print("[3] Search Books")
        print("[4] Book Categories")
        print("[5] Login")
        print("[b] Go Back")
        print("[q] Quit")
        
        return input("What would you like to do? ") # change input to raw_input if using python 2.7

    def process_user_choice(self):
        choice = ''
        display_title_bar()

        while choice != 'b':    
            # Respond to the user's choice.
            choice = self.get_user_choice()
            display_title_bar()
            if choice == '1':
                self.get_latest_books()
            elif choice == '2':
                self.get_popular_books()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.get_book_categories()
            elif choice == 'q':
                print("\nThanks for using Reader. Bye.")
                sys.exit(0)
            elif choice == 'b':
                print("\nHome")
            else:
                print("\nInvalid choice.\n")
        

    def get_latest_books(self):
        # Get latest books from bookshare.org
        try:
            data = requests.get(self.URL + "latest/format/xml?api_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e);
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.childNodes[1].firstChild.nodeValue, book.childNodes[5].firstChild.nodeValue, book.childNodes[3].firstChild.nodeValue])
                t.align = "l"
                print(t)
        else:
            print("Error, server replied with", data.status_code)


    def get_popular_books(self):
        # Get popular books from bookshare.org
        try:
            data = requests.get(self.URL + "popular/format/xml?api_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.childNodes[1].firstChild.nodeValue, book.childNodes[5].firstChild.nodeValue, book.childNodes[3].firstChild.nodeValue])
                t.align = "l"
                print(t)
        else:
            print("Error, server replied with", data.status_code)


    def get_book_categories(self):
        # Get popular books from bookshare.org
        try:
            data = requests.get("https://api.bookshare.org/reference/category/list/format/xml?api_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            categories = parsedData.getElementsByTagName('name')
            if(len(categories) == 0):
                print("No books found")
            else:
                print("BOOK CATEGORIES")
                all_categories = []
                for category in categories:
                    print(category.firstChild.nodeValue)
                    all_categories.append(category.firstChild.nodeValue)
                response = ''
                while(response not in all_categories and response != 'b'):
                    if(response != ''):
                        print("Invalid choice, try again")
                    print("\nEnter a category to search")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.category_search(response)


        else:
            print("Error, server replied with", data.status_code)


    def category_search(self, category_name):
        # Get books of a particular category

        try:
            data = requests.get(self.URL + "search/category/" + category_name + "/format/xml?api_key=" + self.KEY, verify=False)
        except Exception as e:
            print(e)
        if(data.status_code == 200):
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.childNodes[1].firstChild.nodeValue, book.childNodes[5].firstChild.nodeValue, book.childNodes[3].firstChild.nodeValue])
                t.align = "l"
                print(t)
        else:
            print("Error, server replied with", data.status_code)

    def search_book(self):
        # Search books by Title/Author from user given user input
        search = input("Enter book Title/Author: ")
        try:
            data = requests.get(self.URL + "search/" + search + "/format/xml?api_key=" + self.KEY, verify=False)# during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.childNodes[1].firstChild.nodeValue, book.childNodes[5].firstChild.nodeValue, book.childNodes[3].firstChild.nodeValue])
                t.align = "l"
                print(t)
        else:
            print("Error, server replied with", data.status_code)


    def login():
        USERID = input("User ID/ Email: ")
        PASSWORD = input("Password: ")


### MAIN PROGRAM ###

# a loop where users can choose what they'd like to do.
choice = ''
display_title_bar()

while choice != 'q':    
    
    choice = get_user_input()
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        sp = SugamyaPustakalya()
        sp.process_user_choice()
    elif choice == '2':
        bs = Bookshare()
        bs.process_user_choice()
    elif choice == '3':
        search_book()
    elif choice == '4':
        get_book_categories()
    elif choice == 'q':
        print("\nThanks for using Reader. Bye.")
    else:
        print("\nInvalid choice.\n")