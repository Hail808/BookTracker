import json
import os

library = []
file_name = "library.json"

def create_library():
    # create only if library.json doesn't already exist
    if not os.path.exists(file_name):
        with open(file_name, "w") as json_file:
            json.dump(library, json_file, indent=4)

def add_to_library(book):
    books = load_books()
    books.append(book)
    save_books(books)

def load_books():
    with open(file_name, "r") as file:
        library_data = json.load(file)
    return library_data

def save_books(books):
    with open(file_name, "w") as file:
        json.dump(books, file, indent=4)