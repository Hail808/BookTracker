import json
import os

library = []
file_name = "library.json"

def create_library():
    # create only if library.json doesn't already exist
    if not os.path.exists(file_name):
        with open(file_name, "w") as json_file:
            json.dump(library, json_file, indent=4)

def menu():
    print("\n---Menu---")
    print("1. Display Library")
    print("2. Add a Book")
    print("3. Update a Book")
    print("4. Delete a Book")
    print("5. Quit")

    choice = input("\nChoose an option: ")
    return choice

# ----- Menu options -----
def display_library():
    print("\n---Library---")
    library = load_library()

    for book in library:
        print(f"{book['id']}. {book['title']} by {book['author']} - {book['status']} | " \
              f"Current Volume: {book['currentVol']} | Current Chapter: {book['currentCh']}")

def add_book(book):
    cur_library = load_library()
    book["id"] = len(cur_library) + 1
    cur_library.append(book)
    save_library(cur_library)
    return book

def update_book(book_id, key, value):
    cur_library = load_library()
    selected_book = next(book for book in cur_library if book["id"] == book_id) 
    selected_book[key] = value
    save_library(cur_library)
    return selected_book

def delete_book():
    print("\n---Delete a Book---")
    display_library()
    cur_library = load_library()

    while True:
        try:
            selected_book = int(input("\nWhich book would you like to delete?: "))
            if 1 <= selected_book <= len(cur_library):
                break
            else:
                print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")

    delete_from_library(selected_book, cur_library)

    display_library()

# ----- Extended Functions -----
def create_book(title, author, status, curVol, curCh):
# create book with no assigned id
    book = {
        "id": 0,
        "title": title,
        "author": author,
        "status": status,
        "currentVol": curVol,
        "currentCh": curCh
    }
    return book

def add_to_library(book, cur_library):
    cur_library.append(book)
    save_library(cur_library)

def delete_from_library(book, cur_library):
    cur_library.pop(book - 1)
    for i, book in enumerate(cur_library, start=1):
        book["id"] = i
        
    save_library(cur_library)

def load_library():
    with open(file_name, "r") as file:
        library_data = json.load(file)
    return library_data

def save_library(cur_library):
    with open(file_name, "w") as file:
        json.dump(cur_library, file, indent=4)

# ----- Get Functions -----
def get_book_input():
# get user book without id
    book_title = input("Enter book title: ")
    book_author = input("Enter author: ")
    book_status = input("Enter reading status: ")
    book_curVol = input("Enter the current volume you are on: ")
    book_curCh = input("Enter the current chapter you are on: ")

    return book_title, book_author, book_status, book_curVol, book_curCh

def get_book_value_choice(book):
    book_values = list(book.items())
    for i, (key, value) in enumerate(book_values[1:], start=1):
        print(f"{i}. {key}: {value}")
    print(f"{len(book_values)}. Cancel")
    
    while True: 
        try: 
            choice = int(input("\nWhat would you like to update?: "))
            if 1 <= choice < len(book_values):
                break
            elif choice == len(book_values):
                return None
            else:
                print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")
    
    return list(book.keys())[choice]