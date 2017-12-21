import os, sys, hashlib, base64, ftplib, urllib.request
import requests
from xml.dom import minidom
from prettytable import PrettyTable
from contextlib import closing
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
            elif choice == '5':
                self.download_books()
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
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.get_book_id(response)
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
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.get_book_id(response)
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
            data = requests.get(self.URL + "category/" + category_name + "/page/1/limit/52/format/xml?API_key=" + self.KEY, verify=False)
        except Exception as e:
            print(e)
        if(data.status_code == 200):
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                   t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                   all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.get_book_id(response)
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
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.get_book_id(response)
        else:
            print("Error, server replied with", data.status_code)

    def get_book_id(self, id):
        # Search a particular book by ID
        try:
            data = requests.get(self.URL + "id/" + id + "/page/1/limit/25/format/xml?API_key=" + self.KEY, verify=False)# during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            title = parsedData.getElementsByTagName('title')[0].firstChild.nodeValue
            author = parsedData.getElementsByTagName('author')[0].firstChild.nodeValue
            synopsis = parsedData.getElementsByTagName('brief-synopsis')[0]
            print("\nTitle: " + title)
            print("Author: " + author)
            if(len(synopsis.childNodes) != 0):
                print("Synopsis: " + synopsis.firstChild.nodeValue) 

            response = ''
            while(response != 'd' and response != 'b'):
                if(response != ''):
                    print("\nInvalid choice")
                print("\n[d] To download book")
                print("[b] To go back")
                response = input("Response: ")
            if(response != 'b'):
                self.book_download_request(id)
        else:
            print("Error, server replied with", data.status_code)

    def book_download_request(self, id):
        # Download a book
        # if(self.userid == '' or self.password == ''):
        #     self.login()
        try:
            authString = "26353" + ':' "9m85twwz"
            encoded = base64.b64encode(bytearray(authString.encode())).decode()
            print(id)
            headers = {'Authorization': 'Basic ' + encoded, "page" : "1", "limit" : "1", "format" : "xml", "API_key" : self.KEY, "bookId" : id, "formatId" : '6'}
            data = requests.post("https://library.daisyindia.org/NALP/rest/NALPAPIService/raiseBookDownloadRequest", headers = headers, verify=False)
        except Exception as e:
            print(e)

        if(data.status_code == 200):
            parsedData = minidom.parseString(data.text)
            message = parsedData.getElementsByTagName('message')[0]
            print(message.firstChild.nodeValue)
        else:
            print("Error, server replied with", data.status_code) 

    def download_books(self):
        # download books that are ready for downloading
        try:
            authString = "26353" + ':' "9m85twwz"
            encoded = base64.b64encode(bytearray(authString.encode())).decode()
            print(id)
            headers = {'Authorization': 'Basic ' + encoded, "page" : "1", "limit" : "10", "format" : "xml", "API_key" : self.KEY}
            data = requests.post("https://library.daisyindia.org/NALP/rest/NALPAPIService/fetchUserDownloadRequests", headers = headers, verify=False)
        except Exception as e:
            print(e)

        if(data.status_code == 200):
            parsedData = minidom.parseString(data.text)
            print(parsedData.toxml())
            count = 1
            all_urls = {}
            books = parsedData.getElementsByTagName('result')
            t = PrettyTable(['ID', 'TITLE', 'STATUS'])
            for book in books:
                status = book.getElementsByTagName('available-to-download')[0].firstChild.nodeValue
                t.add_row([count, book.getElementsByTagName('title')[0].firstChild.nodeValue, status])
                if(status == 'Available for Download'):
                    all_urls[str(count)] = book.getElementsByTagName('downloadUrl')[0].firstChild.nodeValue
                count += 1
            t.align = "l"
            print(t)
            response = ''
            while(response not in all_urls and response != 'b'):
                if(response != ''):
                    print("\nInvalid choice")
                print("\nEnter Book ID to download an available book")
                print("[b] To go back")
                response = input("Response: ")
            if(response != 'b'):
                path = ''
                filename = 'book'
                ftp = ftplib.FTP("library.daisyindia.org") 
                ftp.login("26353", "9m85twwz") 
                ftp.cwd(path)
                ftp.retrbinary("RETR 21/User_26353/Meditation.zip, open(filename, 'wb').write)
                ftp.quit()
                # proxy = urllib.request.ProxyHandler({'http': 'proxy22.iitd.ac.in:3128'})
                # opener = urllib.request.build_opener(proxy)
                # urllib.request.install_opener(opener)
                # with closing(urllib.request.urlopen(all_urls[response])) as r:
                #     with open('file', 'wb') as f:
                #         shutil.copyfileobj(r, f)
        else:
            print("Error, server replied with", data.status_code)

    def login(self):
        USERID = input("User ID/ Email: ")
        PASSWORD = input("Password: ")




### Class for BOOKSHARE  ###

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
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.get_book_id(response)
        else:
            print("Error, server replied with", data.status_code)


    def get_popular_books(self):
        # Get popular books from bookshare.org
        try:
            data = requests.get(self.URL + "popular/format/xml?api_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text)
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                   t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                   all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.get_book_id(response)
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
                print("No categories found")
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
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                   t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                   all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.get_book_id(response)
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
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("Enter b to go back")
                    response = input("\nResponse: ")
                if(response != 'b'):
                    self.get_book_id(response)
        else:
            print("Error, server replied with", data.status_code)

    def get_book_id(self, id):
        # Search a particular book by ID
        try:
            data = requests.get(self.URL + "id/" + id + "/format/xml?api_key=" + self.KEY, verify=False)# during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            title = parsedData.getElementsByTagName('title')[0].firstChild.nodeValue
            author = parsedData.getElementsByTagName('author')[0].firstChild.nodeValue
            synopsis = parsedData.getElementsByTagName('brief-synopsis')[0]
            print("\nTitle: " + title)
            print("Author: " + author)
            if(len(synopsis.childNodes) != 0):
                print("Synopsis: " + synopsis.firstChild.nodeValue)
            response = ''
            while(response != 'd' and response != 'b'):
                if(response != ''):
                    print("\nInvalid choice")
                print("\n[d] To download book")
                print("[b] To go back")
                response = input("Response: ")
            if(response != 'b'):
                self.book_download(id)
        else:
            print("Error, server replied with", data.status_code)

    def book_download(self, id):
        # Download a book
        try:
            m = hashlib.md5.new(self.password).digest()
            data = requests.get("https://api.bookshare.org/download/content/" + id + "/version/1/for/sidbhakar@gmail.com?api_key=" + self.KEY, verify=False)# during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);

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