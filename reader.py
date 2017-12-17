import os, sys
import requests
from xml.dom import minidom

# Reader is a terminal application that greets old friends warmly,
#   and remembers new friends.

def display_title_bar():
        # Clears the terminal screen, and displays a title bar.
        os.system('clear')
                  
        print("\t**********************************************")
        print("\t***  Reader - A terminal app for accessing Sugamya Pustakalya!  ***")
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
                print("\nGoing back")
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
            books = parsedData.getElementsByTagName('title')
            if(len(books) == 0):
                print("No books found")
            else:
                for book in books:
                    print(book.firstChild.nodeValue)
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


    def __init__(self):
        self.userid =''
        self.password =''


### MAIN PROGRAM ###

# a loop where users can choose what they'd like to do.
choice = ''
display_title_bar()

while choice != 'q':    
    
    choice = get_user_input()
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        sp = SugamyaPustakalya();
        sp.process_user_choice()
    elif choice == '2':
        get_popular_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        get_book_categories()
    elif choice == 'q':
        print("\nThanks for using Reader. Bye.")
    else:
        print("\nInvalid choice.\n")