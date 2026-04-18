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