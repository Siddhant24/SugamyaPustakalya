import os
import requests
from xml.dom import minidom

# Reader is a terminal application that greets old friends warmly,
#   and remembers new friends.

KEY = '2DE1570CE2A29DB65CDE5627F7031448D0F8F286B8D7B7B91513156038798'
URL = 'https://library.daisyindia.org/NALP/rest/NALPAPIService/getNALPData/'
USERID = ''
PASSWORD = ''

### FUNCTIONS ###
def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t**********************************************")
    print("\t***  Reader - A terminal app for accessing Sugamya Pustakalya!  ***")
    print("\t**********************************************")
    
def get_user_choice():
    # Let users know what they can do.
    print("\n[1] Latest books")
    print("[2] Popular books")
    print("[3] Search Books")
    print("[4] Book Categories")
    print("[5] Downloads")
    print("[6] Login")
    print("[q] Quit.")
    
    return input("What would you like to do? ") # change input to raw_input if using python 2.7
    
def get_latest_books():
    # Get latest books from Sugamya Pustakalya
    try:
        data = requests.get(URL + "latest/page/1/limit/20/format/JSON?API_key=" + KEY, verify=False) # during production remove verify = false
    except Exception as e:
        print(e);
    if(data.status_code == 200):       
        parsedData = minidom.parseString(data.text);
        books = parsedData.getElementsByTagName('title')
        for book in books:
            print(book.firstChild.nodeValue)
    else:
        print("Error, server replied with " + data.status_code)


def get_popular_books():
    # Get popular books from Sugamya Pustakalya
    try:
        data = requests.get(URL + "popularbooks/noOfTimesDelivered/1/startDate/2017-01-01/endDate/2017-12-15/page/1/limit/17/format/xml?API_key=" + KEY, verify=False) # during production remove verify = false
    except Exception as e:
        print(e)
    if(data.status_code == 200):       
        parsedData = minidom.parseString(data.text);
        books = parsedData.getElementsByTagName('title')
        for book in books:
            print(book.firstChild.nodeValue)
    else:
        print("Error, server replied with " + data.status_code)


def get_book_categories():
    # Get popular books from Sugamya Pustakalya
    try:
        data = requests.get(URL + "categorylist/page/1/limit/52/format/xml?API_key=" + KEY, verify=False) # during production remove verify = false
    except Exception as e:
        print(e)
    if(data.status_code == 200):       
        parsedData = minidom.parseString(data.text);
        books = parsedData.getElementsByTagName('title')
        for book in books:
            print(book.firstChild.nodeValue)
    else:
        print("Error, server replied with " + data.status_code)


def search_book():
    # Search books by Title/Author from user given user input
    search = input("Enter book Title/Author: ")
    try:
        data = requests.get(URL + "authortitle/" + search + "/page/1/limit/25/format/xml?API_key=" + KEY, verify=False) # during production remove verify = false
    except Exception as e:
        print(e)
    if(data.status_code == 200):       
        parsedData = minidom.parseString(data.text);
        books = parsedData.getElementsByTagName('title')
        for book in books:
            print(book.firstChild.nodeValue)
    else:
        print("Error, server replied with " + data.status_code)


def login():
    USERID = input("User ID/ Email: ")
    PASSWORD = input("Password: ")

### MAIN PROGRAM ###

# a loop where users can choose what they'd like to do.
choice = ''
display_title_bar()

while choice != 'q':    
    
    choice = get_user_choice()
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        get_latest_books()
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