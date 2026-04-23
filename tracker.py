import json
import os

library = []
file_name = "library.json"

def create_library():
    # create only if library.json doesn't already exist
    if not os.path.exists(file_name):
        with open(file_name, "w") as json_file:
            json.dump(library, json_file, indent=4)

def new_book():
    new_book = read_input()

    cur_library = load_library()
    new_id = len(cur_library) + 1
    new_book["id"] = new_id

    add_to_library(new_book, cur_library)

def read_input():
    book_title = input("Enter book title: ")
    book_author = input("Enter author: ")
    book_status = input("Enter reading status: ")
    book_curVol = input("Enter the current volume you are on: ")
    book_curCh = input("Enter the current chapter you are on: ")
    book = {
        "id": 0,
        "title": book_title,
        "author": book_author,
        "status": book_status,
        "currentVol": book_curVol,
        "currentCh": book_curCh
    }
    return book

def add_to_library(book, cur_library):
    cur_library.append(book)
    save_library(cur_library)

def load_library():
    with open(file_name, "r") as file:
        library_data = json.load(file)
    return library_data

def save_library(cur_library):
    with open(file_name, "w") as file:
        json.dump(cur_library, file, indent=4)

def update_book():
    display_library()
    cur_library = load_library()

    book_choice = int(input("\nWhich book would you like to update?: "))
    book_choice = next(book for book in cur_library if book["id"] == book_choice)

    book_values = list(book_choice.items())
    for i, (key, value) in enumerate(book_values[1:], start=1):
        print(f"{i}. {key}: {value}")
    print(f"{len(book_values)}. Cancel")
    value_choice = int(input("\nWhat would you like to update?: "))

    if value_choice == len(book_values):
        return
    key = list(book_choice.keys())[value_choice]
    new_value = input(f"Enter new value for {key}: ")
    book_choice[key] = new_value

    save_library(cur_library)

    print("\n---Updated Library---")
    display_library()

def delete_book():
    display_library()
    cur_library = load_library()

    book_choice = int(input("\nWhich book would you like to delete?: "))

    cur_library.pop(book_choice - 1)
    for i, book in enumerate(cur_library, start=1):
        book["id"] = i

    save_library(cur_library)

    print("\n---Updated Library---")
    display_library()
        
def display_library():
    library = load_library()
    for book in library:
        print(f"{book['id']}. {book['title']} by {book['author']} - {book['status']} | Current Volume: {book['currentVol']} | Current Chapter: {book['currentCh']}")